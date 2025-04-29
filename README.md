# YouTube to MP3 Converter (Now with Thumbnail Embedding)
Have you ever found a very awesome YouTube music video, or for better, a wonderfull video mix that you'll want to downlaod (If legal) and wondered how you could download it to play it later offline?

- That was the Genesis of this hobby project. You only need internet connetivity then run it locally in your Terminal.
- You'll be promted to paste the YouTube link then it automatically downlaods it.
- This is a Work In Progress and an online Web version of this will be available where your just paste your YouTube link and click Convert/Download effortlessly.

A Python script that converts YouTube (Of unlimited length) videos to MP3 audio files and embeds the video's thumbnail as album art.

## Installation

Clone this repository:

```bash
$ git clone https://github.com/okomojacob/YouTube2mp3.git
```

Navigate to the project directory:
```bash
$ cd YouTube2mp3
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

- [x] macOS: `brew install ffmpeg`
- [x] Linux: `sudo apt install ffmpeg`
- [x] Windows: `Use Chocolatey (choco install ffmpeg) or download from FFmpeg.`

## Usage

Run the script from your terminal/ command line:

```bash
$ python youtube_to_mp3.py
```

Enter the YouTube URL when prompted (e.g., https://www.youtube.com/watch?v=RD7GkOSs2ww&list=PLHXrlST7W5bSlzQq8hSQ9FEm5K9KH6KeI).
The script will download the audio, convert it to MP3, embed the thumbnail as album art, and save it in the `output` directory.

## Prerequisites

- [x] Python 3.6 or higher
- [x] ffmpeg (for audio conversion)

## 👨🏼‍⚖ Legal Note ⚖️
- [x] Please ensure you have the necessary rights to download and convert YouTube videos. 
- [x] This script is for educational purposes only and should be used in compliance with [YouTube’s Terms of Service](https://www.youtube.com/t/terms) and applicable copyright laws.

## License
This project is licensed under the MIT License.
Contact
For questions or feedback, reach out via GitHub Issues or contact me at @okomojacob.
