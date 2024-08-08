# Streamlit Chat App with Hugging Face

## Introduction

This project is a simple chat application built using Streamlit and Hugging Face's transformers library. It lets users interact with an AI model in real-time, similar to applications powered by OpenAI's GPT models. In this guide, we'll explain what Hugging Face is, how it differs from OpenAI and Azure OpenAI, how to set up a Hugging Face account, and how to run the Streamlit app.

- https://huggingface.co/openai-community/gpt2
- [Welcome to the Hugging Face course](https://www.youtube.com/watch?v=00GKzGyWFEs)

## Quick Start

```sh
streamlit run app.py
```

## What is Hugging Face?

Hugging Face is a company and community that focuses on building and sharing state-of-the-art machine learning models. They are best known for their **Transformers** library, which provides access to a wide variety of pre-trained models for tasks like text generation, translation, and sentiment analysis. Hugging Face models are open-source, meaning anyone can use, modify, and share them.

### How Does Hugging Face Differ from OpenAI and Azure OpenAI?

- **OpenAI**: OpenAI develops proprietary AI models like GPT-3, which are not open-source. To use OpenAI's models, you typically need an API key and pay for the service. OpenAI's models are highly optimized and trained on large datasets, making them powerful but not customizable by users.

- **Azure OpenAI**: Azure OpenAI is a service provided by Microsoft that allows users to access OpenAI's models through Azure's platform. It integrates with other Azure services, providing additional enterprise-level features like security and scalability.

- **Hugging Face**: Hugging Face, on the other hand, provides a vast range of open-source models, which you can use for free or deploy on your infrastructure. While Hugging Face also offers a paid Inference API for easier access and additional features, the core models and tools are freely available to everyone.

## Setting Up a Hugging Face Account

To use Hugging Face's services, you might want to set up a free account, especially if you plan to use private models or the Hugging Face Inference API.

1. **Sign Up**: Go to the [Hugging Face website](https://huggingface.co) and click on "Sign Up" to create a new account.
2. **Get API Token**: Once you have an account, go to your profile settings to generate an API token. This token will be needed if you are using the Inference API or private models.

## Running the Streamlit App

### Prerequisites

1. **Python**: Ensure you have Python installed on your system (preferably version 3.7 or higher).
2. **Install Dependencies**: Install the required Python libraries using pip. You can do this by running the following command in your terminal:

   ```bash
   pip install streamlit transformers
   ```

### How to Run

1. **Clone the Repository**: Clone this repository to your local machine or download the files manually.
2. **Navigate to the Directory**: Open your terminal and navigate to the directory where the files are located.
3. **Run the Streamlit App**: Start the Streamlit app by running:

   ```bash
   streamlit run app.py
   ```

   This will launch the application in your web browser, where you can interact with the AI model.

## Explanation of the Code

### `pip install transformers`

This command installs the `transformers` library, which is the core library provided by Hugging Face. It allows you to access a wide range of pre-trained models and use them for various tasks, such as text generation, translation, and more.

### `from transformers import pipeline`

This line imports the `pipeline` function from the `transformers` library. The `pipeline` function is a high-level API that makes it easy to use models for various tasks without needing to dive deep into the underlying code.

### `pipe = pipeline("text-generation", model="openai-community/gpt2")`

This line initializes a text generation pipeline using a model from Hugging Face's repository. The model being used here is `"openai-community/gpt2"`, which is a version of the GPT-2 model shared by the community. The `pipeline` function automatically downloads the model and sets it up for use.

### Text Generation in the App

In the app, when a user inputs text, the following happens:

```python
# Use the Hugging Face pipeline to generate a response
response = pipe(user_input, max_length=150, num_return_sequences=1)[0]['generated_text']
```

- **`pipe(user_input)`**: This runs the user input through the text generation model.
- **`max_length=150`**: This parameter controls the maximum length of the generated text. The model will generate up to 150 tokens.
- **`num_return_sequences=1`**: This tells the model to return only one sequence of generated text.
- **`[0]['generated_text']`**: Since `num_return_sequences` is set to 1, the function returns a list with one item. `[0]` accesses this item, and `['generated_text']` extracts the actual text that was generated.

### Displaying the Response

The generated text (response) is then displayed in the Streamlit app as a message from the assistant. The user can interact with this model by entering text, and the model will respond in real-time.
