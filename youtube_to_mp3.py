import os
import shutil
import sys

import requests
from mutagen.id3 import ID3, APIC, ID3NoHeaderError
from mutagen.mp3 import MP3
from yt_dlp import YoutubeDL


def download_thumbnail(url, output_path):
    """Download the thumbnail image from the provided URL."""
    try:
        response = requests.get(url, timeout=30)
    except requests.RequestException as e:
        print(f"Error downloading thumbnail: {e}")
        return False
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        return True
    return False


def embed_thumbnail(audio_path, thumbnail_path):
    """Embed the thumbnail as album art in the MP3 file."""
    try:
        try:
            audio = MP3(audio_path, ID3=ID3)
        except ID3NoHeaderError:
            audio = MP3(audio_path)
            audio.add_tags()
        if audio.tags is None:
            audio.add_tags()

        with open(thumbnail_path, 'rb') as img:
            audio.tags.add(
                APIC(
                    encoding=3,      # UTF-8
                    mime='image/jpeg',
                    type=3,          # Cover (front)
                    desc='Cover',
                    data=img.read(),
                )
            )
        audio.save()
    except Exception as e:
        print(f"Error embedding thumbnail: {e}")


def convert_youtube_to_mp3(url, output_dir="output"):
    """Convert a YouTube video to MP3 with its thumbnail as album art using yt-dlp."""
    if shutil.which('ffmpeg') is None:
        print("ffmpeg not found on PATH. Install it first (macOS: brew install ffmpeg).")
        return None

    try:
        os.makedirs(output_dir, exist_ok=True)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': True,
            'cachedir': False,  # Disable caching to avoid permission issues
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'video')
            thumbnail_url = info.get('thumbnail')

            # Prefer the real post-processed path; fall back to swapping the extension.
            mp3_path = None
            for entry in info.get('requested_downloads') or []:
                mp3_path = entry.get('filepath')
                if mp3_path:
                    break
            if not mp3_path:
                mp3_path = os.path.splitext(ydl.prepare_filename(info))[0] + '.mp3'

        if not os.path.exists(mp3_path):
            print(f"Expected MP3 not found at: {mp3_path}")
            return None

        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
        thumbnail_path = os.path.join(output_dir, f"{safe_title}_thumb.jpg")
        if thumbnail_url and download_thumbnail(thumbnail_url, thumbnail_path):
            embed_thumbnail(mp3_path, thumbnail_path)
            os.remove(thumbnail_path)

        print(f"MP3 saved at: {mp3_path}")
        return mp3_path

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    youtube_url = sys.argv[1] if len(sys.argv) > 1 else input("Enter YouTube URL: ")
    convert_youtube_to_mp3(youtube_url)
