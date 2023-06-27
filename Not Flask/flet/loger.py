import logging

class EventLogger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def info(self, message):
        logging.info(message)

    def warn(self, message):
        logging.warn(message)

    def error(self, message):
        logging.error(message)