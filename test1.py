import streamlit as st

# URL or local path to the image
image_url = "assets/bg2.jpg"  # Or use a local path like "assets/background.jpg"

# Add the custom CSS to set the background image
st.markdown(
    f"""
    <style>
        body {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            height: 100vh;  /* Ensure the image covers the entire viewport height */
            margin: 0;
        }}
        .stApp {{
            background: transparent;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app content
st.title("Streamlit App with Background Image test")
st.write("This is a simple example of how to add a background image.")
