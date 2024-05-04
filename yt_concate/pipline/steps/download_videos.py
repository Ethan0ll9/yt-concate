import yt_dlp

from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('videos to download=', len(yt_set))

        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            print('downloading', url)
            ydl_opt = {
                'writesubtitles': True,
                'nooverwrites': True,
                'outtmpl': yt.video_filepath
            }
            with yt_dlp.YoutubeDL(ydl_opt) as ydl:
                ydl.download([url])

        return data
