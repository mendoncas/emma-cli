from typing import Dict
import re


def get_timestamps(description: list) -> dict:
    timestamps: Dict[str, str] = {}
    expression = r'[0-9]*[0-9]+:[0-9]+[0-9]:*[0-9]*[0-9]*'
    for line in description:
        r = re.findall(expression, line)

        if r:
            timestamps.update({r[0]: (re.sub(expression, "", line))})

    return timestamps
