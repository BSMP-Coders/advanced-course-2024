import streamlit as st  
  
# This creates a text area in the sidebar for user input  
text = st.sidebar.text_area("Paste Text Here")  
  
# This line writes the user's input text to the main page  
st.write(text)   
  
# Here we create two columns on the main page  
col1, col2 = st.columns(2)  
  
# In the first column, we create an expander that can show or hide content  
col1_expander = col1.expander("Expand Original")  
  
# We create a button in the sidebar labeled "Clean Text"  
sidebarButton = st.sidebar.button("Clean Text")  
  
# When the button is clicked, the text from the sidebar is written inside the expander in column 1  
if sidebarButton:  
  with col1_expander:  
    col1_expander.write(text)  
  
# In the second column, we add a header and then display an image  
col2.header("Col 2")   
with col2:  
  st.image("./logos/dallas_cowboys_logo.png", use_column_width=True)  
