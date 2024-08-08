import streamlit as st  
  
# Title of the Streamlit page  
st.title("Learn Python Lists with Interactive Selectbox")  
  
# Tabs for different sections  
tab1, tab2, tab3 = st.tabs(["Introduction", "Examples", "Practice"])  
  
# Introduction Tab  
with tab1:  
    st.header("Introduction to Python Lists")  
      
    with st.expander("What is a Python List?",expanded=True):  
        st.write("""  
        A **list** in Python is a data structure in which values can be stored and accessed.   
        The neat thing about lists is that they do not all need to be the same data type.   
        For example, you can have a list containing a string, an integer, and a float:  
        ```python  
        my_list = ['potato', 3, 4.02]  
        ```  
        You can access list items by their index:  
        ```python  
        my_list[0]  
        ```  
        This will return `'potato'`.  
        """)  
  
    with st.expander("Key Points about Lists",expanded=True):  
        st.write("""  
        - **Lists** are created using square brackets `[]`.  
        - **Lists** are ordered, meaning items have a defined order, and that order will not change.  
        - **Lists** are mutable, so you can change, add, and remove items after the list has been created.  
        - **Lists** can contain items of any data type.  
        - **Lists** allow duplicate elements.  
        """)  
  
# Examples Tab  
with tab2:  
    st.header("Examples of Python Lists")  
  
    # Example 1  
    with st.expander("Example 1: Creating and Accessing Lists",expanded=True):  
        st.write("Select an option from the dropdown to see an example of creating and accessing lists.")  
          
        example1 = st.selectbox("Choose an example:", ["Create List", "Access List"])  
          
        if example1 == "Create List":  
            st.write("""  
            Creating a list:  
            ```python  
            my_list = [1, 2, 3, 4, 5]  
            ```  
            This creates a list with the elements 1, 2, 3, 4, and 5.  
            """)  
          
        elif example1 == "Access List":  
            st.write("""  
            Accessing list items:  
            ```python  
            my_list = [1, 2, 3, 4, 5]  
            print(my_list[0])  # Output: 1  
            print(my_list[2])  # Output: 3  
            ```  
            This accesses the first and third elements of the list.  
            """)  
  
    # Example 2  
    with st.expander("Example 2: Modifying Lists"):  
        st.write("Select an option from the dropdown to see an example of modifying lists.")  
          
        example2 = st.selectbox("Choose an example:", ["Add Item", "Remove Item", "Change Item"])  
          
        if example2 == "Add Item":  
            st.write("""  
            Adding an item to the list:  
            ```python  
            my_list = [1, 2, 3, 4, 5]  
            my_list.append(6)  
            print(my_list)  # Output: [1, 2, 3, 4, 5, 6]  
            ```  
            This adds the element 6 to the end of the list.  
            """)  
  
        elif example2 == "Remove Item":  
            st.write("""  
            Removing an item from the list:  
            ```python  
            my_list = [1, 2, 3, 4, 5]  
            my_list.remove(3)  
            print(my_list)  # Output: [1, 2, 4, 5]  
            ```  
            This removes the first occurrence of the element 3 from the list.  
            """)  
  
        elif example2 == "Change Item":  
            st.write("""  
            Changing an item in the list:  
            ```python  
            my_list = [1, 2, 3, 4, 5]  
            my_list[2] = 10  
            print(my_list)  # Output: [1, 2, 10, 4, 5]  
            ```  
            This changes the third element of the list to 10.  
            """)  
  
# Practice Tab  
with tab3:  
    st.header("Practice with Python Lists")  
  
    with st.expander("Try It Yourself",expanded=True):  
        st.write("""  
        Let's practice adding items to a list! Use the dropdown to choose an item to add to the list, and click the button to see the result.  
        """)  
          
        items = st.selectbox("Choose an item to add to the list:", ["Apple", "Banana", "Cherry"])  
        button = st.button("Add to List")  
          
        if button:  
            my_list = ["Orange", "Grapes"]  
            my_list.append(items)  
            st.write(f"Updated list: {my_list}")  
  
