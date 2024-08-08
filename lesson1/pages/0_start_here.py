import streamlit as st  
  
# Page configuration  
#st.set_page_config(page_title="Python and Streamlit Basics", page_icon="🐍")  
  
# Main title of the page  
st.title("Python and Streamlit Basics 🐍✨")  
  
# Introduction to the basics  
st.markdown("""  
Welcome coders! In this section, we'll explore the basic concepts of Python and how to use Streamlit to create interactive web apps. Let's get started!  
""")  
  
# Creating Streamlit tabs  
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Print Statement", "Variables & Data Types", "Basic Commands", "Interactive Elements", "Layouts with Columns"])  
  
with tab1:  
    st.header("Python Print Statement")  
    st.markdown("""  
    The `print` statement is used to output text to the console. It's one of the most basic and essential functions in Python.  
    """)  
    st.code("print('Hello, world!')", language='python')  
    st.text_area("Console Output", "Hello, world!", height=100, help="This is what the output of the print statement would look like in the console.")  
  
with tab2:  
    st.header("Variables and Data Types")  
    st.markdown("""  
    Variables are like containers that store data values. A data type tells Python what kind of data is stored in a variable.  
    """)  
    st.code("""  
    name = "Alice"  # str (string)  
    age = 30        # int (integer)  
    height = 5.5    # float (floating-point number)  
    """, language='python')  
    st.markdown("""  
    Check the data type of a variable using the `type()` function.  
    """)  
    st.code("""  
    type(name)  # Output: <class 'str'>  
    type(age)   # Output: <class 'int'>  
    type(height)# Output: <class 'float'>  
    """, language='python')  

    st.code("""
    # The first line of code declares a variable called "firstName" and initializes it with the value "John".
    firstName = "John"  

    # The line of code below contains an error. The variable name "first Name" is not valid because it contains a space.
    # The correct way to write the variable name is "firstName".
    #first Name = "John" # Error

    # declares a variable called "lastName" and initializes it with the value "Doe".
    lastName = "Doe"

    # uses the `print` statement to display the text "Hello " followed by the value of the variable "firstName", followed by a space, followed by the value of the variable "lastName".
    print("Hello " + firstName + " " + lastName)

    # The output of the code is the text "Hello John Doe".
            """, language='python')
  
with tab3:  
    st.header("Basic Streamlit Commands")  
    st.markdown("""  
    Streamlit provides simple commands to create web app elements. Here are a few to get you started.  
    """)  
    st.code("""  
    st.write("Hello, Streamlit!")  # Display text  
    # image placeholder - desc of image  
    """, language='python')  
  
with tab4:  
    st.header("Interactive Elements in Streamlit")  
    st.markdown("""  
    Streamlit makes it easy to add interactive elements to your web app.  
    """)  
    st.code("""  
    age = st.slider('Select your age', 0, 100, 25)  # Slider for numeric input  
    st.write(f'Your age is: {age}')  
    """, language='python')  
    # Demonstration of interactive elements  
    age_demo = st.slider('Try the slider!', 0, 100, 25)  
    st.write(f'You selected: {age_demo}')  
  
with tab5:  
    st.header("Layouts with Columns")  
    st.markdown("""  
    You can organize your app's layout using columns.  
    """)  
    st.code("""  
    col1, col2 = st.columns(2)  
    with col1:  
        st.write("This is column 1.")  
    with col2:  
        st.write("This is column 2.")  
    """, language='python')  
    # Demonstration of using columns  
    col1, col2 = st.columns(2)  
    with col1:  
        st.write("Content in column 1.")  
    with col2:  
        st.write("Content in column 2.")  
  
# Navigation sidebar  
st.sidebar.title("Learn Python & Streamlit")  
st.sidebar.markdown("""  
Navigate through the sections to learn different aspects of Python and Streamlit.  
- Basics  
- Variables & Data Types  
- Interactive Elements  
""")  
  
# Resources and links in the sidebar  
st.sidebar.subheader("Resources")  
st.sidebar.markdown("""  
- [Python Official Docs](https://docs.python.org/3/)  
- [Streamlit Docs](https://docs.streamlit.io/)  
""")  
# Sidebar image placeholder - BAM Coding Program logo  
  
# Ending note  
#st.markdown("""Ready to move on? Head over to the next section to continue learning!  """)  
