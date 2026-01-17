
# AI Mood-Based Movie Recommender

# Overview

The AI Mood-Based Movie Recommender is a web-based application that recommends movies according to the user’s current emotional state.It combines Natural Language Processing (NLP) with a clean, modern AI dashboard UI to deliver personalized and explainable movie suggestions.The system focuses on user experience, readability, and emotional relevance, making it suitable for academic projects, demos, and real-world applications.

 # Key Features

- Mood-based movie recommendations (Romantic, Happy, Sad, Motivational, Thriller, etc.)
- AI-powered content similarity using NLP (TF-IDF + Cosine Similarity)
- Explainable AI – explains why a movie is recommended
- Professional UI dashboard
- Glassmorphism central container
- High readability with background overlay
- Animated floating bubbles for visual enhancement
- User-controlled recommendations (slider to choose number of results)
- Uses a custom curated movie dataset


# How It Works

- The user selects their current mood.
- Movie descriptions are processed using TF-IDF vectorization.
- Cosine similarity is calculated between user mood and movie content.
- The system ranks movies based on relevance.
- The top recommendations are displayed with clear explanations.

# Tech Stack

Frontend / UI:            Streamlit, HTML, CSS

Backend / Logic:          Python

Machine Learning / NLP:   TF-IDF Vectorizer, Cosine Similarity

Data Handling:            Pandas, NumPy

Visualization:            Custom UI components & animations

## 📂 Project Structure

AI_Mood_Based_Movie_Recommender/
│
├── data_processing/
│   └── preprocess.py
│
├── feature/
│   ├── recommender.py
│   ├── explain.py
│   └── gpt_explain.py
│
├── db/
│   └── movies.csv
│
├── static/
│   └── background.jpg
│
├── main.py
├── requirements.txt
└── README.md

## ▶ How to Run the Project
pip install -r requirements.txt
streamlit run main.py

## Use Case

This application helps users:

    - Choose movies that match their emotional state
    - Improve mood and entertainment experience
    - Understand recommendations through explainable AI

## Jupyter Notebook Support

- This project also includes a Jupyter Notebook–based implementation to demonstrate the core AI and NLP logic in an interactive, step-by-step manner.
- The notebook version is designed for:
- Academic demonstrations
- Understanding the recommendation logic without a web UI

## Notebook Features

- Loads the movie dataset directly from db/movies.csv
- Performs text preprocessing on movie descriptions and moods
- Applies TF-IDF vectorization and cosine similarity
- Generates mood-based movie recommendations inside the notebook
- Runs fully in Jupyter without requiring Streamlit

## How to Run the Notebook
- jupyter notebook
- Open the file:
AI_Mood_Movie_Recommender.ipynb
- Run all cells sequentially to view dataset exploration and recommendation results.

## Purpose of the Notebook Version

The Jupyter Notebook version focuses on clarity and explainability of the AI pipeline, while the Streamlit application provides a user-friendly web interface. Both versions share the same conceptual logic.

## 🎓 Academic Relevance

    - Demonstrates AI + NLP concepts
    - Focuses on human-centered AI design


## Future Enhancements

    - Real-time emotion detection from text or voice
    - Integration with live movie APIs (TMDB / OMDb)
    - User profiles and recommendation history

Mobile-responsive UI

## 👨 Author

Shivani Shambhavi
B.Tech CSE

