import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# To set a webpage title, header and subtitle
st.set_page_config(page_title = "Spotify analysis",layout = 'wide')
st.header("SoulSync")
st.subheader("Interact with this dashboard using the widgets on the sidebar!")

#read in the file
spotify_data = pd.read_csv("https://raw.githubusercontent.com/chsncg/SoulSyncGiveBackProject/main/spotify-2023.csv")
spotify_data.info()
spotify_data.duplicated()
spotify_data.count()
spotify_data.dropna()

# Creating sidebar widget filters from Spotify dataset
track_name = spotify_data['track_name'].unique().tolist()
artist_name = spotify_data['artist(s)_name'].unique().tolist()
year = spotify_data['released_year'].unique().tolist()
month = spotify_data['released_month'].unique().tolist()
day = spotify_data['released_day'].unique().tolist()
streams = spotify_data['streams'].unique().tolist()
bpm = spotify_data['bpm'].unique().tolist()
playlists = spotify_data['in_spotify_playlists'].unique().tolist()
charts = spotify_data['in_spotify_charts'].unique().tolist()
danceability = spotify_data['danceability_%'].unique().tolist()
