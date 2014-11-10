"""
This module tests if using a different logger still logs correctly.
"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
_handler = logging.StreamHandler()
_handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logger.addHandler(_handler)


def hello():
    logger.debug('Hello world!')
    return "Hello world!"

if __name__ == "__main__":
    print hello()
