import streamlit as st  

# Set the title of the web app  
st.title("BSMP Coding Class: Python Basics with Streamlit 🐍✨")  
  
# Section for the print statement  
st.header("Print Statement")  
st.write("The `print` statement is used to display text on the screen. It's one of the most basic operations in Python.")  
st.code("print('Hello, world!')")  

# Basic Text  
st.write("This is your first Streamlit app. Let's learn and have some fun! 🎉")  

# Adding a Subheader  
#st.subheader("Introduction to Streamlit")  

#st.header("Interactive Element")  
#st.write("Below is an example of an interactive element in Streamlit.")  
#name = st.text_input("Enter your name")  
#st.write(f"Hello, {name}!")  


# place holder on adding imaegs

# place holder on adding interactive elements


# place holder for adding columns

st.header("Hi Coders!")
st.title("my name is Phillip")


# Show how to use markdown to make text italic or bold  
st.write("Here's an example of how to use markdown to *italicize* or **bold** text in Streamlit:")  
st.markdown("You can write in *italic* or in **bold**.")  

#st.link_button("docs",url="https://docs.streamlit.io/")

from datetime import datetime  
date = st.date_input("Choose a date", datetime.now())  
st.write(f"The selected date is {date}")  


# How to add an image  
st.write("Here's how you can add an image to your Streamlit app:")  
st.write("```python\nst.image('path_to_your_image.jpg')\n```")  
st.write("Replace `'path_to_your_image.jpg'` with the actual path to your image.")  
#st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit Logo")
#st.image("https://image.pngaaa.com/96/8993096-middle.png", caption="Streamlit Logo")
# Placeholder for BAM Coding Program logo  
#st.image("bam_coding_logo_white.png")  


# Show how to use interactive elements like sliders  
st.write("You can also add interactive elements, such as sliders:")  
#age = st.slider('Select your age', 0, 100, 25)  
#st.write(f"You've selected: {age} years old")  

# Sidebar  
st.sidebar.title("Navigation")  
st.sidebar.write("Use this sidebar to navigate through different sections.")  
  
# Ending Note  
st.write("Explore more features and have fun coding with Streamlit! 🚀")  


with st.sidebar.expander("Introduction to Python and Streamlit",icon="🔥",expanded=False):
  st.write("""  
  1. **Basic Streamlit Commands:**  
      - `st.title("Title")` - Adds a title to your app.  
      - `st.header("Header")` - Adds a header.  
      - `st.write("Text")` - Writes text to the app.  
  2. **Adding Images:**
      - `st.image(image_path, caption="Caption")` - Adds an image to the app.

  3. **Interactive Elements:**
      - `st.text_input("Label")` - Adds a text input box.
      - `st.button("Button")` - Adds a button.
      - `st.selectbox("Label", options)` - Adds a select box.
      - `st.slider("Label", min_value, max_value, value)` - Adds a slider.
      - `st.checkbox("Label")` - Adds a checkbox.
      - `st.radio("Label", options)` - Adds a radio button.
      - `st.file_uploader("Label", type="file_type")` - Adds a file uploader.
  4. **Layouts:**
      - `st.columns(num_columns)` - Creates a layout with the specified number of columns.
      - `st.sidebar` - Adds a sidebar to the app.
      - `st.expander("Label")` - Adds an expander to the app.
          
  """)  
  
