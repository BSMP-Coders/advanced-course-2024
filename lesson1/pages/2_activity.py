import streamlit as st  
  
st.title("🎉 Activity: Create Your First Streamlit App")  
  
st.header("Objective")  
st.write("Create a simple Streamlit app that displays a title, header, and some text.")  
  
st.header("Instructions")  
st.write("Follow these steps to create your first Streamlit app:")  
  
# Step 1  
st.subheader("Step 1: Open a New Python Script")  
st.write("Create a new Python script called `hello_world.py`.")  
  
# Step 2  
st.subheader("Step 2: Enter the Following Code")  
st.write("Copy and paste this code into your script:")  
st.code("""  
import streamlit as st  
  
st.title("Hello World! 🌎")  
st.header("This is a header")  
st.write("Welcome to your first Streamlit app. 🎈")  
""", language='python')  
  
# Step 3  
st.subheader("Step 3: Run Your App")  
st.write("Save your script and run the app using this command in the terminal:")  
st.code("streamlit run hello_world.py", language='bash')  
  
# Step 4
st.subheader("Step 4: Submitting Your Work")  
st.write("""  
When you are done with your work, follow these simple steps to submit your changes:  
  
1. **Commit Your Changes**: Use the Source Control tab in VS Code to commit your changes.   
2. **Push Your Changes**: Push (sync) your changes to the GitHub repository.    
""")  

with st.expander("Submitting Your Assignment",expanded=False):
    tab1, tab2, tab3 = st.tabs(["Stage and Commit", "Push Changes", "Sync Changes"])

    with tab1:
        st.write("""
        **Stage and Commit**  
        Use the Source Control tab in VS Code to stage and commit your changes.
        """)
        st.image("https://github.com/BSMP-Coders/advanced_coding_wiki/raw/main/media/codespaces/submit_1_stage_commit.png")

    with tab2:
        st.write("""
        **Push Changes**  
        Push (sync) your changes to the repository to submit new code.
        """)
        st.image("https://github.com/BSMP-Coders/advanced_coding_wiki/raw/main/media/codespaces/submit_2_push_sync_changes.png")

    with tab3:
        st.write("""
        **Sync Changes**  
        Stop Codespace when finished.
        """)
        st.image("https://github.com/BSMP-Coders/advanced_coding_wiki/raw/main/media/codespaces/submit_3_stop_codespace.png")

    st.write("For detailed instructions, refer to the [BSMP Homework Submission process](https://bsmp-coders.github.io/#/students/Getting-Started?id=_4-submitting-your-homework-assignment-how-to-commit-and-push-changes).")  

st.divider()
# Step 5  
with st.expander("Optional: Explore and Add Features", expanded=False):
    st.subheader("Step 5: Explore and Add Features")  
    st.write("Enhance your app by completing these tasks:")  
    st.markdown("""  
    - Add a subheader using `st.subheader("This is a subheader")`.  
    - Add a text input to accept the user's name and display a greeting using `st.text_input` and `st.write`.  
    - Use the Streamlit documentation to explore and add one more interactive element of your choice. [Streamlit API Reference](https://docs.streamlit.io/develop/api-reference)  
    """)  
    
    st.write("Here’s an example of how you can add a text input and display a greeting:")  
    st.code("""  
    import streamlit as st  
    
    st.title("Hello World! 🌎")  
    st.header("This is a header")  
    st.subheader("This is a subheader")  
    
    name = st.text_input("Enter your name:")  
    st.write(f"Hello, {name}! 🎉")  
    """, language='python')  