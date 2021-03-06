RESOURCE_METHODS = ['GET','POST']

ITEM_METHODS = ['GET','PUT']

DATE_FORMAT = 'DD/MM/YYYY HH:MM'

XML = False

DOMAIN = {'temblores': {
                'additional_lookup': {
                    'url': 'regex("[\w]+")',
                    'field': 'id'
                },
                'schema':{
                    'id':{
                        'type': 'integer'
                    },
                    'duracion':{
                        'type': 'integer'
                    },
                    'observaciones':{
                        'type': 'string'
                    },
                    'timestamp_inicio':{
                        'type': 'integer'
                    },
                    'device_id':{
                        'type': 'string'
                    }
                }
            },
            'datos_sensor': {
                'additional_lookup': {
                    'url': 'regex("[\w]+")',
                    'field': 'posiciones'
                },
                'schema': {
                    'id': {
                        'type': 'integer'
                    },
                    'sensor' : {
                        'type': 'string'
                    },
                    'posiciones': {
                        'type': 'integer'
                    },
                    'db_timestamp': {
                        'type': 'string'
                    },
                    'app_timestamp': {
                        'type': 'string'
                    },
                    'datos': {
                        'type': 'string'
                    },
                    'device_id':{
                        'type': 'string'
                    },
                    'tipo_sensor':{
                        'type': 'string'
                    }
                }
          },
          'posiciones': {
                'additional_lookup': {
                    'url': 'regex("[\w]+")',
                    'field': 'id'
                },
                'schema': {
                    'id': {
                        'type': 'integer'
                    },
                    'posiciones': {
                        'type': 'string'
                    },
                    'device_id':{
                        'type': 'string'
                    }
                }
          },
          'medicamentos': {
                'additional_lookup': {
                    'url': 'regex("[\w]+")',
                    'field': 'nombre'
                },
                'schema': {
                    'nombre': {
                        'type': 'string'
                    },
                    'dias': {
                        'type': 'string'
                    },
                    'hora': {
                        'type': 'string'
                    },
                    'minutos_descartar': {
                        'type': 'integer'
                    },
                    'device_id':{
                        'type': 'string'
                    }
                }
          },
          'actividades': {
                'additional_lookup': {
                    'url': 'regex("[\w]+")',
                    'field': 'nombre'
                },
                'schema':{
                    'nombre': {
                        'type': 'string'
                    },
                    'intervalo': {
                        'type': 'integer'
                    },
                    'hora': {
                        'type': 'string'
                    },
                    'device_id':{
                        'type': 'string'
                    },
                    'observaciones': {
                        'type': 'string'
                    },
                    'fecha': {
                        'type': 'string'
                    }
                }
          },
          'usuario': {
              'additional_lookup': {
                    'url': 'regex("[\w]+")',
                    'field': 'nombre'
                },
                'schema': {
                    'nombre': {
                        'type': 'string',
                        'unique': True
                    },
                    'password': {
                        'type': 'string'
                    }
                }
          },
          'paciente': {
              'additional_lookup': {
                    'url': 'regex("[\w]+")',
                    'field': 'nombre'
                },
                'schema': {
                    'nombre': {
                        'type': 'string',
                        'unique': True
                    },
                    'device_id': {
                        'type': 'string',
                        'unique': True
                    }
                }
          },
          'tomas': {
              'additional_lookup': {
                    'url': 'regex("[\w]+")',
                    'field': 'medicamento'
                },
                'schema': {
                    'medicamento': {
                        'type': 'string'
                    },
                    'hora': {
                        'type': 'string'
                    },
                    'fecha': {
                        'type': 'string'
                    },
                    'tomado': {
                        'type': 'string'
                    },
                    'device_id': {
                        'type': 'string',
                        'unique': True
                    }
                }
          }
}
