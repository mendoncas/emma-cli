import click
import requests
import os
from pytube import YouTube
from . import page_content as pc


@click.command()
@click.argument("video_url")
def main(video_url):
    timestamps = pc.video_data(requests.get(video_url).text)
    yt = YouTube(video_url)
    yt.streams.filter(only_audio=True).first().download(
        output_path='./'+yt.title)
    os.rename('./'+yt.title+'/'+yt.title+'.mp4',
              './'+yt.title+'/'+yt.title+'.mp3')

    print('success i guess')

if __name__ == '__main__':
    main()
