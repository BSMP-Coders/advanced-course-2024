### 1. Recap: Lists and Loops in Python from Lesson 2  
   
In our last lesson, we explored the versatility of lists in Python. As a quick recap:  
   
- A **list** is an ordered collection of items that can be of various types, and it is one of the most commonly used data structures in Python.  
- Lists are mutable, meaning we can modify them after their creation.  
- We use the index (starting from zero) to access individual items in a list.  
   
Let's review how we can manipulate and traverse lists using different operations and loops.  
   
#### Example: Creating and Modifying a List  
   
```python  
# Recap: Creating a list with three fruits  
fruits = ["apple", "banana", "cherry"]  
   
# Recap: Appending a new fruit to the end of the list  
fruits.append("orange")  
   
# We expect the list to now be ['apple', 'banana', 'cherry', 'orange']  
print(fruits)  
```  
   
#### Example: Accessing List Items  
   
```python  
# Recap: Accessing the first item in the list using its index  
first_fruit = fruits[0]  # Indexes start at 0 in Python  
print("The first fruit is:", first_fruit)  # Output: The first fruit is: apple  
   
# Recap: Accessing the last item using negative indexing  
last_fruit = fruits[-1]  
print("The last fruit is:", last_fruit)  # Output: The last fruit is: orange  
```  
   
#### Example: Looping Over a List  
   
```python  
# Recap: Using a for loop to iterate over the list  
print("All fruits in the list:")  
for fruit in fruits:  
    print(fruit)  
      
# Expected output:  
# All fruits in the list:  
# apple  
# banana  
# cherry  
# orange  
```  
   
#### Example: List Comprehensions  
   
We can also use list comprehensions to create new lists based on existing ones.  
   
```python  
# Recap: Creating a new list with the length of each fruit's name  
fruit_lengths = [len(fruit) for fruit in fruits]  
print(fruit_lengths)  
   
# Expected output: [5, 6, 6, 6]  
# This represents the number of characters in 'apple', 'banana', 'cherry', 'orange'  
```  
   
Now that we've recapped how lists work and how we can loop through them, we'll see how these concepts apply to our upcoming lesson on Streamlit chat messages and session state. Remember, the list will hold the chat messages as dictionaries, and we'll loop over this list to display each message in the Streamlit app.



### 2. Introduction to Streamlit and Session State  
   
Introduce the students to Streamlit and the concept of session state:  
   
- Streamlit is a Python library that allows us to create web apps quickly and easily.  
- `st.session_state` is a way to store variables in the app that persist across reruns.  
   
### 3. Connecting Lists and Streamlit Session State  
   
Explain how lists can be used with `st.session_state` to store chat messages:  
   
- We create a list in the session state to hold our chat messages.  
- Each message is a dictionary with a "role" (who is sending the message) and "content" (the message text).  
- We use the list to keep track of all the messages sent during the chat session.  
   
### 4. Step-by-Step Code Explanation  
   
Now, go through the code step by step:  
   
#### Check if the list of messages exists  
   
```python  
if "messages" not in st.session_state:  
    st.session_state.messages = []  
```  
   
- Check if a list called `messages` exists in `st.session_state`.  
- If it doesn't exist, initialize it as an empty list.  
   
#### Displaying the messages  
   
```python  
for message in st.session_state.messages:  
    with st.chat_message(message["role"]):  
        st.markdown(message["content"])  
```  
   
- Loop through all the messages in the `messages` list.  
- For each message, display it using `st.chat_message()` with the role specified.  
- The message content is displayed using `st.markdown()`.  
   
#### Handling new chat input  
   
```python  
if prompt := st.chat_input("What is up?"):  
```  
   
- Use `st.chat_input()` to get input from the user.  
- If the user enters something, store it in the variable `prompt`.  
   
#### Sending a user message  
   
```python  
st.chat_message("user").markdown(prompt)  
st.session_state.messages.append({"role": "user", "content": prompt})  
```  
   
- Display the user's message.  
- Append the user's message to the `messages` list in the session state.  
   
#### Sending an assistant (bot) message  
   
```python  
response = f"Echo: {prompt}"  
st.chat_message("assistant").markdown(response)  
st.session_state.messages.append({"role": "assistant", "content": response})  
```  
   
- Create a response message by echoing back the user's input.  
- Display the assistant's message.  
- Append the assistant's message to the `messages` list in the session state.  
   