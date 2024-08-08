import streamlit as st
from openai import AzureOpenAI
import os
import dotenv

# Load environment variables
dotenv.load_dotenv()
AOAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AOAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")

# Set up the Azure OpenAI client
client = AzureOpenAI(api_key=AOAI_KEY, azure_endpoint=AOAI_ENDPOINT, api_version="2024-05-01-preview")

# Streamlit UI setup
st.title("Create an Interactive Story")

# User input for story prompt
custom_prompt = st.text_area("Enter the beginning of your story:")
user_input = st.text_input("Enter what happens next:")

# Initialize session state with custom prompt
if 'story_prompts' not in st.session_state:
    st.session_state['story_prompts'] = [{"role": "system", "content": "You are an AI that helps create an interactive story. Continue the story based on the user's input."}]
    st.session_state['story'] = []

# Function to generate story continuation
def generate_story(prompt):
    st.session_state['story_prompts'].append({"role": "user", "content": prompt})
    completion = client.chat.completions.create(
        model="gpt-35-turbo",
        messages=st.session_state['story_prompts'],
        stream=False,
        temperature=0.7,
        max_tokens=100,
        top_p=0.95,
    )
    response = completion.choices[0].message.content
    st.session_state['story'].append(response)
    return response

# Button to generate story continuation
if st.button("Continue Story"):
    if user_input:
        generate_story(user_input)

# Display story
for part in st.session_state['story']:
    st.write(part)
