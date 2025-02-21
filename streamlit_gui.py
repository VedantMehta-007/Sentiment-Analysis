import streamlit as st
import pandas as pd

# Load the structured DataFrame from CSV (or use the DataFrame directly)
df = pd.read_csv('youtube_sentiment_results.csv')

# Set page title
st.title('YouTube Sentiment Analysis')

# Show data table
st.write('### Sentiment Analysis Results')
st.dataframe(df)

# Filter results by sentiment type
sentiment_filter = st.selectbox('Filter by Sentiment', ['All', 'Positive', 'Neutral', 'Negative'])

if sentiment_filter != 'All':
    df = df[df['Sentiment'] == sentiment_filter]

# Display filtered results
st.write(f"### Showing {sentiment_filter} comments")
st.dataframe(df)

# Plotting sentiment distribution (optional)
st.write('### Sentiment Distribution')
st.bar_chart(df['Sentiment'].value_counts())
