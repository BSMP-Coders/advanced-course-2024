import streamlit as st  
  
# Main title of the page  
st.title("Lesson 2 Activities: IF Statement and Operators 📘")  
  
# Activity 1: Test Score Evaluation  
st.header("Activity 1: Test Score Evaluation")  
st.write("Enter your test scores below. If your total score is 36 or more, you've passed!")  
  
# Input fields for test scores  
test1 = st.number_input("Test Score 1 (out of 20):", min_value=0, max_value=20, value=0, step=1)  
test2 = st.number_input("Test Score 2 (out of 20):", min_value=0, max_value=20, value=0, step=1)  
test3 = st.number_input("Test Score 3 (out of 20):", min_value=0, max_value=20, value=0, step=1)  
  
# Placeholder for total score calculation  
# TODO: Calculate the total score from test1, test2, and test3  
  
# Placeholder for pass/fail logic  
# TODO: Use an IF statement to determine if the student has passed or failed  

# Activity 2: Grade Evaluation  
st.header("Activity 2: Grade Evaluation")  
st.write("Based on your scores from Activity 1, let's determine your grade.")  
  
# Placeholder for grade determination logic  
# TODO: Use IF, ELIF, and ELSE statements to determine the student's grade  
  
# Placeholder for additional conditions  
st.header("Additional Conditions")  
st.write("Let's evaluate your individual test scores with additional conditions.")  
  
# TODO: Check if any test score is below 10 and output "You have failed the exam"  
# TODO: Check if all test scores are above 10 and output "You have passed the exam"  
# TODO: Check if test2 or test3 is above 10 and output a custom message  
  
# Hint for students  
st.sidebar.subheader("Hints for Students")  
st.sidebar.markdown("""  
- Use the `st.number_input` function to get test scores from the user.  
- Calculate the total score by adding `test1`, `test2`, and `test3`.  
- Use `if`, `elif`, and `else` statements to determine the grade and print messages.  
- Use logical operators (`and`, `or`, `not`) to evaluate multiple conditions.  
- Remember to convert input values to integers before performing calculations.  
""")  
