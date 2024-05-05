import yt_dlp
import os
from time import time
from threading import Thread
from multiprocessing import Process

from .step import Step
from yt_concate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time()
        threads = []

        count_captions = 0
        for yt in data:
            print('downloading caption for ', yt.id)
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue

            threads.append(Thread(target=self.download_captions, args=(yt,)))

            count_captions += 1
            if count_captions >= inputs['caption_limit']:
                break

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time()
        print(f'downloading captions took {end - start} seconds')

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
