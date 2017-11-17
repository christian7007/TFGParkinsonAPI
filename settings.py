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
                        'type': 'timestamp'
                    }
                }
            },
          'datos_sensor': {
                'additional_lookup': {
                    'url': 'regex("[\w]+")',
                    'field': 'posiciones'
                },
                'schema': {
                    'sensor' : {
                    'type': 'string'
                    }
                    'posiciones': {
                        'type': 'integer'
                    },
                    'db_timestamp': {
                        'type': 'timestamp'
                    },
                    'app_timestamp': {
                        'type': 'timestamp'
                    },
                    'datos': {
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
                    }
                }
          }
         }
