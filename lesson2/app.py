
import streamlit as st  
import random  
  
# Main title of the page  
st.title("Lesson 2: IF Statements and Operators 📘")  
  
# Recap Lesson 1 and Homework Assignment Breakout  
st.header("Recap of Lesson 1 and Homework")  
st.write("""  
In our previous lesson, we learned the basics of Python and Streamlit, and you had a homework assignment to create a multi-page Streamlit app. Great job to everyone who submitted their assignments! 🌟  
""")  
  
# Lesson 2 Overview  
st.header("Lesson 2 Overview")  
st.write("""  
Today, we're going to dive into conditional logic with if/else statements and explore how to use them in Streamlit. We will also look at lists, loops, and logical operators. Get ready to code some cool examples! 🚀  
""")  
  
# IF/ELSE Statements  
st.header("IF/ELSE Statements")  
st.markdown("""  
An `if` statement executes a block of code if a specified condition is true. If the condition is false, an optional `else` block can be executed.  
  
In Python, indentation is crucial as it defines the scope of the code blocks.  
""")  
  
# Logical Operators  
st.header("Logical Operators")  
st.write("""  
Logical operators are used to combine conditional statements:  
  
- `==`: Equal to  
- `!=`: Not equal to  
- `<`: Less than  
- `<=`: Less than or equal to  
- `>`: Greater than  
- `>=`: Greater than or equal to  
- `and`: Logical AND  
- `or`: Logical OR  
- `not`: Logical NOT  
""")  
  

# Interactive Elements  
with st.expander("Interactive Elements 🎛️", expanded=False):
    st.subheader("Try it Yourself! ✨")  
    st.write("Add some interactive elements to your app and see the magic happen!")  
      
    # User input  
    name = st.text_input("What's your name, young coder?")  
    if name:  
        st.success(f"Hello, {name}! 👋 Welcome to the world of coding!")  
  
    # Button to display a friendly message  
    if st.button("Say Hello!"):  
        st.balloons()  
        st.write(f"Hello, {name}! You're off to a great start! 🚀")  


with st.expander("Interactive Elements 🎛️", expanded=False):
    text = """

    - More information on streamlit [here](https://docs.streamlit.io/)

    """

    st.write(text)
    st.success("Today is Thursday")
    st.error("oops")

    st.slider("This is a slider", 0, 100, (25, 75))
    st.divider()  # 👈 Draws a horizontal rule
    st.write("This text is between the horizontal rules.")

    st.image("logos/microsoft_logo.png")

    st.success("Success")

    #st.sidebar.header("Streamlit Sidebar")
    #st.sidebar.image("logos/microsoft_logo.png")

    #button1 = st.button("Click Me")
      
# Sidebar  
#st.sidebar.image("bam_coding_logo_white.png")
st.sidebar.image("https://github.com/BSMP-Coders/BSMP-Coders.github.io/raw/master/_media/logos/bam_coding_logo.png")

  
# Sidebar with helpful resources  
st.sidebar.header("Helpful Resources")  
st.sidebar.markdown("""
## Additional Resources 📚  
   
For more information on Python if statements and for loops, please go through these tutorials on [vscodeedu - intro to python](https://vscodeedu.com/courses/intro-to-python) using your BAM emails:  
   
- **Unit 3 (vscodeedu) - If Statements**: [If Statements Tutorial](https://vscode.dev/edu?courseId=intro-to-python&workspace-scheme=vscode-edu-workspace&profile=default#select-course-node=intro-to-python%3Aitp-if)  
- **Unit 5 (vscodeedu) - For Loops**: [For Loops Tutorial](https://vscode.dev/edu?courseId=intro-to-python&workspace-scheme=vscode-edu-workspace&profile=default#select-course-node=intro-to-python%3Aitp-for)  

""")
st.sidebar.markdown("""  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)  
""")  

st.sidebar.markdown("""                    
# Check out my other Streamlit projects! 🚀
- [StreamlitLand Adventure RPG](https://github.com/TomJohnH/streamlit-game)
- [Streamlit Dungeon Crawler](https://github.com/TomJohnH/streamlit-dungeon)
""")