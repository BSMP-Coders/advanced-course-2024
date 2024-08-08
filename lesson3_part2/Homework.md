# Homework Assignment 2: Build Your Own Streamlit Game 🎮   
  
Hello, aspiring coders! This week, we're stepping into the exciting world of game development. Your mission is to create a simple game using Streamlit that incorporates `if` statements, `for` loops, and interactive elements. This project aims to apply what you've learned in class and to get creative with coding!  
   
## Your Task 🚀   
  
Choose one of the following game ideas or feel free to invent your own:  
- **Tic-Tac-Toe**  
- **Blackjack or Other Card Game**  
- **Higher or Lower**  
- **Hangman**  
   
Your Streamlit app should include:  
1. **A Game Introduction Page**: Explain the game and its rules.  
2. **A Strategy Guide Page**: Offer tips or strategies on how to win.  
3. **A Game Play Page**: This is where the user can actually play the game.  
   
## Requirements 📝   
  
- **Lists**: Use lists to store game elements (e.g., player moves, deck of cards, the hidden word in Hangman).  
- **If Statements**: Implement `if` statements for the game's logic, like determining a winner or handling turns.  
- **For Loops** 👉 **optional**: Use `for` loops to iterate through game elements, like revealing letters in Hangman or checking win conditions in Tic-Tac-Toe.  
- **Images**: Include images to make your game more visually appealing. For example, use symbols for Tic-Tac-Toe, card images for Blackjack, or hangman images for Hangman.  
- **Input Widgets**: Add input elements like buttons, sliders, or text input for interactive gameplay.  
- **Interactive Streamlit Elements**: Get creative and use other Streamlit widgets to enhance your game's interactivity and user experience.  

## Submission 📥   
  
- **Code**: Submit your Streamlit app's by checking in the code to the repo. 
   

## Deadline 🗓️   
  
Submit your completed homework by Tuesday, July 23.  


## Additional Game Ideas 🎮

👉 see `streamlit run guess_who_demo.py` in the `guess_who` director to see an example game in streamlit, whwer we  have the person guess  who the character is, like the old **Guess Who** board game. 

![](images/guess_who_example_game_app.png)

Here are some other idea details. 

1. **Blackjack:** Write a simple version of the card game. Use a `for` loop to deal cards and `if` statements to handle the rules of the game, such as determining if a player has gone bust or has blackjack.  
   
2. **Tic Tac Toe:** Create a grid using a list of lists. Use `for` loops to iterate over the grid to check for a win condition after each turn. Use `if` statements to determine if a player has won or if a draw has occurred.  
   
3. **Higher or Lower:** Write a game where the computer randomly selects a number between 1 and 100 and the player has to guess what it is. Use a `for` loop to give the player a certain number of attempts and `if` statements to provide hints based on the player's guess (e.g., "higher" or "lower").  
   
4. **Hangman:** Choose a random word and let the player guess letters. Use a `for` loop to iterate through the word and `if` statements to check if the guessed letter is in the word. If the letter is in the word, reveal that letter; otherwise, draw a part of the hangman.  

## Tips 💡   
  
- Start simple: Get the basic functionality working before adding advanced features.  
- Test often: Run your app frequently to catch errors early.  
- Have fun: Enjoy the process of creating and playing your game!  
- here is more about session state and buttons: [Session State - Streamlit Docs](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state) + [YouTube Tutorial](http://www.youtube.com/watch?v=92jUAXBmZyU)

## Resources 🛠️   
  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)  
- [Python If Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)  
- [Python For Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)  
   
