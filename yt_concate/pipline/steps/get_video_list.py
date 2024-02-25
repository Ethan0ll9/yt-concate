from googleapiclient.discovery import build

from yt_concate.pipline.steps.step import Step
from yt_concate.settings import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs):
        channel_id = inputs["channel_id"]
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
        print(video_urls)
        return video_urls
