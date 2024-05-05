from yt_concate.pipline.steps.get_video_list import GetVideoList
from yt_concate.pipline.steps.initialize_yt import InitializeYT
from yt_concate.pipline.steps.download_caption import DownloadCaptions
from yt_concate.pipline.steps.read_caption import ReadCaption
from yt_concate.pipline.steps.search import Search
from yt_concate.pipline.steps.download_videos import DownloadVideos
from yt_concate.pipline.steps.edit_video import EditVideo
from yt_concate.pipline.steps.preflight import Preflight
from yt_concate.pipline.steps.postflight import Postflight
from yt_concate.pipline.pipeline import Pipeline
from yt_concate.utils import Utils


CHANNEL_ID = 'UCX6OQ3DkcsbYNE6H8uQQuVA'
SEARCH_WORD = 'money'
CAPTION_LIMIT = 30
VIDEO_LIMIT = 10
EDIT_LIMIT = 20


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': SEARCH_WORD,
        'caption_limit': CAPTION_LIMIT,
        'video_limit': VIDEO_LIMIT,
        'edit_limit': EDIT_LIMIT,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()
