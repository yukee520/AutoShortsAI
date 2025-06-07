# app.py
import streamlit as st
import os
import subprocess

st.title("AutoShortsAI Video Generator")

# User input for video topic
prompt = st.text_input("Enter your video topic or keyword")

if st.button("Generate Video"):
    if prompt:
        # Save prompt to a temporary file or environment variable
        with open("input_prompt.txt", "w") as f:
            f.write(prompt)

        # Call your existing script
        result = subprocess.run(["python", "autoshorts.py"], capture_output=True, text=True)
        
        st.success("Video generated!")
        st.text(result.stdout)
    else:
        st.warning("Please enter a topic first.")
