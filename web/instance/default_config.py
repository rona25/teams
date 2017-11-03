import os

DEBUG = True
JSONIFY_PRETTYPRINT_REGULAR = False

JSON_DATA_DIR = os.path.realpath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'data',
        'teams',
    )
)

LOG_CONFIG = {
    'loggers': {
        'teams': {
            'handlers': [
                'console'
            ],
            'level': 'DEBUG',
            'propagate': False
        }
    },
    'root': {
        'handlers': [
            'console'
        ],
        'level': 'INFO'
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
            'stream': 'ext://sys.stdout',
        },
    },
    'formatters': {
        'default_formatter': {
            'format': '%(asctime)s %(levelname)s [%(name)s] %(message)s',
        }
    },
    'version': 1,
}