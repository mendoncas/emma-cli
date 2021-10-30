import requests
import re


def get_video_description(url: str) -> list:
    description = re.findall(
        r'shortDescription":".+?","', requests.get(url).text)[0]

    return re.sub('","', '', description).split("\\n")
