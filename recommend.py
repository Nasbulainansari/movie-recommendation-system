import requests
import pickle
import pandas as pd

# ------------------ LOAD DATA ------------------
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


# ------------------ FETCH POSTER FUNCTION ------------------
def fetch_poster(movie_name):
    """
    Fetch movie poster from TMDb API.
    Make sure you replace YOUR_REAL_API_KEY with your own key.
    """
    url = f"https://api.themoviedb.org/3/search/movie?api_key=abc123xyz&query={movie_name}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        # 👇 Debugging: print to terminal
        print(f"DEBUG {movie_name}:", data)

        if "results" in data and len(data["results"]) > 0:
            poster_path = data["results"][0].get("poster_path")
            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path

        # 🟡 Fallback image (in case poster not found)
        return "https://via.placeholder.com/500x750?text=No+Image+Available"

    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching poster for {movie_name}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image+Available"


# ------------------ RECOMMEND FUNCTION ------------------
def recommend(movie):
    """
    Returns top 5 similar movies and their posters.
    """
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_name = movies.iloc[i[0]].title
        recommended_movie_names.append(movie_name)
        poster = fetch_poster(movie_name)
        recommended_movie_posters.append(poster)

    return recommended_movie_names, recommended_movie_posters
