FROM python:3
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY get_videos.py /code/get_videos.py
COPY edit_videos.py /code/edit_videos.py
COPY upload_video.py /code/upload_video.py


COPY main.py /code/main.py


WORKDIR /code/

ENV number_of_videos ""
ENV key ""
ENV mode ""
ENV period ""
ENV twitch_id ""
ENV username ""
ENV password ""
ENV subreddit ""
ENV reddit_id ""
ENV reddit_secret ""


COPY env.list /code/env.list
CMD  "python main.py"
