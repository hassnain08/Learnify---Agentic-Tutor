from crewai.tools import BaseTool  # Required base class for CrewAI tools
from typing import Type
from pydantic import BaseModel, Field  # For input validation and schema
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


class YoutubeTranscriptInput(BaseModel):
    """Input schema for YouTube Transcript Tool."""
    url: str = Field(..., description="Full YouTube video URL (e.g., https://www.youtube.com/watch?v=abc123)")


class YoutubeTranscriptTool(BaseTool):
    """Tool to fetch and chunk transcript from YouTube videos using youtube-transcript-api."""
    
    name: str = "youtube_transcript_tool"
    description: str = (
        "Fetch and chunk transcript text from a YouTube video. Returns timestamped sections for downstream summarization."
    )
    args_schema: Type[BaseModel] = YoutubeTranscriptInput

    def _extract_video_id(self, url: str) -> str:
        """Extracts the video ID from a YouTube URL."""
        parsed_url = urlparse(url)
        if 'youtu.be' in parsed_url.netloc:
            return parsed_url.path.lstrip('/')
        elif 'youtube' in parsed_url.netloc:
            return parse_qs(parsed_url.query).get("v", [None])[0]
        return None

    def _run(self, url: str) -> list[str] | str:
        """Main method that fetches and chunks transcript."""
        video_id = self._extract_video_id(url)
        if not video_id:
            return "❌ Invalid YouTube URL. Make sure it's in correct format."

        try:
            # Get transcript from YouTube
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
        except Exception as e:
            return f"❌ Failed to fetch transcript: {str(e)}"

        # Process and chunk transcript (approx 700-word limit)
        chunks, chunk_text, token_count, start_time = [], "", 0, 0
        token_limit = 700

        for entry in transcript:
            words = entry["text"].split()
            token_count += len(words)
            chunk_text += entry["text"] + " "

            if token_count > token_limit:
                chunks.append(f"🕒 Start: {start_time:.2f}s\n{chunk_text.strip()}")
                chunk_text = ""
                token_count = 0
                start_time = entry["start"]

        if chunk_text.strip():
            chunks.append(f"🕒 Start: {start_time:.2f}s\n{chunk_text.strip()}")

        return chunks
