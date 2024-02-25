from yt_concate.pipline.steps.get_video_list import GetVideoList
from yt_concate.pipline.pipeline import Pipeline


CHANNEL_ID = 'UCX6OQ3DkcsbYNE6H8uQQuVA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()
