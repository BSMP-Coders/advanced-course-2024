from openai import AzureOpenAI   
import os   
import streamlit as st   
import dotenv   
import random   
  
dotenv.load_dotenv()   
  
# Azure OpenAI credentials   
AOAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]   
AOAI_KEY = os.environ["AZURE_OPENAI_API_KEY"]   
MODEL_NAME = "gpt-35-turbo"   
  
# Initialize Azure OpenAI client   
client = AzureOpenAI(api_key=AOAI_KEY, azure_endpoint=AOAI_ENDPOINT, api_version="2024-05-01-preview")   
  
# Character characteristics   
characters = {   
    "Alex": {"hair": "brown", "earrings": "no", "image": "https://img.buzzfeed.com/buzzfeed-static/static/2016-12/27/2/asset/buzzfeed-prod-web-14/sub-buzz-25745-1482823329-1.jpg"},   
    "Susan": {"hair": "blonde", "earrings": "yes", "image": "https://img.buzzfeed.com/buzzfeed-static/static/2016-12/27/2/asset/buzzfeed-prod-web-15/sub-buzz-7240-1482824615-1.jpg"}   
}   
  
# Initialize game state with system prompt and answered questions   
if 'game_state' not in st.session_state:   
    selected_character = random.choice(list(characters.keys()))   
    st.session_state.game_state = {   
        "selected_character": selected_character,   
        "guesses": [],   
        "answered_questions": [],   
        "message": "Ask a question or make a guess!",   
        "system_prompt": f"You are an AI system hosting the game 'Guess Who?'. Your role is to respond to questions about the selected character and determine correct guesses based on their characteristics. The character you are guessing has the following characteristics: {characters[selected_character]}. if the person makes a guess of {selected_character} then the system will respond with {selected_character}."   
    }   
  
# Reset game state with system prompt and answered questions   
if st.button("Reset Game"):   
    selected_character = random.choice(list(characters.keys()))   
    st.session_state.game_state = {   
        "selected_character": selected_character,   
        "guesses": [],   
        "answered_questions": [],   
        "message": "Ask a question or make a guess!",   
        "system_prompt": f"You are an AI system hosting the game 'Guess Who?'. Your role is to respond to questions about the selected character and determine correct guesses based on their characteristics. The character you are guessing has the following characteristics: {characters[selected_character]}. if the person makes a guess of {selected_character} then the system will respond with {selected_character}"   
    }   
  
st.title('Guess Who? Game with Azure OpenAI')   
  
# Update instructions with suggestions on what questions to ask   
st.write("Try to guess the selected character by asking yes/no questions about their characteristics, like hair color or presence of earrings.")   
  
# Display current state   
st.write(f"Guesses: {st.session_state.game_state['guesses']}")   
st.write(f"Answered Questions: {st.session_state.game_state['answered_questions']}")   
  
# User input for questions or guesses   
user_input = st.text_input("Ask a question or make a guess:")   
  
if user_input:   
    system_prompt = st.session_state.game_state["system_prompt"]   
    response = client.chat.completions.create(   
        model=MODEL_NAME,   
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_input}],   
        stream=False   
    )   
    response_content = response.choices[0].message.content   
    st.write(response_content)   
  
    # Normalize the user input to ensure consistent recognition of guesses   
    normalized_input = user_input.strip().lower()   
    selected_character = st.session_state.game_state["selected_character"].lower()   
  
    if normalized_input == selected_character or any(normalized_input.endswith(f" is it {name.lower()}?") for name in characters):  
        st.session_state.game_state["guesses"].append((user_input, True))  
        st.success(f"Correct! You guessed the character {selected_character.capitalize()}!")  
    else:  
        st.session_state.game_state["guesses"].append((user_input, False))  
        st.session_state.game_state["answered_questions"].append(user_input)  
  
  
# Sidebar with character information   
st.sidebar.header("Characters")   
for name, details in characters.items():   
    st.sidebar.image(details["image"], width=100)   
    st.sidebar.write(name)  
