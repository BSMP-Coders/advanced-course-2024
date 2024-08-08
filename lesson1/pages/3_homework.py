import streamlit as st  
  
st.title("Homework Submission Instructions")  
  
st.header("Overview of Homework Assignment 1")  
st.write("""  
Welcome to your first homework assignment for the Advanced Coding Streamlit course! This assignment will help you get familiar with creating a [multi-page](https://docs.streamlit.io/develop/concepts/multipage-apps/overview) Streamlit app and using different features from the [Streamlit API reference](https://docs.streamlit.io/develop/api-reference).  
You will create a Streamlit app with the following pages:  
1. **About Me**: A page where you introduce yourself.  
2. **Favorite Animals**: A page where you display a list of your favorite animals with images.  
3. **My Hobbies**: A page where you describe your hobbies and use interactive elements.  
4. **Fun Facts**: A page to share fun facts about yourself using columns and layout features.  
Each page should use different Streamlit components to display content.  
""")  
  
st.subheader("Accepting the GitHub Classroom Homework Invitation")  
st.write("""  
To get started, please accept the GitHub Classroom homework invitation by following this link:   
[GitHub Classroom Homework 1 Invitation](https://classroom.github.com/a/KddoilYB).   
  
Once accepted, you will have your own repository to work on the homework assignment.
""")  

st.divider()

st.subheader("Submitting Your Homework Assignment")  
st.write("""  
When you are done with your work, follow these simple steps to submit your homework:  
  
1. **Commit Your Changes**: Use the Source Control tab in VS Code to commit your changes.   
2. **Push Your Changes**: Push (sync) your changes to the GitHub repository.    
""")  

with st.expander("For detailed instructions, refer to the [BSMP Homework Submission process](https://bsmp-coders.github.io/#/students/Getting-Started?id=_4-submitting-your-homework-assignment-how-to-commit-and-push-changes).",icon="🔥",expanded=False):
    
    #st.header("Submitting Your Homework Assignment")

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
        Push (sync) your changes to the repository to submit homework.
        """)
        st.image("https://github.com/BSMP-Coders/advanced_coding_wiki/raw/main/media/codespaces/submit_2_push_sync_changes.png")

    with tab3:
        st.write("""
        **Sync Changes**  
        Stop Codespace when finished.
        """)
        st.image("https://github.com/BSMP-Coders/advanced_coding_wiki/raw/main/media/codespaces/submit_3_stop_codespace.png")



# Sidebar with navigation and resources  
st.sidebar.image("https://github.com/BSMP-Coders/BSMP-Coders.github.io/raw/master/_media/logos/bam_coding_logo.png")  
st.sidebar.header("Resources")  
st.sidebar.markdown("""  
- [Python Beginner's Guide](https://docs.python.org/3/tutorial/index.html)  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)  
""")  
  
# Homework Reminder  
st.sidebar.header("Homework Reminder 📚")  
st.sidebar.info("""  
Work on your homework assignment to create a [multi-page](https://docs.streamlit.io/develop/concepts/multipage-apps/overview) Streamlit app with the following sections:  
- About Me  
- Favorite Animals  
- My Hobbies  
- Fun Facts  
  
Submit it through GitHub Classroom when you're done! Good luck! 🌟  
""")  
