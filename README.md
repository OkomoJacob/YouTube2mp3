# YouTube to MP3 Converter with Thumbnail Embedding
Have you ever found a very awesome YouTube video, or for better a wonderfull video mix that you'll want to downlaod (If legal) and wondered how you could download it?

That's was the Genesis of this project. You only need internet connetivity then run it, You'll be promted to paste the YouTube link then it automatically downlaods it.

A Python script that converts YouTube (Of unlimited length) videos to MP3 audio files and embeds the video's thumbnail as album art.

## Installation

Clone this repository:

```bash
$ git clone https://github.com/okomojacob/youtube-to-mp3.git
```

Navigate to the project directory:
```bash
$ cd youtube-to-mp3
```

Create and activate virtual environment (optional but recommended):
```bash
$ python -m venv venv
```

# On macOS/Linux
```bash
$ source venv/bin/activate
```

# On Windows: 
```bash
$ venv\Scripts\activate
```

Install the required dependencies:
```shell
pip install -r requirements.txt
```

Note: Ensure you have ffmpeg installed on your system, as it’s required for audio conversion. Install it via:

macOS: `brew install ffmpeg`
Linux: `sudo apt install ffmpeg`
Windows: `Use Chocolatey (choco install ffmpeg) or download from FFmpeg.`

## Usage

Run the script from your terminal/ command line:

```bash
$ python youtube_to_mp3.py
```

Enter the YouTube URL when prompted (e.g., https://www.youtube.com/watch?v=RD7GkOSs2ww&list=PLHXrlST7W5bSlzQq8hSQ9FEm5K9KH6KeI).
The script will download the audio, convert it to MP3, embed the thumbnail as album art, and save it in the `output` directory.

## Prerequisites

[ x ] Python 3.6 or higher
[ x ] ffmpeg (for audio conversion)

## 👨🏼‍⚖ Legal Note ⚖️
[ x ] Please ensure you have the necessary rights to download and convert YouTube videos. 
[ x ] This script is for educational purposes only and should be used in compliance with [YouTube’s Terms of Service](https://www.youtube.com/t/terms) and applicable copyright laws.

## License
This project is licensed under the MIT License.
Contact
For questions or feedback, reach out via GitHub Issues or contact me at @okomojacob.
