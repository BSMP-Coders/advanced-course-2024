import streamlit as st  #👈 the streamlit library is imported and aliased as st
#![](https://pbs.twimg.com/media/F80nu7kWYAAjeE7?format=png&name=small)
st.markdown("""
# Lesson 3: Streamlit + ChatGPT Integration 🤖  


## Streamlit Basics Review 📝  
   
Streamlit is a powerful, user-friendly framework for creating interactive web applications with Python. Let’s quickly revisit the core concepts:  
   
### Basic Streamlit Commands  
   
1. **Title and Header**: Use `st.title` and `st.header` to add titles and headers to your app.  
   ```python  
   st.title("My App")  
   st.header("Welcome to my app!")  
   ```  
     
2. **Text**: Use `st.text` and `st.markdown` to add text to your app.  
   ```python  
   st.text("This is simple text.")  
   st.markdown("**This is markdown text.**")  
   ```  
   
3. **Input Widgets**: Use `st.button`, `st.text_input`, and `st.selectbox` to add interactive elements.  
   ```python  
   if st.button("Click me!"):  
       st.write("Button clicked!")  
   user_input = st.text_input("Enter some text")  
   option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])  
   ```  

----
               
## Introduction to ChatGPT and Azure OpenAI API 🌐  
   
ChatGPT is a language model developed by OpenAI that can understand and generate human-like text. We’ll use the Azure OpenAI API to integrate ChatGPT into our Streamlit app.  
   
### Setting Up Azure OpenAI API  
   
1. **Install Required Packages**:  
  
   ```bash  
   pip install openai streamlit python-dotenv  
   ```  
   
2. **API Key Setup**: Obtain your API key from Azure and set it up in your app.  
  
   ```python  
   from openai import AzureOpenAI  
   import os  
   import dotenv  
  
   dotenv.load_dotenv()  
  
   AOAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")  
   AOAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")  
  
   client = AzureOpenAI(  
       api_key=AOAI_KEY,  
       azure_endpoint=AOAI_ENDPOINT,  
       api_version="2024-05-01-preview",  
   )  
   ```  
   
3. **Making API Calls**: Use the `client.chat.completions.create` method to generate responses.  
  
   ```python  
   response = client.chat.completions.create(  
       model="gpt-35-turbo",  
       messages=[  
           {"role": "user", "content": "Hello, how can I help you?"}  
       ],  
       stream=False,  
   )  
   reply = response.choices[0].message.content
   ```
----
            
## Building Your Chat Application 🛠️  
   
### Step-by-Step Guide  
   
1. **Initialize Chat History**:  
   ```python  
   if "messages" not in st.session_state:  
       st.session_state.messages = []  
   ```  
   
2. **Display Chat Messages**:  
   ```python  
   for message in st.session_state.messages:  
       with st.chat_message(message["role"]):  
           st.markdown(message["content"])  
   ```  
   
3. **Handle User Input**:  
   ```python  
   if prompt := st.chat_input("What is up?"):  
       st.chat_message("user").markdown(prompt)  
       st.session_state.messages.append({"role": "user", "content": prompt})  
       response = f"Echo: {prompt}"  
       st.chat_message("assistant").markdown(response)  
       st.session_state.messages.append({"role": "assistant", "content": response})  
   ```  
   
## Submitting Your Work 📬  
   
Once you've completed the lesson, submit your work through the provided submission link.  
   
## Ready, Set, Code! 🏁  
   
Let's get coding and bring your chatbot to life! 🚀
""")