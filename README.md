# Codebro Chatbot

Codebro Chatbot is a simple AI chatbot web app built with **Python**, **Streamlit**, and the **OpenAI API**.

The project includes a chat interface, conversation memory, a custom system prompt, and web search support using OpenAI’s built-in web search tool.

## About This Project

I built this project as part of my journey toward becoming an **AI Engineer**.

The goal was to create a working AI chatbot from scratch, understand how the different parts connect together, and practice building a real AI-powered application instead of only watching tutorials.

This project helped me practice:

- Building a web app with Streamlit
- Connecting Python to the OpenAI API
- Managing API keys safely with environment variables
- Creating a custom chatbot personality using a system prompt
- Saving and loading chat history with JSON
- Adding web search so the chatbot can answer with more up-to-date information
- Structuring a small AI project in a clean and understandable way

The code was written manually by me as a learning project.

## Features

- AI chatbot powered by the OpenAI API
- Streamlit-based web interface
- Chat memory saved in `history.json`
- Loads previous conversations when the app starts
- Supports web search through OpenAI’s `web_search` tool
- Uses a custom system prompt to control the chatbot’s behavior
- Environment variable support using `.env`
- Simple project structure for beginners learning AI engineering

## How It Works

The app runs through Streamlit and displays a simple chat interface.

When the user sends a message, the app sends the conversation to the OpenAI API. The chatbot then responds based on:

1. The system prompt
2. The current user message
3. The saved chat history
4. Web search results, when needed

The conversation is saved locally in a JSON file so the chatbot can remember the previous messages.

## Project Structure

```text
codebro-chatbot/
│
├── app.py              # Main Streamlit app
├── history.json        # Stores chat history
├── requirements.txt    # Python dependencies
├── .env                # Stores the OpenAI API key
└── README.md           # Project documentation
