import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

DOWNLOADS_DIR = 'downloads_dir'
VIDEOS_DIR = 'downloads_dir/videos_dir'
CAPTIONS_DIR = 'downloads_dir/captions_dir'
