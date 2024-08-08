from openai import AzureOpenAI
import os  
import streamlit as st  
import dotenv

dotenv.load_dotenv()

# Streamlit app title and header  
st.title("Welcome to BSMP Coding Class on Streamlit 🤖")  
st.header("Lesson 3: Streamlit + ChatGPT Integration")  

st.write("Welcome to the third lesson of our coding class! In this lesson, we will learn how to integrate OpenAI's ChatGPT with Streamlit to create an interactive chatbot.") 
 
st.write("Use the sidebar to navigate to different sections of this lesson.")

with st.expander("Instructions for Running This App in GitHub Codespaces 🤖", expanded=False):  
    st.write("""  
    ### Instructions for Running This App in GitHub Codespaces:  
    1. **Open GitHub Codespaces**: Navigate to the repository and open it in GitHub Codespaces.  
    2. **Run the App**: Start the Streamlit app by running: `streamlit run app.py`  
    
    Use the sidebar to navigate to different sections of this lesson.  
    """)  

# Sidebar with navigation and resources  
st.sidebar.image("https://github.com/BSMP-Coders/BSMP-Coders.github.io/raw/master/_media/logos/bam_coding_logo.png")  
st.sidebar.header("Resources")  
st.sidebar.markdown("""  
- [Streamlit Chat](https://docs.streamlit.io/develop/api-reference/chat)
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [OpenAI API Documentation](https://beta.openai.com/docs/)  
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)  
""")  


# End Note  
st.write("Ready to begin? Let's start integrating ChatGPT with Streamlit and see how we can create an interactive chatbot! 🚀")  
st.write("Head over to `pages/1_basics.py` to continue learning.")  
st.divider()  

st.subheader("Try it Yourself! ✨")    
#chat_basics_TA_notes = st.checkbox("Quick Start 🤖", value=True)
#if chat_basics_TA_notes:
    #st.markdown("Here's a simple example to get you started with ChatGPT integration in Streamlit.")
#with st.expander("Quick Start 🤖", expanded=False):    
    #st.subheader("Try it Yourself! ✨")    
st.markdown("Here's a simple example to get you started with ChatGPT integration in Streamlit.")
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