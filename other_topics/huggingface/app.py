import os
import streamlit as st  
import dotenv
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
dotenv.load_dotenv()

# Initialize the Hugging Face pipeline
pipe = pipeline("text-generation", model="openai-community/gpt2")
st.subheader("Our First ChatGPT-like app")  

# Initialize session state for storing messages
if "messages" not in st.session_state:  
    st.session_state.messages = []  

# Create a button to reset the conversation
if st.button("New Topic"):        
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
        # Use the Hugging Face pipeline to generate a response
        response = pipe(user_input, max_length=150, num_return_sequences=1)[0]['generated_text']
        st.markdown(response)  
        st.session_state.messages.append({"role": "assistant", "content": response})
