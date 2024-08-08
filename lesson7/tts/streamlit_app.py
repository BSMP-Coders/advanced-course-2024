import streamlit as st
from openai import AzureOpenAI
import os
import dotenv
import base64

# Load environment variables
dotenv.load_dotenv()

# Get the keys and variables from environment
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT_BSMP24")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY_BSMP24")
MODEL_NAME = 'tts'  # Model name for TTS

# Initialize the AzureOpenAI client
openai_client = AzureOpenAI(api_key=AZURE_OPENAI_API_KEY, azure_endpoint=AZURE_OPENAI_ENDPOINT, api_version="2024-02-15-preview")

# Streamlit app
st.title("Text to Speech with Azure OpenAI")
st.write("Enter text to convert it to speech using Azure OpenAI's TTS model.")

# Input text
input_text = st.text_area("Input Text", "I'm excited to try text to speech.")

# TTS function
def text_to_speech(input_text):
    data = {
        "model": MODEL_NAME,
        "input": input_text,
        "voice": "alloy"
    }
    response = openai_client.audio.speech.create(
        model=MODEL_NAME,
        voice="alloy",
        input=input_text
    )
    audio_file = 'speech_output.mp3'
    response.write_to_file(audio_file)
    return audio_file

# Button to convert text to speech
if st.button("Convert to Speech"):
    if input_text:
        audio_file = text_to_speech(input_text)
        st.audio(audio_file, format='audio/mp3')
        st.success("Text converted to speech successfully.")
    else:
        st.error("Please enter text to convert.")
