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


# Add the filters. Every widget goes in here
with st.sidebar:
    st.write("Select a range on the slider (it represents movie score) to view the total number of songs in a genre that falls within that range ")
    #create a slider to hold user scores
    new_score_rating = st.slider(label = "Choose a value:",
                                  min_value = 1.0,
                                  max_value = 10.0,
                                 value = (3.0,4.0))


    st.write("Select your preferred genre(s) and year to view the music released that year and in that genre")
    #create a multiselect option that holds genre
    new_genre_list = st.multiselect('Choose Genre:',
                                        genre_list, default = ['Animation', 'Horror', 'Fantasy', 'Romance'])

    #create a selectbox option that holds all unique years
    year = st.selectbox('Choose a Year', year_list, 0)

#Configure the slider widget for interactivity
score_info = (spotify_data['score'].between(*new_score_rating))



#Configure the selectbox and multiselect widget for interactivity
new_genre_year = (spotify_data['genre'].isin(new_genre_list)) & (spotify_data['year'] == year)


#VISUALIZATION SECTION
#group the columns needed for visualizations
col1, col2 = st.columns([2,3])
with col1:
    st.write("""#### Lists of movies filtered by year and Genre """)
    dataframe_genre_year = spotify_data[new_genre_year].groupby(['name', 'genre'])['year'].sum()
    dataframe_genre_year = dataframe_genre_year.reset_index()
    st.dataframe(dataframe_genre_year, width = 400)

with col2:
    st.write("""#### User score of movies and their genre """)
    rating_count_year = spotify_data[score_info].groupby('genre')['score'].count()
    rating_count_year = rating_count_year.reset_index()
    figpx = px.line(rating_count_year, x = 'genre', y = 'score')
    st.plotly_chart(figpx)




 # creating a bar graph with matplotlib
st.write("""
Average Movie Budget, Grouped by Genre
    """)
avg_budget = spotify_data.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

fig = plt.figure(figsize = (19, 10))

plt.bar(genre, avg_bud, color = 'maroon')
plt.xlabel('genre')
plt.ylabel('budget')
plt.title('Matplotlib Bar Chart Showing The Average Budget of Movies in Each Genre')
st.pyplot(fig)
