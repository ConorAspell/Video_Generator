from get_videos import get_videos
from edit_videos import edit_video
from upload_video import upload_to_reddit, upload_to_streamable

if __name__ == "__main__":
    places = get_videos()
    saves = edit_video(places)
    url = upload_to_streamable(saves)
    upload_to_reddit(url)