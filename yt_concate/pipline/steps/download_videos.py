import yt_dlp
from time import time
from threading import Thread
import logging

from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger(f'logs.{__name__}')
        start = time()
        yt_set = set([found.yt for found in data])
        logger.info(f'videos to download= {len(yt_set)}')

        threads = []

        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                logger.info(f'found existing video file for {url}, skipping')
                continue

            logger.warning('downloading', url)

            threads.append(Thread(target=self.download_videos, args=(yt, url)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time()
        logger.info(f'downloading videos took {end - start} seconds')

        return data

    def download_videos(self, yt, url):
        ydl_opt = {
            'nooverwrites': True,
            'outtmpl': yt.video_filepath
        }
        with yt_dlp.YoutubeDL(ydl_opt) as ydl:
            ydl.download([url])
