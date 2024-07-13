# Data Handler Project

## Overview
This project is designed to handle various types of data including tabular data, RGB images, and textual data. It features a backend developed with Python and Flask, and a frontend built with React. The application provides functionalities such as data upload, processing, analysis, and visualization.

## Features
- **Tabular Data**: Upload, process, query, and visualize tabular data.
- **RGB Images**: Upload images, generate color histograms, perform image manipulation tasks.
- **Textual Data**: Perform text analysis including summarization, keyword extraction, and sentiment analysis.

## Installation and Running

### Prerequisites
- Docker
- Docker Compose

### Steps to Run the Project
1. Clone the repository:
    ```sh
    git clone https://github.com/YassenHatem/CorporaticaDataHandler.git
    cd CorporaticaDataHandler
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

3. Open your browser and navigate to `http://localhost:3000` for the frontend.

## Project Structure
- `backend/`: Contains the Flask backend.
- `frontend/`: Contains the React frontend.