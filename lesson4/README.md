# Lesson 4: Introduction to Flask and Building Flask Web Apps
Welcome to your next adventure in web development! So far, you've been building web apps using Streamlit. Now, we're going to explore Flask, another powerful tool for creating web applications. This guide will help you understand the differences between Streamlit and Flask and get you started with Flask basics.


## Lesson Overview
In this lesson, you'll learn the basics of Flask, a web framework for Python. We'll cover the following:

1. **Introduction to Flask Basics**
2. **Creating a Simple Flask Application**
3. **Building a Flappy Bird Game Using Flask and GitHub Copilot**


## What's the Difference Between Streamlit and Flask?

### Streamlit:
- **Purpose**: Streamlit is designed for quickly building interactive web apps for data science and machine learning.
- **Ease of Use**: It's very easy to use and you can create apps with just a few lines of Python code.
- **Features**: Streamlit takes care of most of the web development for you. It automatically handles the front end (what users see) and the back end (the logic and data processing).

### Flask:
- **Purpose**: Flask is a web framework used to build more general web applications. It gives you more control over your app's structure and behavior.
- **Flexibility**: Flask requires more setup and code, but it also gives you more flexibility and control.
- **Client-Server Model**: Flask follows a client-server model, where the client (browser) makes requests to the server (your Flask app) which processes these requests and sends back responses (like web pages or data).


#### 1. Introduction to Flask  
**Objective:** Understand what Flask is and how it functions within the client-server model.  
   
**What is Flask?**  
- Flask is a lightweight web framework for Python, allowing you to build web applications quickly and with minimal setup.  
- It’s particularly useful for creating simple, yet powerful web services and APIs.  

![](https://image.slidesharecdn.com/pythonflaskpresentation-rohit-191028114913/75/Python-Flask-Presentation-2-2048.jpg)

**Client-Server Model:**  
- **Server:** The server runs the Flask application. It listens for requests from clients, processes them, and sends back responses.  
- **Client:** The client makes requests to the server and waits for responses. This can be a web browser, a mobile app, or another program.  


## Getting Started with Flask

### Basic Concepts

- **Client**: The client is what the user interacts with, usually a web browser.
- **Server**: The server processes requests from the client and sends back responses. In Flask, you'll write Python code to define how the server handles these requests.
- **Routes**: Routes in Flask are like addresses that point to different parts of your web app. Each route is associated with a specific function in your code that defines what should happen when someone visits that route.

### Setting Up Flask

1. **Install Flask**:
   Open your terminal or command prompt and run:
   ```bash
   pip install flask
   ```

2. **Create a Simple Flask App**:
   Create a new file called `app.py` and add the following code:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Hello, Flask!"

   if __name__ == '__main__':
       app.run(debug=True)
   ```

3. **Run Your Flask App**:
   In your terminal or command prompt, navigate to the directory where `app.py` is located and run:
   ```bash
   python app.py
   ```
   Open your web browser and go to `http://127.0.0.1:5000/` to see your app in action.

### Flask vs. Streamlit: Key Differences

- **Code Structure**:
  - Streamlit: You write your code in a linear fashion, similar to writing a script.
  - Flask: You define routes and functions to handle different parts of your app, similar to setting up a series of addresses and instructions for each address.

- **Flexibility**:
  - Streamlit: Quick and easy for data apps but less flexible for general web development.
  - Flask: More setup required but provides greater flexibility for building various types of web applications.


## Sections

### 1. Basic Flask Setup

First, let's set up our Flask application:

```python
from flask import Flask
import random

app = Flask(__name__)
```

Here, we import Flask and create an instance of the `Flask` class. This instance will be our web application.

### 2. Creating Routes

Routes are the different URLs that our application can respond to. Each route is associated with a function that returns the response for that URL.

#### Home Route

```python
@app.route('/')
def home():
    print("> using the home route")
    message = "This is our BSMP Flask HOMEPAGE!"
    return message 
```

The `@app.route('/')` decorator creates a route for the home page (`127.0.0.1:5000/`). The function `home()` returns a simple message.

#### Hello Route

```python
@app.route('/hello')
def hello():
    print("> using the hello route")
    message = "HELLO!!!"
    return message
```

The `/hello` route returns a greeting message.

#### Number Route

```python
@app.route('/number')
def number():
    print("> using the number route")
    message = "Here's a random number: {0}"
    num = random.randint(1, 25)
    return message.format(num)
```

This route generates and returns a random number between 1 and 25.

### 3. HTML Templates

We can also return HTML content from our routes. 

#### Number with HTML

```python
@app.route('/number2')
def number2():
    print("> using the number2 route")
    page = """
        <h1>Here's a random number: {0}</h1>
        <form>
            <button>New Number</button>
        </form>
    """
    num = random.randint(1, 25)
    return page.format(num)
```

This route returns HTML content with a random number and a button.

### 4. Dynamic Content

We can create routes that return different responses based on the URL.

#### Name Routes

```python
@app.route('/name')
def name():
    return "My Name is: Phillip Hale"

@app.route('/name/first')
def firstname():
    return "Phillip"

@app.route('/name/last')
def lastname():
    return "Hale"

@app.route('/name/full')
def fullname():
    first_name = firstname()
    last_name = lastname()
    return f"{first_name} {last_name}"
```

These routes return different parts of a name.

### 5. API Integration

We can also integrate external APIs into our Flask application.

#### Meme Generator

```python
import requests

def get_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    return response.json()['url']

@app.route('/meme')
def meme():
    meme_url = get_meme()
    return f'<img src="{meme_url}" alt="Meme" style="max-width: 100%; height: auto;">'
```

This route fetches a random meme from an external API and displays it.

### 6. HTML Forms

We can handle form submissions in Flask.

#### User Information Form

```python
from flask import render_template, request

@app.route('/user', methods=['GET', 'POST'])
def user_info():
    user_data = None
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        city = request.form['city']
        user_data = {'name': name, 'age': age, 'city': city}
    return render_template('simple_form.html', user_data=user_data)
```

This route displays a form and handles form submissions. The form template is `simple_form.html`.

### Templates

#### `home.html`

```html
<!DOCTYPE html>
<html>
    <head>
        <title>BSMP Flask Homepage</title>
    </head>
    <body>
        <h1>{{ message }}</h1>
        <p>Click <a href="/user">here</a> to enter your details.</p>
    </body>
</html>
```

#### `simple_form.html`

```html
<!DOCTYPE html>
<html>
<head>
  <title>User Information</title>
</head>
<body>
    <p>Click <a href="/">here</a> to go back Homepage.</p>
  {% if user_data %}
    <h1>Thank You!</h1>
    <p>Hello, {{ user_data['name'] }}! You are {{ user_data['age'] }} years old and live in {{ user_data['city'] }}.</p>
  {% else %}
    <h1>Enter Your Details</h1>
    <form action="/user" method="POST">
      <label for="name">Name:</label>
      <input type="text" name="name" id="name" required><br>
      <label for="age">Age:</label>
      <input type="number" name="age" id="age" required><br>
      <label for="city">City:</label>
      <input type="text" name="city" id="city" required><br>
      <button type="submit">Submit</button>
    </form>
  {% endif %}
</body>
</html>
```

### Blueprints

For larger applications, we can organize our routes using blueprints.

#### `meme_app.py`

```python
from flask import Blueprint
import requests

meme_bp = Blueprint('meme_bp', __name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    return response.json()['url']

@meme_bp.route('/meme2')
def meme():
    print("running meme generator from demos/meme_app.py")
    meme_url = get_meme()
    return f'<img src="{meme_url}" alt="Meme" style="max-width: 100%; height: auto;">'
```

### Activities

1. **Create a New Route**
   - Create a new route that returns a personalized message.

2. **Modify HTML Content**
   - Modify the `/number2` route to include more HTML content.

3. **Dynamic Route**
   - Create a route that returns a random joke or fact.

4. **API Integration**
   - Integrate a different public API and display its data.

5. **Form Handling**
   - Create a new form that collects different user information and displays it.

----