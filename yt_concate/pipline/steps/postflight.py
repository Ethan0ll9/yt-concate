import logging

from .step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger(f'logs.{__name__}')
        logger.info('in Postflight')
