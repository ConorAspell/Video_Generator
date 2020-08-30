  
from datetime import datetime
import requests
import json
import time
import os

def get_videos():
    number_of_videos = os.environ.get("number_of_videos")
    mode = os.environ.get("mode")
    key = os.environ.get("key")
    period = os.environ.get("period")
    twitch_id = os.environ.get("twitch_id")
    # number_of_videos = 2
    # mode = "game"
    # key = "chess"
    # twitch_id = "022i90v7stu8i3u71otlf5xxa6w8si"
    url="https://api.twitch.tv/kraken/clips/top?limit="+str(number_of_videos)+"&"+mode+"="+key+"&period="+str(period)
    referrer = "google.ie"
    client_id = twitch_id
    headers = {
        'Client-ID' : client_id,    
        'Accept': 'application/vnd.twitchtv.v5+json'
    }
    response = requests.get(url, headers=headers, timeout=10)
    clips=[]    
    places=[]   
    response_dict = json.loads(response.content)
    print(response_dict)
    today = datetime.now().strftime("%d_%m_%Y")
    save_location = "top_clips_" + today
    duration = 0
    for item in response_dict['clips']:
        duration += item['duration']
        if duration > 125:
            break
        temp = item['thumbnails']['medium']
        temp2='-'.join(temp.split('-')[:-2])+".mp4"
        clips.append(temp2)
    for clip in clips:
        r=requests.get(clip)
        key=clip.split('/')[-1]
        place='/tmp/'+key
        with open(place, 'wb') as f:
            f.write(r.content)
        places.append(place)
    return places