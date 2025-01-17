import streamlit as st

# Set page configuration
st.set_page_config(page_title="Custom Background", layout="wide")

# Add CSS for the background image
background_image = """
<style>
body {
    background-image: url('https://github.com/papavask/test/blob/main/bg-img.jpg?raw=true');
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


# insert image
#st.image("./bg2.jpg")

#htp="https://github.com/papavask/test/blob/cbe639559116540999088d6f38f350d6fff22acc/assets/bg2.jpg"
#st.image(htp, caption= 'logo', width=350)
