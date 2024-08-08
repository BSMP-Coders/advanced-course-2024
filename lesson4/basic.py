# python app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"



from demos.meme_app import meme_bp  
# Register the blueprint  
app.register_blueprint(meme_bp) 

if __name__ == '__main__':
    app.run(debug=True)