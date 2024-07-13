# Backend - Data Handler

## Overview
This is the backend service for the Data Handler project. It is built with Python and Flask and provides APIs for handling tabular data, RGB images, and textual data.

## Features
- **Tabular Data**: Endpoints for CRUD operations, complex queries, and statistical computations.
- **RGB Images**: Endpoints for image upload, color histogram generation, image manipulation.
- **Textual Data**: Endpoints for text summarization, keyword extraction, sentiment analysis.

## Installation

### Prerequisites
- Python 3.8+
- Docker

### Local Setup
1. Navigate to the backend directory:
    ```sh
    cd backend
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    flask run
    ```

The backend server will start at `http://127.0.0.1:5000`.

## Running with Docker
1. Build and run the Docker container:
    ```sh
    docker build -t data-handler-backend .
    docker run -p 5000:5000 data-handler-backend
    ```
