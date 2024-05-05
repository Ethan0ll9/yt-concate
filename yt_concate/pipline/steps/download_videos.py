import yt_dlp
import os
from time import time
from threading import Thread
from multiprocessing import Process

from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        start = time()
        yt_set = set([found.yt for found in data])
        print('videos to download=', len(yt_set))

        threads = []

        count_videos = 0
        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            print('downloading', url)

            threads.append(Thread(target=self.download_videos, args=(yt, url)))

            count_videos += 1
            if count_videos >= inputs['video_limit']:
                break

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time()
        print(f'downloading videos took {end - start} seconds')

        return data

    def download_videos(self, yt, url):
        ydl_opt = {
            'nooverwrites': True,
            'outtmpl': yt.video_filepath
        }
        with yt_dlp.YoutubeDL(ydl_opt) as ydl:
            ydl.download([url])
