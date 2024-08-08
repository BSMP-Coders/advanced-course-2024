import streamlit as st
from openai import AzureOpenAI
import os
import dotenv
import json
import requests
from PIL import Image
from io import BytesIO

# Load environment variables
dotenv.load_dotenv()

# Set up the Azure OpenAI client
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
client2 = AzureOpenAI(api_key=AZURE_OPENAI_API_KEY, azure_endpoint=AZURE_OPENAI_ENDPOINT, api_version="2024-05-01-preview")

# Streamlit app
st.title("DALL-E 3 Image Generation")
st.write("Enter a description below to generate an image using DALL-E 3.")

# User input for the image prompt
prompt = st.text_input("Image Prompt", "kobe bryant playing chess")

# Button to generate image
if st.button("Generate Image"):
    try:
        # Generate image using the DALL-E model
        result = client2.images.generate(
            model="dalle3",  # The name of your DALL-E 3 deployment
            prompt=prompt,
            n=1
        )
        
        # Extract the image URL from the response
        image_url = json.loads(result.model_dump_json())['data'][0]['url']
        
        # Display the image URL and image
        st.write(f"Image URL: {image_url}")
        
        # Download and display the image
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption=prompt)
    except Exception as e:
        st.error(f"Error generating image: {e}")
