import streamlit as st
import pickle
import requests

# Function to load movie data and similarity scores
@st.cache_data
def load_data():
    movies = pickle.load(open("Models/movies_list.pkl", 'rb'))
    similarity = pickle.load(open("Models/similarity.pkl", 'rb'))
    return movies, similarity

# Function to fetch movie posters,
@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f99f126bfd58ba9b4aa8a3e6db301b6e&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

# Function to recommend movies based on the similarity scores
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Load movies and similarity data
movies, similarity = load_data()

# Streamlit UI
st.title("Movie Recommender System")

# Dynamic movie selection with autocomplete feature
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button("Show Recommendations"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Displaying recommendations in a more visually appealing manner
    cols = st.columns(5)
    for i, (movie_name, movie_poster) in enumerate(zip(recommended_movie_names, recommended_movie_posters)):
        with cols[i % 5]:
            st.image(movie_poster, caption=movie_name, use_column_width=True)

st.markdown("""
<style>
/* Custom CSS for improving the UI/UX of the Streamlit app */
.streamlit-container {
    margin-top: 20px;
}
.stButton>button {
    width: 100%;
    border-radius: 20px;
    border: 1px solid #4CAF50;
    background-color: #4CAF50;
    color: white;
    padding: 10px 24px;
    cursor: pointer;
    font-size: 18px;
}
.stButton>button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)
