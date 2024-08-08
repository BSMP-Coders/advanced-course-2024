import streamlit as st  #👈 the streamlit library is imported and aliased as st
  
st.title("Welcome to BSMP Coding Class on Streamlit 🤖")  
st.header("Lesson 1: Introduction to Python and Streamlit")  
  
st.write("""  
Welcome to the first lesson of our coding class! This course is designed to introduce you to the basics of Python programming and creating interactive web apps with Streamlit.  
  
### Instructions for Running This App in GitHub Codespaces:  
1. **Open GitHub Codespaces**: Navigate to the repository and open it in GitHub Codespaces.  
2. **Run the App**: Start the Streamlit app by running: `streamlit run app.py`  
  
Use the sidebar to navigate to different sections of this lesson.  
""")  
  
# Sidebar with navigation and resources  
st.sidebar.image("https://github.com/BSMP-Coders/BSMP-Coders.github.io/raw/master/_media/logos/bam_coding_logo.png")  #, caption="BAM Coding Program Logo"
st.sidebar.header("About Streamlit")  
st.sidebar.write("[Streamlit](https://streamlit.io) is an awesome tool to create interactive web apps with Python. You'll learn how to use it in this course!")  
#st.sidebar.image("bam_coding_logo_white.png")
#st.sidebar.image("https://github.com/BSMP-Coders/BSMP-Coders.github.io/raw/master/_media/logos/bam_coding_logo.png")

  
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
  
# End Note  
st.write("Ready to begin? Let's start with some Python basics and see how Streamlit can make coding more fun and interactive! 🚀")  
st.write("Head over to `pages/1_basics.py` to continue learning.")  

st.divider()
# Interactive Elements  
with st.expander("Interactive Elements 🎛️", expanded=False):    
    st.subheader("Try it Yourself! ✨")    
    st.write("Let's try adding some interactive elements to your app.")    
        
    # User input using columns  
    name = st.text_input("What's your name, young coder?")
    col1, col2 = st.columns(2)  
    with col1:  
        st.write(f"Hello, {name}! 👋")
        #if name:  
        #    st.success(f"Nice to meet you, {name}! 👋") 
    with col2: 
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Microsoft_icon.svg/1280px-Microsoft_icon.svg.png", caption="Microsoft Logo", width=100) 
        
    # Slider for experience level  
    experience_level = st.slider("How much do you love coding?", 0, 100, 25)  
    st.write(f"Your coding love level is: {experience_level}% ❤️")  
        
    # Color Picker  
    favorite_color = st.color_picker("Pick your favorite color")  
    st.write(f"Your favorite color is: {favorite_color} 🎨") 