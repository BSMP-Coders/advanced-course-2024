#📌inspired by https://github.com/Azure-Samples/simple-flask-server-appservice
from flask import Flask, render_template, request, jsonify  
from openai import AzureOpenAI  
import os  
import dotenv  
  
# Load environment variables  
dotenv.load_dotenv()  
AOAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")  
AOAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")  
MODEL_NAME = "gpt-35-turbo"  
  
# Set up the client for AI Chat  
client = AzureOpenAI(api_key=AOAI_KEY,azure_endpoint=AOAI_ENDPOINT,api_version="2024-05-01-preview")  
  
SYSTEM_MESSAGE = "You are a helpful assistant."  
  
# Function to get AI response with context  
def get_response(question, chat_history):  
    # Create the message history  
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}]  
    messages.extend(chat_history)  
    messages.append({"role": "user", "content": question})  
  
    # Get the answer using the GPT model (create 1 answer (n) and use a temperature of 0.7 to set it to be pretty creative/random)
    response = client.chat.completions.create(  
        model=MODEL_NAME,  
        temperature=0.7,  
        n=1,  
        messages=messages,  
    )  
    answer = response.choices[0].message.content  
    #print(answer)
    return answer  
  
############################################
######## THIS IS THE WEB APP CODE  #########
############################################
# Create a flask app
app = Flask(__name__, template_folder='templates', static_folder='static')  
  
# Routes  
@app.get('/')  
def index():  
    # Return a page that links to these three pages /test-ai, /ask, /chat
    return """<a href="/test-ai">Test AI</a> <br>  
              <a href="/ask">Ask</a> <br>  
              <a href="/chat">Chat</a>"""  

# This is the route that shows the form the user asks a question on
@app.get('/test-ai')  
def test_ai():  
    # Very basic form that sends a question to the /contextless-message endpoint
    return """<h1>Ask a question!</h1>  
              <form method="post" action="/test-ai">  
                  <textarea name="question" placeholder="Ask a question"></textarea>  
                  <button type="submit">Ask</button>  
              </form>"""  
  
@app.route("/test-ai", methods=["POST"])  
def ask_response():  
    # Get the question from the form
    question = request.form.get("question")  
    
    # Return the response from the AI
    return get_response(question, [])  
  
@app.route('/status', methods=['GET'])  
def a_live():  
    return "Alive!"  
  
@app.get('/ask')  
def ask():  
    return render_template("ask.html")  
  
@app.route('/contextless-message', methods=['POST'])  
def contextless_message():  
    data = request.json  
    question = data['message']  
    chat_history = data.get('context', [])  
    resp = get_response(question, chat_history)  
    return jsonify({"resp": resp})  
    #return {"resp": resp}
  
@app.route('/chat', methods=['GET', 'POST'])  
def chat():  
    if request.method == 'POST':  
        question = request.form.get("question")  
        chat_history = request.form.get("chat_history", [])  
        return get_response(question, chat_history)  
    else:  
        return render_template("chat.html")  
  
@app.errorhandler(404)  
def handle_404(e):  
    return '<h1>404</h1><p>File not found!</p><img src="https://httpcats.com/404.jpg" alt="cat in box" width=400>', 404  
  
if __name__ == '__main__':  
    app.run(debug=True)  
