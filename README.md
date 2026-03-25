# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Movie%20Camera.png" alt="Movie Camera" width="40" /> Netflix Recommendation System
[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://netflix-recommendation-system-68.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

> **A high-performance AI dashboard predicting cinematic preferences using Matrix Factorization and TMDB real-time metadata.**

---

### 🛠️ Technical Architecture
<p align="left">
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=flat-square&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=flat-square&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/TMDB_API-01d277?style=flat-square&logo=the-movie-database&logoColor=white" />
</p>

---

### 🚀 Core Functionalities
* **Vectorized Search:** Leverages **Singular Value Decomposition (SVD)** for latent factor analysis.
* **Metadata Injection:** Fetches dynamic assets via **TMDB API v3**.
* **Global Trends:** Real-time data pipeline for weekly trending content.
* **Optimized Caching:** Uses `st.cache_resource` to minimize computational overhead.

---

### 📂 Repository Structure
```text
.
├── app.py              # Application Entry Point
├── notebooks/          # Model Engineering
│   └── movie_recommender.pkl
├── data/               # Metadata Assets
│   └── movie_titles _1_.csv
└── requirements.txt    # Dependency Manifest


## Live Demo
You can try the live application here:
👉 **[Netflix Recommendation Dashboard](https://netflix-recommendation-system-68.streamlit.app/)**
