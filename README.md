# Anviro: A FastAPI application for text extraction and summarization

This repository contains a FastAPI application that provides endpoints for extracting text from URLs and summarizing the extracted text using advanced language models. The application leverages libraries such as BeautifulSoup for web scraping, Hugging Face Transformers for text summarization, and SpaCy for Named Entity Recognition (NER).

## Features
- Named Entity Recognition (NER) to identify and extract entities from text.
- Summarize the extracted text using Gemini.
- FastAPI endpoints for easy integration and usage.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Yasirrazaa/anviro.git
2. Navigate to the project directory:
   ```bash
    cd anviro

3. Install the required dependencies:
   ```bash
   pip install uv
   uv sync
4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Gemini API key:
     ```env
     GEMINI_API_KEY=your_gemini_api_key_here

     ```

## Usage
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
2. Access the API documentation at `http://localhost:8000/docs` to explore the available endpoints and test the functionality.

## Deployment
Deploy simply using Docker. Build the Docker image and run the container:
```bash
docker build -t anviro .
docker run -d -p 8000:8000 anviro
```