# Data Processing Microservice

## Introduction

This project provides a data processing microservice that accepts text queries, sends them to an AI model, and returns structured data in JSON format.

## Requirements

- Docker
- OpenAI API Key

## Setup and Usage

1. **Clone the repository**:

    ```sh
    git clone https://github.com/Michailbul/Granton-microservice
    ```

2. **Set your OpenAI API key**:
   
   Create a file named `.env` in the root directory of the project with the following content:

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

3. **Build the Docker image**:

    ```sh
    docker build -t microservice .

    ```

4. **Run the Docker container**:

    ```sh
    docker run --env-file .env -p 8000:8000 microservice

    ```

5. **Access the API**:

    - Open your browser and go to `http://localhost:8000/docs` to access the Swagger UI.
    - Use `curl` or any other HTTP client to interact with the API.

## Example API Requests

**Using `curl`**:

- **POST /process**:
    ```sh
    curl -X POST "http://localhost:8000/process" -H "Content-Type: application/json" -d '{"text": "Pikachu"}'
    ```

## Running Tests

To run the tests using `pytest`, follow these steps:

1. **Ensure you have pytest installed**:

    ```sh
    pip install pytest
    ```

2. **Run the tests**:

    ```sh
    pytest app/test_main.py
    ```
