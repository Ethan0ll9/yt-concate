import yt_dlp

from .step import Step
from .step import StepException
from yt_concate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            if utils.caption_file_exists(url):
                print('found existing caption file')
                continue

            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'subtitlesformat': 'srt',
                'skip_download': True,
                'subtitleslangs': ['en'],
                'outtmpl': f'{CAPTIONS_DIR}/{utils.get_video_id_from_url(url)}.srt'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
