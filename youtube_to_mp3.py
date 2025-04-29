import os
import requests
from yt_dlp import YoutubeDL
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

def download_thumbnail(url, output_path):
    """Download the thumbnail image from the provided URL."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        return True
    return False

def embed_thumbnail(audio_path, thumbnail_path):
    """Embed the thumbnail as album art in the MP3 file."""
    try:
        audio = MP3(audio_path, ID3=ID3)
        audio.tags.add(
            APIC(
                encoding=3,  # UTF-8
                mime='image/jpeg',
                type=3,  # Cover (front)
                desc='Cover',
                data=open(thumbnail_path, 'rb').read()
            )
        )
        audio.save()
    except error as e:
        print(f"Error embedding thumbnail: {e}")

def convert_youtube_to_mp3(url, output_dir="output"):
    """Convert a YouTube video to MP3 with its thumbnail as album art using yt-dlp."""
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': True,
            'nocache': True,  # Disable caching to avoid permission issues
        }

        # Download and extract audio
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'video')
            # Get the actual MP3 filename from yt-dlp
            mp3_filename = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            mp3_path = mp3_filename
            thumbnail_url = info.get('thumbnail')

        # Download thumbnail
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
        thumbnail_path = os.path.join(output_dir, f"{safe_title}_thumb.jpg")
        if thumbnail_url and download_thumbnail(thumbnail_url, thumbnail_path):
            # Embed thumbnail as album art
            embed_thumbnail(mp3_path, thumbnail_path)
            # Clean up thumbnail file
            os.remove(thumbnail_path)

        print(f"MP3 saved at: {mp3_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    youtube_url = input("Enter YouTube URL: ")
    convert_youtube_to_mp3(youtube_url)