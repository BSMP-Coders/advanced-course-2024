from openai import AzureOpenAI  
import os
import dotenv  
  
# Load environment variables  
dotenv.load_dotenv()  
  
# Get the keys and variables from environment  
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT_BSMP24")  
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY_BSMP24")  
MODEL_NAME = 'tts'  # Model name for TTS  
  
# Initialize the AzureOpenAI client  
openai_client = AzureOpenAI(api_key=AZURE_OPENAI_API_KEY, azure_endpoint=AZURE_OPENAI_ENDPOINT, api_version="2024-02-15-preview")  
  
# Define the data payload  
data = {  
    "model": MODEL_NAME,  
    "input": "I'm excited to try text to speech.",  
    "voice": "alloy"  
}  

 
# Make the request to the AzureOpenAI endpoint  
# Producing text-to-speech
response = openai_client.audio.speech.create(
    model = MODEL_NAME,
    voice = "alloy",
    input = "Menu options include vegetarian lasagna, beef bourguignon, and pan-seared salmon."
)
# Saving TTS output to file
response.write_to_file('speech_client.mp3')