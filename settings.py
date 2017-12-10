RESOURCE_METHODS = ['GET','POST']

ITEM_METHODS = ['GET','PUT']

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
                        'type': 'integer'
                    },
                    'app_timestamp': {
                        'type': 'integer'
                    },
                    'datos': {
                        'type': 'string'
                    },
                    'device_id':{
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
          }
         }
