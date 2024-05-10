import sys
sys.path.append('../')
import getopt
import logging

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
from yt_concate.logs import set_logger


def print_usage():
    print('python main.py OPTIONS')
    print('OPTIONS:')
    print('{:>6} {:<15}{}'.format('-c', '--channel_id', 'Channel id of youtube channel to download.'))
    print('{:>6} {:<15}{}'.format('-s', '--search_word', 'Word for searching in the video.'))
    print('{:>6} {:<15}{}'.format('-e', '--edit_limit', 'Video editing restrictions.'))


def main():
    inputs = {
        'channel_id': 'UCX6OQ3DkcsbYNE6H8uQQuVA',
        'search_word': 'money',
        'edit_limit': 20,
        'logging_level': logging.WARNING,
    }

    short_opts = 'hc:s:e:l:'
    long_opts = 'help channel_id= search_word= edit_limit= logging_level='.split()
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit(0)
        elif opt in ('-c', '--channel_id'):
            inputs['channel_id'] = arg
        elif opt in ('-s', '--search_word'):
            inputs['search_word'] = arg
        elif opt in ('-e', '--edit_limit'):
            inputs['edit_limit'] = arg
        elif opt in ('-l', '--logging_level'):
            inputs['logging_level'] = arg

    set_logger(inputs['logging_level'])

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
