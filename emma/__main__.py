import click
import requests
from . import page_content as pc


@click.command()
@click.argument("video_url")
def main(video_url):
    print(pc.video_data(requests.get(video_url).text))


if __name__ == '__main__':
    main()
