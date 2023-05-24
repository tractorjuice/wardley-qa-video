# Wardley Mapping Question & Answer with Simon Wardley Videos
This repository contains an application that utilizes AI-powered language models to provide responses and queries about the video "Intro To Wardley Mapping." It leverages the OpenAI GPT model and the LLama Index library for efficient searching and indexing of text data.

This is a Python script that scrapes the transcription from a YouTube video and builds a vector database for querying via OpenAI. The script makes use of several key libraries and modules, including openai, streamlit, llama_index, and gpt_index.

[![Twitter Follow](https://img.shields.io/twitter/follow/mcraddock?style=social)](https://twitter.com/mcraddock)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://wardley-video-chat.streamlit.app/)

## Features
Query the video content using AI-powered language models.
Retrieve relevant information and responses based on user prompts.
Display the video for reference and context.
Generate dynamic responses and messages based on user input.

## Installation
To run the application, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/wardley-mapping-ai.git
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the application:

bash
Copy code
streamlit run app.py
Access the application through your web browser using the provided URL (typically http://localhost:8501).

On the main page, you will see the video "Intro To Wardley Mapping."

Enter your prompt or question in the text input field.

Click the "Send" button to generate a response based on your input.

The application will utilize the OpenAI GPT model and the LLama Index library to search and provide relevant information based on your prompt.

The response will be displayed in the message area below the text input field.

To clear the prompt and response, click the "Clear" button.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## Acknowledgements
The LLama Index library (imported as llama_index) is used for efficient text indexing and querying.
The OpenAI GPT model is utilized for generating dynamic responses and messages.
This application is developed by Mark Craddock.
Please note that the OpenAI API key is required to run the application, and it should be provided as an environment variable or using a secrets management system.

Feel free to explore the code and adapt it to your needs. Enjoy your journey into Wardley Mapping with AI!
