# How to Use

## Obtaining audio file
1. Get video download URL link from [savevideo.me](https://savevideo.me/us/)
2. Using the URL from savevideo.me, run in shell: `ffmpeg -i "$download url" -c copy input.mp4`
3. Convert to audio: `ffmpeg -i input.mp4 -q:a 0 -map a output.mp3`

## Obtaining transcriptions
1. Create `.env` in root folder (`touch .env`)
2. Add API keys: `ASSEMBLYAI_API_KEY` and/or `DEEPGRAM_API_KEY`. Google API key should be configured in your terminal with JSON.
3. Install necessary SDKs with pip
4. Run transcription Python files depending on which AI service you want to use.
