import logging

from .step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger(f'logs.{__name__}')
        search_word = inputs['search_word']
        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)

        logger.info(f'The found quantity is {len(found)}')
        return found
