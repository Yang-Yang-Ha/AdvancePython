import logging
import logging.config

log_config = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'date_level_message',
            'stream': 'ext://sys.stdout'
        }

    },
    'formatters': {
        'date_level_message': {
            'format': '%(asctime)s - %(levelname)s : %(message)s',
            'datefmt': '%a %b %d %Y %I:%M:%S%p'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', ]
        }
    }
}
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     datefmt='%a %b %d %Y %I:%M:%S%p')
logging.config.dictConfig(log_config)


def debug(message):
    logging.debug(message)


def info(message):
    logging.info(message)


def warning(message):
    logging.warning(message)


def error(message):
    logging.error(message)


def critical(message):
    logging.critical(message)
