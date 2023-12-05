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
year_list = spotify_data['released_year'].unique().tolist()
score_rating = spotify_data['score'].unique().tolist()
genre_list = spotify_data['genre'].unique().tolist()
