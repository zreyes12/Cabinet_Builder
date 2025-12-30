### logs/logger.py

import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='../logs/app.log',
                        filemode='a')
    return logging.getLogger(__name__)
