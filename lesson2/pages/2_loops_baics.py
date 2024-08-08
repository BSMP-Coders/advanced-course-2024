#modify the layout to display the Streamlit code at the bottom of each interactive section when the "Show Code" button is pressed. This way, students can first interact with the elements and then view the code below.
import streamlit as st  
  
# Title of the Streamlit page  
st.title("Learn Python Loops with Interactive Sliders")  
  
# Tabs for different sections  
tab1, tab2, tab3 = st.tabs(["Introduction", "Examples", "Practice"])  
  
# Introduction Tab  
with tab1:  
    st.header("Introduction to Loops in Python")  
  
    with st.expander("What is a Loop?", expanded=True):  
        st.write("""  
            **Loops** allow us to execute a block of code multiple times.   
            There are two main types of loops in Python:  
            - **For Loops**: Used for iterating over a sequence (like a list, tuple, dictionary, set, or string).  
            - **While Loops**: Repeat as long as a condition is true.  
        """)  
  
    with st.expander("Key Points about Loops", expanded=True):  
        st.write("""  
            - **For Loops**:  
              - Use when you know the number of iterations.  
              - Syntax:  
              ```python  
              for item in sequence:  
                  # code block  
              ```  
            - **While Loops**:  
              - Use when the number of iterations is not known and depends on a condition.  
              - Syntax:  
              ```python  
              while condition:  
                  # code block  
              ```  
        """)  
  
# Examples Tab  
with tab2:  
    st.header("Examples of Loops")  
  
    # Example 1: For Loop  
    with st.expander("Example 1: For Loop", expanded=True):  
        st.write("A `for` loop that prints numbers from 0 to 4:")  
        st.code("""  
        for i in range(5):  
            print(i)  
        """)  
  
        st.write("Try it out:")  
        for_loop_range = st.slider("Select range for loop:", min_value=1, max_value=10, value=5)  
        st.write("Loop Output:")  
        for i in range(for_loop_range):  
            st.write(i)  
  
        show_code_for_loop = st.button("Show Streamlit Code for For Loop")  
        if show_code_for_loop:  
            st.code("""  
import streamlit as st  
  
for_loop_range = st.slider("Select range for loop:", min_value=1, max_value=10, value=5)  
st.write("Loop Output:")  
for i in range(for_loop_range):  
    st.write(i)  
            """, language='python')  
  
    # Example 2: While Loop  
    with st.expander("Example 2: While Loop", expanded=True):  
        st.write("A `while` loop that prints numbers from 0 to 4:")  
        st.code("""  
        count = 0  
        while count < 5:  
            print(count)  
            count += 1  
        """)  
  
        st.write("Try it out:")  
        while_loop_limit = st.slider("Select limit for while loop:", min_value=1, max_value=10, value=5)  
        count = 0  
        st.write("Loop Output:")  
        while count < while_loop_limit:  
            st.write(count)  
            count += 1  
  
        show_code_while_loop = st.button("Show Streamlit Code for While Loop")  
        if show_code_while_loop:  
            st.code("""  
import streamlit as st  
  
while_loop_limit = st.slider("Select limit for while loop:", min_value=1, max_value=10, value=5)  
count = 0  
st.write("Loop Output:")  
while count < while_loop_limit:  
    st.write(count)  
    count += 1  
            """, language='python')  
  
# Practice Tab  
with tab3:  
    st.header("Practice with Loops")  
  
    with st.expander("Try It Yourself", expanded=True):  
        st.write("""  
            Let's practice using loops! Choose the type of loop and the range/limit, and observe the output.  
        """)  
  
        loop_type = st.selectbox("Choose loop type:", ["For Loop", "While Loop"])  
  
        if loop_type == "For Loop":  
            st.write("You selected a For Loop.")  
            for_loop_range_practice = st.slider("Select range for for loop:", min_value=1, max_value=20, value=5)  
            st.write("Loop Output:")  
            for i in range(for_loop_range_practice):  
                st.write(i)  
  
            show_code_practice_for = st.button("Show Streamlit Code for Practice For Loop")  
            if show_code_practice_for:  
                st.code(f"""  
import streamlit as st  
  
for_loop_range_practice = st.slider("Select range for for loop:", min_value=1, max_value=20, value=5)  
st.write("Loop Output:")  
for i in range(for_loop_range_practice):  
    st.write(i)  
                """, language='python')  
  
        elif loop_type == "While Loop":  
            st.write("You selected a While Loop.")  
            while_loop_limit_practice = st.slider("Select limit for while loop:", min_value=1, max_value=20, value=5)  
            count_practice = 0  
            st.write("Loop Output:")  
            while count_practice < while_loop_limit_practice:  
                st.write(count_practice)  
                count_practice += 1  
  
            show_code_practice_while = st.button("Show Streamlit Code for Practice While Loop")  
            if show_code_practice_while:  
                st.code(f"""  
import streamlit as st  
  
while_loop_limit_practice = st.slider("Select limit for while loop:", min_value=1, max_value=20, value=5)  
count_practice = 0  
st.write("Loop Output:")  
while count_practice < {while_loop_limit_practice}:  
    st.write(count_practice)  
    count_practice += 1  
                """, language='python')  
