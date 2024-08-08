import streamlit as st
import os
import dotenv
from openai import AzureOpenAI

# Load environment variables
dotenv.load_dotenv()
AOAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AOAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")

# Set up the Azure OpenAI client
client = AzureOpenAI(api_key=AOAI_KEY, azure_endpoint=AOAI_ENDPOINT, api_version="2024-05-01-preview")

# Streamlit UI setup
st.title("BSMP ChatGPT 🤖 - Write a Song")
artist = st.radio("Who should be the artist?", ["Drake", "Michael Jackson", "The Rock"])
st.header(artist)

st.subheader("Create a catchy hook and meaningful verse")

# Initialize session state for storing messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are an AI that creates a hook and verse for a famous singer on the topic requested by the user. The hook should be catchy and memorable, and the verse should be meaningful and relevant to the topic. The singer should be able to sing the hook and verse with their own unique style."}]

# Create a button to reset the conversation
if st.button("New Topic"):
    st.session_state.messages = [{"role": "system", "content": "You are an AI that creates a hook and verse for a famous singer on the topic requested by the user. The hook should be catchy and memorable, and the verse should be meaningful and relevant to the topic. The singer should be able to sing the hook and verse with their own unique style."}]

# Display all previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input and generate a response
user_input = st.chat_input(f"What do you want the song to be about by {artist}?")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-35-turbo",
            messages=st.session_state.messages,
            stream=False,
            temperature=0.7,
            max_tokens=100,
            top_p=0.95,
        )
        response_content = response.choices[0].message.content
        st.markdown(response_content)
        st.session_state.messages.append({"role": "assistant", "content": response_content})
