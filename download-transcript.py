#!/usr/bin/env python3
import argparse
from pathlib import Path
import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

from src.youtube import get_info


def get_video_id(url):
    query = urlparse(url).query
    return parse_qs(query)["v"][0]


def get_transcript(video_id, languages=('en', 'zh-TW', 'zh')):
    return YouTubeTranscriptApi.get_transcript(video_id, languages=languages)


def get_output_filepath(video_id, out_dir):
    info = get_info(video_id)
    filename = slugify(f"{info.title}-{info.author}")
    return Path(out_dir) / f"{filename}.txt"


def slugify(name):
    name = re.sub(r'[^\w\s-]', '_', name.lower())
    name = re.sub(r'[-\s]+', '-', name).strip('-_')
    return name


def write_transcript(transcript, filepath):
    with open(filepath, 'w') as f:
        for line in transcript:
            f.write(line["text"] + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url")
    parser.add_argument("--out-dir")
    parser.parse_args()
    args = parser.parse_args()

    video_id = get_video_id(args.url)
    transcript = get_transcript(video_id)
    filepath = get_output_filepath(video_id, args.out_dir)
    write_transcript(transcript, filepath)
    print(f"Transcript written to file: {filepath}")
