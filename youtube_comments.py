import googleapiclient.discovery
import googleapiclient.errors

# Define the function to get YouTube comments
def get_youtube_comments(video_id):
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey="AIzaSyBVHRy3rb0ZZmVwbgevfhE-FEJbPjIQt8Y")
    
    # Request to fetch comments
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )
    response = request.execute()
    
    comments = []
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
        comments.append(comment)
    
    return comments
