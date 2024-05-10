import yt_dlp
from time import time
from threading import Thread
import logging

from .step import Step
from yt_concate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger(f'logs.{__name__}')
        start = time()
        threads = []

        for yt in data:
            logger.info(f'downloading caption for {yt.id}')
            if utils.caption_file_exists(yt):
                logger.info('found existing caption file')
                continue

            threads.append(Thread(target=self.download_captions, args=(yt,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time()
        logger.warning(f'downloading captions took {end - start} seconds')

        return data

    def download_captions(self, yt):
        ydl_opts = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitlesformat': 'srt',
            'skip_download': True,
            'subtitleslangs': ['en'],
            'outtmpl': f'{CAPTIONS_DIR}/{yt.get_video_id_from_url(yt.url)}.srt'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt.url])
