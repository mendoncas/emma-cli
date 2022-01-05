import re
from bs4 import BeautifulSoup
from typing import Dict


def timestamps(content: str) -> dict:
    return get_timestamps(get_description(content))


def get_title(content: str) -> str:
    return re.sub(' - YouTube', '',
                  BeautifulSoup(content, 'html.parser').title.text)


def get_description(content: str) -> list:
    description = re.findall(
        r'shortDescription":".+?","', content)[0]

    return re.sub('","', '', description).split("\\n")


def get_timestamps(description: list) -> dict:
    timestamps: Dict[str, str] = {}
    expression = r'[0-9]*[0-9]+:[0-9]+[0-9]:*[0-9]*[0-9]*'
    for line in description:
        r = re.findall(expression, line)
        if r:
            timestamps.update({r[0]: (re.sub(expression, "", line))})

    return timestamps
