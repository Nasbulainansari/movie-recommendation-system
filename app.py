import streamlit as st
import pickle
import requests
from recommend import recommend

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# ---------- Load Movie Data ----------
movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies_list = movies_dict['title'].values

# ---------- Add Custom CSS ----------
st.markdown("""
    <style>
    /* your responsive CSS here */
    </style>
""", unsafe_allow_html=True)

# ---------- Main App ----------
st.title("🎥 Movie Recommendation System")

selected_movie = st.selectbox('🎬 Select a movie:', movies_list)

if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    cols = st.columns(5)
    for idx, (name, poster) in enumerate(zip(recommended_movie_names, recommended_movie_posters)):
        with cols[idx % 5]:
            st.markdown(f"""
                <div class="movie-card">
                    <img src="{poster}" alt="{name}">
                    <p class="movie-title">{name}</p>
                </div>
            """, unsafe_allow_html=True)
