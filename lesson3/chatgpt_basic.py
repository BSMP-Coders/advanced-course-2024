import os  
import dotenv  
from openai import AzureOpenAI  
  
# Load environment variables  
dotenv.load_dotenv()  
AOAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")  
AOAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")  
  
# Set up the Azure OpenAI client  
client = AzureOpenAI(api_key=AOAI_KEY, azure_endpoint=AOAI_ENDPOINT, api_version="2024-05-01-preview")  
  
# Example 1: Simple user query  
response = client.chat.completions.create(model="gpt-35-turbo",  
                                          messages=[{"role": "user", "content": "What is the capital of France?"}])  
print(response.choices[0].message.content)  
  
# Example 2: System message to set behavior  
response = client.chat.completions.create(model="gpt-35-turbo",  
                                          messages=[  
                                              {"role": "system", "content": "You are a helpful assistant. Answer the question in both English and French."},  
                                              {"role": "user", "content": "What is the capital of France?"}  
                                          ])  
print(response.choices[0].message.content)  
  
# Example 3: Extended conversation  
response = client.chat.completions.create(model="gpt-35-turbo",  
                                          messages=[  
                                              {"role": "system", "content": "You are a helpful assistant."},  
                                              {"role": "user", "content": "Who was the first president of the USA?"},  
                                              {"role": "assistant", "content": "The first president of the United States was George Washington."},  
                                              {"role": "user", "content": "When was he president?"}  
                                          ])  
print(response.choices[0].message.content)  
  
# Function to generate responses  
def generate_response(prompt, model="gpt-35-turbo"):  
    response = client.chat.completions.create(  
        model=model,  
        messages=[{"role": "user", "content": prompt}]  
    )  
    return response.choices[0].message.content  
  
# Example usage of the function  
#print(generate_response("Who is the quarterback for the Dallas Cowboys?"))  
