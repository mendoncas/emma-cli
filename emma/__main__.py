import sys
from .get_timestamps import get_timestamps
from .get_video_description import get_video_description


def main():
    print(get_timestamps(get_video_description(
        sys.argv[1])))


if __name__ == '__main__':
    main()
