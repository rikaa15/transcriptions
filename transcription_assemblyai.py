import os
from dotenv import load_dotenv
import assemblyai as aai

load_dotenv()

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")

def transcribe_audio_with_timestamps(audio_path):
    # Configure API Key
    aai.settings.api_key = ASSEMBLYAI_API_KEY

    # Initialize Transcriber
    transcriber = aai.Transcriber()

    # Transcribe the file (URL or local path)
    transcript = transcriber.transcribe(audio_path)

    # Check for errors
    if transcript.status == aai.TranscriptStatus.error:
        print("Transcription Error:", transcript.error)
        return

    # Process word-level timestamps
    output_file = f"transcription_assemblyai_{os.path.splitext(os.path.basename(audio_path))[0]}.txt"
    words_data = [
        f"{word.start/1000:.3f}-{word.end/1000:.3f}: {word.text}"
        for word in transcript.words
    ]

    # Save transcription with timestamps to a file
    with open(output_file, "w") as f:
        f.write("\n".join(words_data))

    print(f"Transcription saved to {output_file}")

# Example usage:
audio_file = "elon0_audio.mp3"  # Path to your audio file or URL

# Run transcription
transcribe_audio_with_timestamps(audio_file)
