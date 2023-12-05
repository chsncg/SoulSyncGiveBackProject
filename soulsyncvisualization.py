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
year_list = spotify_data['released_year'].unique().tolist()
month_list = spotify_data['released_month'].unique().tolist()
day_list = spotify_data['released_day'].unique().tolist()
streams_list = spotify_data['streams'].unique().tolist()
bpm_list = spotify_data['bpm'].unique().tolist()
playlists_list = spotify_data['in_spotify_playlists'].unique().tolist()
charts_list = spotify_data['in_spotify_charts'].unique().tolist()
danceability = spotify_data['danceability_%'].unique().tolist()

# Add the filters. Every widget goes in here
with st.sidebar:
    st.write("Select song release year")
    #create a slider to hold user scores
    new_year_list = st.slider(label = "Choose a value:",
                                  min_value = 1940,
                                  max_value = 2023,
                                 value = (2022,2023))
    st.write("Select song release month")
    #create a slider to hold user scores
    new_month_list = st.slider(label = "Choose a value:",
                                  min_value = 1,
                                  max_value = 12,
                                  value = (1,12))


    st.write("Select artist")
    #create a multiselect option that holds genre
    artist = st.selectbox('Choose an option:', artist_name, 0)

    st.write("Select song")
    #create a selectbox option that holds all unique artists
    track = st.multiselect('Choose 1 or more options', track_name)

#Configure the slider widget for interactivity
year_info = (spotify_data['released_year'].between(*new_year_list))

#Configure the slider widget for interactivity
month_info = (spotify_data['released_month'].between(*new_month_list))
