import click
import requests
from youtube_dl import YoutubeDL
from . import page_content as pc
from . import audio as ad

# todo:
# save on Musics directory by default
# allow user to set download path
# save mp3 with album, artist info and thumbnail
# crop audio with timestamps


@click.command()
@click.argument("video_url")
def main(video_url):
    timestamps = pc.timestamps(requests.get(video_url).text)

    yt = YoutubeDL({'format': 'bestaudio/best'})

    title = yt.extract_info(video_url, download=False)['title']

    # yt = YoutubeDL({'format': 'bestaudio/best',
    #                 'outtmpl': f'{title}.mp3',
    #                 'postprocessors': [{
    #                     'key': 'FFmpegExtractAudio',
    #                     'preferredcodec': 'mp3'
    #                 }]})

    # yt.extract_info(video_url)

    print('finished downloading audio... cropping...')

    ad.extract_segments(f'{title}.mp3', timestamps, title)


if __name__ == '__main__':
    main()
