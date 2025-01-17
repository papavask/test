import streamlit as st
import streamlit.components.v1 as components

# HTML content with background image
html_content = """
<div style="background-image: url('bg2.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            height: 100vh;
            padding: 20px;">
    <h1 style="color: white;">Welcome to the Streamlit App!</h1>
    <p style="color: white;">This app has a custom background.</p>
</div>
"""

# Render the HTML in the Streamlit app
components.html(html_content, height=600)
