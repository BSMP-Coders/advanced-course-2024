## Text to Speech (TTS) Integration with Azure OpenAI and Streamlit

### Introduction

In this lesson, we'll explore how to use Azure OpenAI's Text to Speech (TTS) capabilities to convert text into spoken words. We'll start by understanding the basics of TTS and then implement a simple Python script (`tts_client.py`) to generate speech. Finally, we'll integrate TTS into a Streamlit app (`streamlit_app.py`) to provide a user-friendly interface for converting text to speech and playing the audio.

![](image.png)

* [Azure OpenAI Text to Speech Guide](https://platform.openai.com/docs/guides/text-to-speech/overview) 
* [Azure OpenAI Quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/text-to-speech-quickstart?tabs=command-line)

### Understanding Text to Speech (TTS)

Text to Speech (TTS) technology allows computers to read out text in a natural-sounding voice. This is useful in various applications, such as virtual assistants, accessibility tools, and more. Azure OpenAI provides an API that makes it easy to implement TTS in your projects.

### Setup and Prerequisites

1. **Azure OpenAI Account**: Ensure you have access to the Azure OpenAI API. You'll need your `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY` from your Azure portal.
2. **Environment Variables**: Store your API key and endpoint in a `.env` file to keep your credentials secure. 

### Step 1: Using TTS in Python (`tts_client.py`)

In this script, we'll use the Azure OpenAI SDK to convert text into speech and save it as an audio file.

#### Key Points:
- **Environment Setup**: Ensure the Azure OpenAI API key and endpoint are loaded from the `.env` file.
- **Text Input**: The text you want to convert into speech.
- **Voice Selection**: Choose a voice that best suits your needs.
- **Audio Output**: The script will generate an audio file (`speech_client.mp3`) containing the spoken text.

### Step 2: Integrating TTS with Streamlit (`streamlit_app.py`)

Streamlit provides an interactive interface for users to input text and listen to the generated speech.

#### Features:
- **Text Input**: Users can input the text they want to convert into speech.
- **Voice Selection**: Users can select a voice from the available options.
- **Playback**: Users can play the generated audio directly within the app.

### Running the Scripts

#### Running `tts_client.py`

1. **Update Environment Variables**: Ensure your `.env` file is properly configured with your `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT`.
2. **Execute the Script**: Run the script using the command:
   ```sh
   python tts_client.py
   ```
3. **Check Output**: The audio file `speech_client.mp3` will be created with the synthesized speech.

#### Running `streamlit_app.py`

1. **Start the Streamlit App**: Run the app with the command:
   ```sh
   streamlit run streamlit_app.py
   ```
2. **Interact with the App**: Use the Streamlit interface to input text and listen to the generated speech.

### Conclusion

This lesson provides a hands-on experience with Azure OpenAI's TTS capabilities, demonstrating how to integrate this technology into Python scripts and web applications using Streamlit. By the end of this lesson, you should have a basic understanding of how to use TTS in your projects and how to build interactive applications that utilize speech synthesis.

For more information and detailed documentation, refer to the [Azure OpenAI Text to Speech Guide](https://platform.openai.com/docs/guides/text-to-speech/overview) and [Azure OpenAI Quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/text-to-speech-quickstart?tabs=command-line).