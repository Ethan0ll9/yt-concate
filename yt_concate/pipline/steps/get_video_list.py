from googleapiclient.discovery import build

from yt_concate.pipline.steps.step import Step
from yt_concate.settings import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs["channel_id"]

        if utils.video_list_exists(channel_id):
            print('Found existing video_list for channel_id ', channel_id)
            return self.read_to_file(utils.get_video_list_filepath(channel_id))

        youtube = build(
            'youtube',
            'v3',
            developerKey=API_KEY
        )

        request = youtube.channels().list(
            part='contentDetails',
            id=channel_id
        )

        response = request.execute()

        playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        videos = []
        next_page_token = None

        while True:
            playlist_items_response = youtube.playlistItems().list(
                        part='snippet',
                        playlistId=playlist_id,
                        maxResults=50,
                        pageToken=next_page_token
            ).execute()

            videos += playlist_items_response['items']

            next_page_token = playlist_items_response.get('nextPageToken')

            if not next_page_token:
                break

        video_urls = []

        for video in videos:
            video_id = video['snippet']['resourceId']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_urls.append(video_url)

        self.write_to_file(video_urls, utils.get_video_list_filepath(channel_id))
        return video_urls

    def write_to_file(self, video_links, filepath):
        with open(filepath, 'w') as f:
            for url in video_links:
                f.write(url + '\n')

    def read_to_file(self, filepath):
        video_links = []
        with open(filepath, 'r') as f:
            for url in f:
                video_links.append(url.strip())
        return video_links
