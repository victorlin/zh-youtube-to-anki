import json
from typing import NamedTuple
import urllib.request


class VideoInfo(NamedTuple):
    title: str
    author: str


def get_info(video_id):
    params = {
        "format": "json",
        "url": f"https://www.youtube.com/watch?v={video_id}",
    }
    query_string = urllib.parse.urlencode(params)
    url = f"https://www.youtube.com/oembed?{query_string}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    return VideoInfo(
        title = data['title'],
        author = data['author_name'],
    )
