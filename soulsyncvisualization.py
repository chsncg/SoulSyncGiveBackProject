import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# To set a webpage title, header and subtitle
st.set_page_config(page_title = "SoulSync",layout = 'wide')
st.header("SoulSync")
st.subheader("Connecting Through Music")

#read in the file
spotify_data = pd.read_csv("https://raw.githubusercontent.com/chsncg/SoulSyncGiveBackProject/main/spotify-2023.csv")
spotify_data.info()
spotify_data.duplicated()
spotify_data.count()

# Creating sidebar widget filters from Spotify dataset
track = spotify_data['track_name'].unique().tolist()
artist_name = spotify_data['artist(s)_name'].unique().tolist()
year_list = spotify_data['released_year'].unique().tolist()
month_list = spotify_data['released_month'].unique().tolist()
day_list = spotify_data['released_day'].unique().tolist()
streams_list = spotify_data['streams'].unique().tolist()
bpm_list = spotify_data['bpm'].unique().tolist()
playlists_list = spotify_data['in_spotify_playlists'].unique().tolist()
charts_list = spotify_data['in_spotify_charts'].unique().tolist()
danceability = spotify_data['danceability_%'].unique().tolist()
valence = spotify_data['valence_%'].unique().tolist()

# Add the filters. Every widget goes in here
with st.sidebar:
    st.write("Select song release year")
    #create a slider to hold user scores
    new_year_list = st.slider(label = "Choose a value:",
                                  min_value = 1990,
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
    artist = st.selectbox('Choose an option:', artist_name, 2)

    st.write("Select song")
    #create a selectbox option that holds all unique artists
    track_info = st.multiselect('Choose 1 or more options', track)

#Configure the slider widget for interactivity
year_info = (spotify_data['released_year'].between(*new_year_list))

#Configure the slider widget for interactivity
month_info = (spotify_data['released_month'].between(*new_month_list))

#Configure the selectbox and multiselect widget for interactivity
new_artist_year = (spotify_data['artist(s)_name'] == artist) & (spotify_data['released_year'].isin(year_info))

#Configure the chart data for interactivity
if track_info:
    chart_data = (spotify_data['artist(s)_name'] == artist) & (spotify_data['track_name'].isin(track_info))
else:
    # Handle the case when track_info is empty (e.g., no tracks selected)
    chart_data = spotify_data['artist(s)_name'] == artist

#VISUALIZATION SECTION
#group the columns needed for visualizations
col1, col2 = st.columns([2,3])
with col1:
    st.write("""#### List of Songs Filtered by Artist and Year """)
    dataframe_artist_year = spotify_data[new_artist_year].groupby(['track_name', 'artist(s)_name'])['released_year'].sum()
    dataframe_artist_year = dataframe_artist_year.reset_index()
    st.dataframe(dataframe_artist_year)

with col2:
    st.write("""#### Danceability vs Valence """)
    track_data = spotify_data[chart_data]
    fig = px.scatter(track_data, x="track_name", y=["danceability_%", "valence_%"], color_discrete_map={'danceability_%': 'purple', 'valence_%': 'blue'})
    fig.update_traces(marker_size = 15)
    st.plotly_chart(fig)

st.write("""#### Streams by Song """)
fig = px.bar(track_data, x="track_name", y="streams", color='track_name', height=550, width=1300)
st.plotly_chart(fig)

col1, col2 = st.columns([2,3])
    
with col1:
    st.write("""#### Spotify Charts Distribution""")
    fig_pie = px.pie(track_data, names='track_name', values='in_spotify_charts')
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig_pie)

with col2:
    st.write("""#### Spotify Playlists Distribution""")
    fig_pie = px.pie(track_data, names='track_name', values='in_spotify_playlists')
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig_pie)
