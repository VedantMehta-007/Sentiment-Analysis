from flask import Flask, render_template, request
from youtube_comments import get_youtube_comments  # Importing the function from youtube_comments.py
import re

app = Flask(__name__)

# Home route to handle form submission and YouTube comments processing
@app.route('/', methods=['GET', 'POST'])
def home():
    video_url = request.form.get('video_url', '')  # Extract the video URL entered in the form
    error = None
    tables = None

    if video_url:
        # Extract the video ID from the URL
        video_id = extract_video_id(video_url)
        
        if video_id:
            try:
                comments = get_youtube_comments(video_id)  # Fetch comments from YouTube using the video ID
                tables = sentiment_analysis(comments)  # Analyze the sentiment of the comments
            except Exception as e:
                error = f"An error occurred: {str(e)}"
        else:
            error = "Please enter a valid YouTube URL."
    
    return render_template('index.html', error=error, tables=tables)

# Function to extract the video ID from a YouTube URL
def extract_video_id(url):
    youtube_regex = r"(?:https?:\/\/(?:www\.)?youtube\.com\/(?:v\/|e\/|.*[?&]v=)|https?:\/\/(?:www\.)?youtu\.be\/)([a-zA-Z0-9_-]+)"
    match = re.match(youtube_regex, url)
    return match.group(1) if match else None

# Sentiment analysis function (This is a simple placeholder)
def sentiment_analysis(comments):
    # Here you can use any sentiment analysis library, for example TextBlob or Vader.
    # For now, let's just return the comments as is.
    analysis_results = []
    for comment in comments:
        # A simple mock-up sentiment result (replace with actual sentiment analysis)
        analysis_results.append({'comment': comment, 'sentiment': 'Positive'})  # Example sentiment
    return analysis_results

if __name__ == "__main__":
    app.run(debug=True)
