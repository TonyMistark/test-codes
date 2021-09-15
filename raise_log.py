import logging

logger = logging.getLogger(__name__)


def s():
    try:
        int('sss')
    except ValueError as e:
        logger.exception(f"eeeee: {e=}")

s()
