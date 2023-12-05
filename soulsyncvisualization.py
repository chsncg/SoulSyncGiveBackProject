import time
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_url = "https://gist.githubusercontent.com/rioto9858/ff72b72b3bf5754d29dd1ebf898fc893/raw/1164a139a780b0826faef36c865da65f2d3573e0/top50MusicFrom2010-2019.csv"

# read csv from a URL
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

# dashboard title
st.title("Spotify Dashboard 2010-19")

# Print out the top artist
top_artist = df['artist'].value_counts().idxmax()
st.write(f"Top Artist: {top_artist}")

# Add an image next to the top artist information
image_url = "https://people.com/thmb/fs95OUVphm331bzezgDbmeRqGHc=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(674x309:676x311):format(webp)/Katy-Perry-Ginger-Instagram-01-121622-ca18a1ece0874f18bb7153a46873d428.jpg"
st.image(image_url, caption='Top Artist Image', width=200)


# Create a scatter plot for song durations in different years
fig = px.scatter(df, x='year', y='Length - The duration of the song', color='year', 
                 title='Song Durations Over the Years',
                 labels={'Length - The duration of the song': 'Song Duration (s)', 'year': 'Year'})
st.plotly_chart(fig)

# Print out the top genre
top_genre = df['the genre of the track'].value_counts().idxmax()
st.write(f"Top Genre: {top_genre}")

# Create a pie chart for different genres of songs released in the year 2010
data_2019 = df[df['year'] == 2019]
fig = px.pie(data_2019, names='the genre of the track', title='Distribution of Genres in 2019')
st.plotly_chart(fig)

# Create a trend chart for the popularity of songs for each artist
fig = px.line(df, x='year', y='Popularity- The higher the value the more popular the song is', color='artist', 
              title='Artist Popularity Trend Over the Years',
              labels={'year': 'Year', 'Popularity- The higher the value the more popular the song is': 'Artist Popularity'})
st.plotly_chart(fig)

# Create a point line graph for the number of songs produced by Katy Perry each year
katy_perry_data = df[df['artist'] == 'Katy Perry']
fig = px.line(katy_perry_data, x='year', y='Popularity- The higher the value the more popular the song is', title='Popularity by Katy Perry Each Year',
              labels={'year': 'Year', 'Popularity- The higher the value the more popular the song is': 'Popularity'})
fig.update_traces(mode='markers+lines')
st.plotly_chart(fig)
