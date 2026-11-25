# Whisper Speech Transcriber

Turns spoken audio into text with OpenAI's Whisper speech-recognition model.

## What it does

`speech_text_app.py` defines `Transcriber`, which loads the Whisper `base` model and
transcribes an audio file.

```python
from speech_text_app import Transcriber

transcriber = Transcriber()
print(transcriber.transcribe("voice.mp3"))
```

## Requirements

- Python 3.9+
- `openai-whisper` (see `requirements.txt`)
- `ffmpeg` on the `PATH` — required by Whisper for audio decoding

```bash
python -m pip install -r requirements.txt
```

The model weights (about 150 MB for `base`) download on first use.

## Notes and limitations

- Whisper `base` favours speed over accuracy; use `small` or `medium` for noisy recordings.
- The whole file is transcribed in one pass, so very long audio is memory hungry.
- No speaker diarisation and no timestamps are returned by this wrapper.

## Status

Single-module prototype. Planned work: a command-line entry point and timestamped output.

## License

No license file is present yet. Until one is added, the default copyright applies.
