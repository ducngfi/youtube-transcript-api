from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_transcript(video_url):
    # Extract video ID from the URL
    video_id = video_url.split("v=")[1]
    
    try:
        # Retrieve the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format the transcript as plain text
        formatter = TextFormatter()
        formatted_transcript = formatter.format_transcript(transcript)
        
        return formatted_transcript
    except Exception as e:
        return f"An error occurred: {str(e)}"

# URL of the YouTube video
video_url = "https://www.youtube.com/watch?v=8hcxnuaXDF0"

# Get the transcript
transcript = get_transcript(video_url)

# Check if an error occurred
if transcript.startswith("An error occurred"):
    print(transcript)
else:
    # Save the transcript to a file
    with open('transcript.txt', 'w', encoding='utf-8') as f:
        f.write(transcript)
    print("Transcript has been saved to transcript.txt")
