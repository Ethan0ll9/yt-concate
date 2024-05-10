import logging


def set_logger(stream_file):
    logger = logging.getLogger('logs')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

    file_handler = logging.FileHandler('yt_concate.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_file)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
