import streamlit as st        
import random        
    
# Initialize variables for each character's characteristics      
alex_hair = 'brown'      
alex_earrings = 'no'      
alex_image = "https://img.buzzfeed.com/buzzfeed-static/static/2016-12/27/2/asset/buzzfeed-prod-web-14/sub-buzz-25745-1482823329-1.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto"    
      
susan_hair = 'blonde'      
susan_earrings = 'yes'      
susan_image = "https://img.buzzfeed.com/buzzfeed-static/static/2016-12/27/2/asset/buzzfeed-prod-web-15/sub-buzz-7240-1482824615-1.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto"    

# Initialize game state      
if 'characters' not in st.session_state:        
    st.session_state.characters = ['Alex', 'Susan']      
    st.session_state.selected_character = random.choice(st.session_state.characters)      
    st.session_state.guesses = []        
    st.session_state.message = "Ask a question or make a guess!"        
    
# Create a reset button that sets the counter to 0        
if st.button("Reset characters"):        
    st.session_state.characters = ['Alex', 'Susan']      
    st.session_state.selected_character = random.choice(st.session_state.characters)      
    st.session_state.guesses = []        
    st.session_state.message = "Ask a question or make a guess!"        
    
st.title('Guess Who?')     
# Display instructions and current state        
st.write("Try to guess the selected character by asking yes/no questions.")        
st.write("Characters: Alex, Susan")    
st.write("Characteristics: brown hair, blonde hair, earrings")    
st.markdown(f"Guesses: {st.session_state.guesses}", unsafe_allow_html=True)    


# Organize layout into columns
col1, col2 = st.columns(2)

with col1:
    # User input for questions        
    question = st.selectbox('Ask a question:',['Is the hair brown?','Is the hair blonde?','Are there earrings?'])    

    # Answering questions based on selection    
    if question:    
        if st.session_state.selected_character == 'Alex':      
            if question == 'Is the hair brown?':        
                if alex_hair == 'brown':
                    st.session_state.message = "Yes, the hair is brown." 
                else:
                    st.session_state.message = "No, the hair is not brown."      
            elif question == 'Are there earrings?':        
                if alex_earrings == 'yes':
                    st.session_state.message = "Yes, there are earrings." 
                else:
                    st.session_state.message = "No, there are no earrings."      
        elif st.session_state.selected_character == 'Susan':      
            if question == 'Is the hair blonde?':        
                if susan_hair == 'blonde':        
                    st.session_state.message = "Yes, the hair is blonde."
                else: 
                    "No, the hair is not blonde."      
            elif question == 'Are there earrings?':        
                st.session_state.message = "Yes, there are earrings." if susan_earrings == 'yes' else "No, there are no earrings."    
    # Display the message    
    st.write(st.session_state.message)    
      
with col2:
    # User input for making a guess    
    guess = st.selectbox('Make a guess:', [''] + st.session_state.characters)    
    if st.button('Guess'):    
        if guess == st.session_state.selected_character:        
            st.success(f"Correct! The character was {guess}.")    
            if guess == 'Alex':      
                st.image(alex_image)      
            elif guess == 'Susan':      
                st.image(susan_image)      
        else:        
            st.error(f"Wrong! The character is not {guess}.")        
            st.session_state.guesses.append(guess)      
    


st.sidebar.header("Guess Who? Characters")   
st.sidebar.image("images/guess-who-characters-full-belly-laughs.jpg",)
st.sidebar.caption("Guess Who? Characters - A list of all the characters in the classic board game Guess Who?")
st.sidebar.info("inspired by: https://fullbellylaughs.com/guess-who-board-games-characters")
st.sidebar.divider()
st.sidebar.markdown("got the character imaged from [bussfeed](https://www.buzzfeed.com/arivoukydis/guess-who-dot-dot-dot-is-hiding-something)")