import logging

from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger(f'logs.{__name__}')
        logger.info('in Preflight')
        utils.create_dir()
