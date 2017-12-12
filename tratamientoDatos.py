import Queue
import sys
from humbledb import Mongo, Document
from datetime import datetime
from threading import Timer

class OPPosiciones(Document):
    config_database = "eve"
    config_collection = "posiciones"

class OPTemblores(Document):
    config_database = "eve"
    config_collection = "temblores"

class OPDatosSensor(Document):
    config_database = "eve"
    config_collection = "datos_sensor"

class OPDatosProcesados(Document):
    config_database = "datos_procesados"
    config_collection = "datos_sensor"

NUM_DESCARTES = 10

'''
x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

t = Timer(secs, procesarDatos)
t.start()
'''


def procesarDatos():

    with Mongo:
        dispositivos = OPDatosSensor.distinct("device_id")
        for dispositivo in dispositivos:
            posiciones = OPDatosSensor.distinct("posiciones", {"device_id": dispositivo})

            for posicion in posiciones:
                sensores = OPDatosSensor.distinct("sensor", {"device_id": dispositivo, "posiciones": posicion})
                queues = []

                for i in xrange(0, len(sensores)):
                    queues.append(OPDatosSensor.find({"sensor" : sensores[i], "posiciones": posicion, "device_id": dispositivo}, {"sensor": 1, "posiciones": 1, "db_timestamp": 1, "datos": 1, "_id": 0}))

                minimo = sys.maxint
                for queue in queues:
                    #obtenemos la lista de menor longitud
                    if minimo > queue.count():
                        minimo = queue.count()

                if minimo > NUM_DESCARTES:
                    for i in xrange(NUM_DESCARTES, minimo - NUM_DESCARTES):
                        op = OPDatosProcesados()
                        op["dispositivo"] = dispositivo
                        op["posicion"] = posicion
                        op["sensores"] = sensores
                        op["timestamp"] = queues[0][i]["db_timestamp"]
                        op["datos"] = ""
                        for queue in queues:
                            op["datos"] += queue[i]["datos"] + ";"
                        OPDatosProcesados.insert(op)

procesarDatos()
