import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* Main container styling */
        .main {
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Header styling */
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 2rem;
            font-size: 2.5rem;
            font-weight: 700;
            border-bottom: 3px solid #3498db;
            padding-bottom: 1rem;
        }

        /* Subheader styling */
        h2 {
            color: #34495e;
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
            font-weight: 600;
        }

        /* Button styling */
        .stButton button {
            width: 100%;
            border-radius: 8px;
            height: 3em;
            background-color: #2c3e50;
            color: white;
            border: none;
            font-weight: 600;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .stButton button:hover {
            background-color: #3498db;
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        /* Input field styling */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            border-radius: 8px;
            border: 2px solid #e0e0e0;
            padding: 0.5rem 1rem;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: #3498db;
            box-shadow: 0 0 0 2px rgba(52,152,219,0.2);
        }

        /* Tab styling */
        .stTab {
            background-color: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
            border: 1px solid #f0f2f6;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: #f8f9fa;
            padding: 2rem 1rem;
            border-right: 1px solid #e9ecef;
        }

        /* Template preview container */
        .template-preview {
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }

        .template-preview:hover {
            border-color: #3498db;
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        /* Profile picture container */
        .profile-container {
            text-align: center;
            padding: 1rem;
            border-radius: 8px;
            background-color: #f8f9fa;
            margin-bottom: 1.5rem;
        }

        /* Success message styling */
        .stSuccess {
            background-color: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #c3e6cb;
        }
        </style>
    """, unsafe_allow_html=True)