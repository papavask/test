import streamlit as st

# Set page configuration
st.set_page_config(page_title="Custom Background", layout="wide")

# Add CSS for the background image
background_image = """
<style>
body {
    background-image: url('bg2.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
}
</style>
"""

# Inject the custom CSS
st.markdown(background_image, unsafe_allow_html=True)

# Streamlit app content
st.title("Welcome to the Streamlit App!")
st.write("This app has a custom background.")
