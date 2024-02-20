from googleapiclient.discovery import build
from yt_concate.settings import API_KEY

# Change the channel id here
CHANNEL_ID = 'UCX6OQ3DkcsbYNE6H8uQQuVA'


def get_all_video_list(channel_id):
    api_key = API_KEY
    youtube = build(
        'youtube',
        'v3',
        developerKey=api_key
    )

    # Make a request to youtube api
    request = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    )

    # get a response for api
    response = request.execute()

    # Retrieve the uploads playlist ID for the given channel
    playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Retrieve all videos from uploads playlist
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

    # Extract video URLs
    video_urls = []

    for video in videos:
        video_id = video['snippet']['resourceId']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_urls.append(video_url)

    return video_urls


video_list = get_all_video_list(CHANNEL_ID)
print(len(video_list))