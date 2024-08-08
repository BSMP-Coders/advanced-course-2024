from openai import AzureOpenAI
import os  
import streamlit as st  
import dotenv
dotenv.load_dotenv()
    
# Put the keys and variables here (never put your real keys in the code)  
AOAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]  
AOAI_KEY = os.environ["AZURE_OPENAI_API_KEY"]  
MODEL_NAME = "gpt-35-turbo"  

# Set up the client for AI Chat  
client = AzureOpenAI(api_key=AOAI_KEY,azure_endpoint=AOAI_ENDPOINT,api_version="2024-05-01-preview",)

st.subheader("Our First ChatGPT-like app")  

# Initialize session state for storing messages
if "messages" not in st.session_state:  
    st.session_state.messages = []  
    #st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant that responds like a pirate."}]

# Create a button to reset the conversation
if st.button("New Topic"):        
    #st.session_state.messages = []  
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant that responds like a pirate."}]

# Display all previous messages
for message in st.session_state.messages:  
    with st.chat_message(message["role"]):  
        st.markdown(message["content"])  

# Get user input and generate a response
user_input = st.chat_input("What is up?")
if user_input:  
    st.session_state.messages.append({"role": "user", "content": user_input})  
    with st.chat_message("user"):  
        st.markdown(user_input)  
    with st.chat_message("assistant"):  
        response = client.chat.completions.create(  
            model=MODEL_NAME,  
            messages=st.session_state.messages,  
            stream=False
        )
        response_content = response.choices[0].message.content  
        st.markdown(response_content)  
        st.session_state.messages.append({"role": "assistant", "content": response_content})