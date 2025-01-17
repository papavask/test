import streamlit as st

# Use a local path or a URL for the image
image_url = "./bg-img.jpg"  # Or use a local path like "assets/my_background.jpg"

# Inject CSS to set the background image
st.markdown(
    f"""
    <style>
        .css-1d391kg {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            height: 100vh;  /* Full viewport height */
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Your Streamlit app content
st.title("Streamlit App with Background Image")
st.write("This is a simple example of how to add a background image.")
