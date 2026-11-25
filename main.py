"""Example usage for the Whisper transcriber.

Run:  python main.py path/to/voice.mp3
"""

import sys

from speech_text_app.transcriber import Transcriber


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python main.py <audio_file>")
    transcriber = Transcriber()
    print(transcriber.transcribe(sys.argv[1]))


if __name__ == "__main__":
    main()
