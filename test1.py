import streamlit as st
from PIL import Image
import base64

# URL or local path to the image
image_url = "assets/bg2.jpg"  # Or use a local path like "assets/background.jpg"
mime_type = image_url.split('.')[-1:][0].lower()
with open(image_url, "rb") as f:
   content_bytes = f.read()
content_b64encoded = base64.b64encode(content_bytes).decode()
image_url = f'data:image/{mime_type};base64,{content_b64encoded}'
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
