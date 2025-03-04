"""Transcribes an MP3 audio file into a text file using Whisper."""

import whisper
import os

# Define paths
audio_input_dir = os.path.expanduser("~/mckim_creed/projects/meeting_minutes/voice_input/")
audio_output_dir = os.path.expanduser("~/mckim_creed/projects/meeting_minutes/input/")
transcript_file = os.path.join(audio_output_dir, "meeting_transcript.txt")

# Ensure output directory exists
os.makedirs(audio_output_dir, exist_ok=True)

# Find the latest .mp3 file in voice_input
mp3_files = sorted(
    [f for f in os.listdir(audio_input_dir) if f.endswith(".mp3")],
    key=lambda x: os.path.getmtime(os.path.join(audio_input_dir, x)), 
    reverse=True  # Sort by newest first
)

if not mp3_files:
    raise FileNotFoundError("No .mp3 files found in voice_input directory.")

latest_mp3 = os.path.join(audio_input_dir, mp3_files[0])  # Get the latest MP3 file

# Load Whisper model and transcribe
print(f"Transcribing: {latest_mp3}")
try:
    model = whisper.load_model("base")  # Options: "tiny", "base", "small", "medium", "large"
    result = model.transcribe(latest_mp3)

    # Save transcript
    with open(transcript_file, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"✅ Transcription completed. Saved as: {transcript_file}")

except Exception as e:
    print(f"❌ Error during transcription: {e}")
