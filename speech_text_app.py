# speech_text_app/transcriber.py
import whisper

class Transcriber:
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        return result["text"]

# speech_text_app/README.md
"""
# Whisper Speech Transcriber

Convert spoken audio into text using OpenAI's Whisper model.

## Example:
```python
t = Transcriber()
print(t.transcribe("voice.mp3"))
```
"""