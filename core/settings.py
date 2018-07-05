DYNACONF_NAMESPACE = 'DELAY'

LOGGING_CONFIG = {
    'version': 1,
    # DO NOT SET this to TRUE! It will disable any loggers created up until this
    # point including the loggers created for app at import time
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(name)s %(message)s'
        }
    },
    'handlers': {
        'info': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
        'error': {
            'level': 'ERROR',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr'
        }
    },
    'loggers': {
        '': {
            'handlers': ['info', 'error'],
            'level': 'INFO'
        },
        'newrelic.core': {
            'handlers': ['error'],
            'level': 'ERROR'
        }
    },
    'root': {
        'handlers': ['info', 'error'],
        'level': 'INFO'
    }
}
