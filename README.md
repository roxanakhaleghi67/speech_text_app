# Whisper Speech Transcriber

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python](https://img.shields.io/badge/python-3.8%2B-blue)

Convert spoken audio into text using OpenAI's Whisper model.

## Features

- Transcribes an audio file to plain text
- Uses the Whisper `base` model by default
- Handles common audio formats supported by Whisper (for example, `.mp3`, `.wav`)
- Minimal, class-based API (`Transcriber`)

## Requirements

- Python 3.8 or newer
- `openai-whisper`
- PyTorch (`torch`) as the backend
- `ffmpeg` installed and available on your system `PATH` (required by Whisper to decode audio)

## Installation

```bash
pip install -r requirements.txt
```

Make sure `ffmpeg` is installed separately, for example:

```bash
# Debian/Ubuntu
sudo apt-get install ffmpeg

# macOS (Homebrew)
brew install ffmpeg
```

## Usage

```python
from speech_text_app import Transcriber

transcriber = Transcriber()
print(transcriber.transcribe("voice.mp3"))
```

The first call downloads the Whisper `base` model, so it may take a moment.

## Project Structure

```text
speech_text_app/
├── speech_text_app.py   # Transcriber implementation
├── requirements.txt
└── README.md
```

## License

This project is released under the **MIT License**.

## Author

**Roxana Khaleghi**
