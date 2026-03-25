import streamlit as st
import pandas as pd
import requests

import streamlit as st
import pickle
import pandas as pd

# 1. Load the Pre-trained Model
@st.cache_resource # This ensures model loads only ONCE (Performance boost!)
def load_trained_model():
    with open('./notebooks/movie_recommender.pkl', 'rb') as f:
        return pickle.load(f)

model_data = load_trained_model()
df_pivot = model_data['pivot_table']
preds_df = model_data['predictions']
movie_titles = model_data['movie_titles']

# 2. Recommendation Logic Function
def get_recommendations(user_id, num_recs=5):
    # Find user row index
    user_idx = df_pivot.index.get_loc(user_id)
    # Get high-rated predictions for this user
    user_preds = preds_df.iloc[user_idx].sort_values(ascending=False)
    # Join with titles and return top 5
    return user_preds.head(num_recs).index.tolist()

# --- Rest of your UI and TMDB Poster code here ---

# 1. Page Config & Style
st.set_page_config(page_title="Netflix Pro", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #141414; color: white; }
    div.stButton > button:first-child { background-color: #E50914; color: white; border: none; }
    h1, h2, h3 { color: #E50914; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    </style>
    """, unsafe_allow_html=True)

API_KEY = "8265bd1679663a7ea12ac168da84d2e8" # Replace with your Key

# 2. TMDB Helper Functions
def get_movie_details(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    res = requests.get(url).json()
    if res['results']:
        movie = res['results'][0]
        return movie['id'], "https://image.tmdb.org/t/p/w500/" + movie['poster_path']
    return None, None

def get_recommendations(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}"
    res = requests.get(url).json()
    return res['results'][:5] # Top 5 dynamic recs

def get_trending():
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}"
    return requests.get(url).json()['results'][:5]

def get_by_genre(genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}&sort_by=popularity.desc"
    return requests.get(url).json()['results'][:5]


# OLD (Thappu):
# path = r"C:\Users\saira\Projects\Netflix-recommendation-engine\data\movie_titles _1_.csv"

# NEW (Correct):
@st.cache_data
def load_data():
    # Direct ga GitHub folder structure ni follow avvu
    path = "data/movie_titles _1_.csv" 
    return pd.read_csv(path, encoding="latin1", header=None, names=['Movie_Id', 'Year', 'Name'], on_bad_lines='skip', engine='python')


movie_titles = load_data()

# 4. Main UI
st.title("🎬 Netflix Smart Dashboard")
selected_movie = st.selectbox("Search Movie:", movie_titles['Name'].values)

if st.button('Analyze & Recommend'):
    m_id, m_poster = get_movie_details(selected_movie)
    if m_id:
        st.image(m_poster, width=200)
        st.subheader(f"Because you liked {selected_movie}...")
        
        recs = get_recommendations(m_id)
        cols = st.columns(5)
        for i, movie in enumerate(recs):
            with cols[i]:
                path = "https://image.tmdb.org/t/p/w500/" + movie['poster_path'] if movie['poster_path'] else ""
                st.image(path)
                st.caption(movie['title'])

# 5. Genres & Trending (Always Visible)
st.markdown("---")
st.header("🔥 Trending This Week")
t_cols = st.columns(5)
for i, m in enumerate(get_trending()):
    with t_cols[i]:
        st.image("https://image.tmdb.org/t/p/w500/" + m['poster_path'])
        st.caption(m['title'])

st.header("🚀 Best in Sci-Fi")
s_cols = st.columns(5)
for i, m in enumerate(get_by_genre(878)): # 878 is Sci-Fi
    with s_cols[i]:
        st.image("https://image.tmdb.org/t/p/w500/" + m['poster_path'])
        st.caption(m['title'])

st.header("😂 Top Comedy Hits")
c_cols = st.columns(5)
for i, m in enumerate(get_by_genre(35)): # 35 is Comedy
    with c_cols[i]:
        st.image("https://image.tmdb.org/t/p/w500/" + m['poster_path'])
        st.caption(m['title'])