import streamlit as st  
import random  
  
# Initialize game state  
if 'deck' not in st.session_state:  
    st.session_state.deck = [f'{color} {number}' for color in ['Red', 'Green', 'Blue', 'Yellow'] for number in range(1, 10)]  
    random.shuffle(st.session_state.deck)  
    st.session_state.player_hand = [st.session_state.deck.pop() for _ in range(5)]  
    st.session_state.computer_hand = [st.session_state.deck.pop() for _ in range(5)]  
    st.session_state.current_card = st.session_state.deck.pop()  
    st.session_state.turn = 'player'  
  
st.title('UNO Card Game')  
  
# Display current state  
st.write(f'Current card: {st.session_state.current_card}')  
st.write(f'Your hand: {st.session_state.player_hand}')  
  
# Player's turn  
if st.session_state.turn == 'player':  
    selected_card = st.selectbox('Select a card to play:', st.session_state.player_hand + ['Draw card'])  
  
    if st.button('Play'):  
        if selected_card == 'Draw card':  
            st.session_state.player_hand.append(st.session_state.deck.pop())  
        elif selected_card.split()[0] == st.session_state.current_card.split()[0] or selected_card.split()[1] == st.session_state.current_card.split()[1]:  
            st.session_state.current_card = selected_card  
            st.session_state.player_hand.remove(selected_card)  
            st.session_state.turn = 'computer'  
  
# Computer's turn  
if st.session_state.turn == 'computer':  
    for card in st.session_state.computer_hand:  
        if card.split()[0] == st.session_state.current_card.split()[0] or card.split()[1] == st.session_state.current_card.split()[1]:  
            st.session_state.current_card = card  
            st.session_state.computer_hand.remove(card)  
            st.session_state.turn = 'player'  
            break  
    else:  
        st.session_state.computer_hand.append(st.session_state.deck.pop())  
        st.session_state.turn = 'player'  
  
# Check for win  
if len(st.session_state.player_hand) == 0:  
    st.write('You win!')  
elif len(st.session_state.computer_hand) == 0:  
    st.write('Computer wins!')  
  
# Display deck and hands for debugging purposes  
st.write(f'Deck: {len(st.session_state.deck)} cards remaining')  
st.write(f'Computer hand: {st.session_state.computer_hand}')  
