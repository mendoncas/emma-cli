from time import time
from typing import Dict
from pydub import AudioSegment
import os


def extract_segments(file: str, timestamps: Dict, title: str):
    timestamps = list(timestamps.items())
    # files_path = title
    try:
        os.mkdir(title)
    except FileExistsError:
        print('folder already exists')

    for i in range(len(timestamps)):
        song_name = f'{timestamps[i][1]}.mp3'
        stamp = timestamps[i][0].split(':')
        song = AudioSegment.from_file(file)

        startMin = int(stamp[0])
        startSec = int(stamp[1])

        startTime = startMin*60*1000+startSec*1000

        try:
            stamp = timestamps[i+1][0].split(':')

            endMin = int(stamp[0])
            endSec = int(stamp[1])
            endTime = endMin*60*1000+endSec*1000
            extract = song[startTime:endTime]

        except IndexError:
            extract = song[startTime:]

        extract.export(song_name, format="mp3")
