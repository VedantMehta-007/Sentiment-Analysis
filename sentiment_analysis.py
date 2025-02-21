from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_analysis(comments):
    analyzer = SentimentIntensityAnalyzer()  # Initialize the sentiment analyzer
    analysis_results = []
    
    for comment in comments:
        sentiment_score = analyzer.polarity_scores(comment)  # Get sentiment scores
        compound_score = sentiment_score['compound']  # Extract compound score

        # Classify sentiment based on the compound score
        if compound_score >= 0.05:
            sentiment = 'Positive'
        elif compound_score <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        # Store result as a dictionary
        analysis_results.append({
            'comment': comment,
            'sentiment': sentiment,
            'score': round(compound_score, 2)  # Round score to 2 decimal places
        })
    
    return analysis_results
