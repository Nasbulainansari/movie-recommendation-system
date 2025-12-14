import streamlit as st

def load_custom_css():
    st.markdown("""
        <style>
        /* ----------------- Base Styles ----------------- */
        .main {
            background: linear-gradient(135deg, #000000, #141414, #1f1f1f);
            color: white;
            font-family: 'Poppins', sans-serif;
            padding: 20px;
        }

        .title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .movie-card {
            text-align: center;
            background-color: #1f1f1f;
            border-radius: 15px;
            padding: 15px;
            transition: transform 0.3s ease;
        }

        .movie-card:hover {
            transform: scale(1.05);
        }

        img {
            border-radius: 10px;
            width: 100%;
            height: auto;
        }

        .movie-title {
            margin-top: 10px;
            font-size: 1.1rem;
            color: #f1f1f1;
        }

        /* ----------------- Responsive Media Queries ----------------- */

        /* Mobile Phones (max-width: 600px) */
        @media (max-width: 600px) {
            .title {
                font-size: 1.8rem;
            }

            .movie-card {
                padding: 10px;
                margin-bottom: 15px;
            }

            img {
                width: 100%;
                height: auto;
            }

            .movie-title {
                font-size: 1rem;
            }

            .stButton button {
                width: 100%;
                font-size: 1rem;
                padding: 10px;
            }
        }

        /* Tablets (600px to 1024px) */
        @media (min-width: 601px) and (max-width: 1024px) {
            .title {
                font-size: 2rem;
            }

            .movie-card {
                padding: 12px;
            }

            .movie-title {
                font-size: 1.1rem;
            }
        }

        /* Large Screens (above 1024px) */
        @media (min-width: 1025px) {
            .title {
                font-size: 2.5rem;
            }

            .movie-card {
                padding: 15px;
            }

            .movie-title {
                font-size: 1.2rem;
            }
        }
        </style>
    """, unsafe_allow_html=True)
