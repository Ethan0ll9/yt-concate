import yt_dlp

from .step import Step
from .step import StepException
from yt_concate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            print('downloading caption for ', yt.id)
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue

            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'subtitlesformat': 'srt',
                'skip_download': True,
                'subtitleslangs': ['en'],
                'outtmpl': f'{yt.caption_filepath}.srt'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt.url])

        return data
