import streamlit as st

# Define the path to the image (local or URL)
image_url = "./bg-img.png"  # For a URL image
# image_path = "path/to/your/local/image.jpg"  # If using a local image

# Apply custom CSS to set the background image
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            height: 100vh;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Your Streamlit app content
st.title("Streamlit App with Background Image")
st.write("This is a simple example of how to add a background image.")
