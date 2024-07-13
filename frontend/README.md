# Frontend - Data Handler

## Overview
This is the frontend service for the Data Handler project. It is built with React and provides a user interface for interacting with the backend APIs for tabular data, RGB images, and textual data.

## Features
- **Tabular Data**: Upload, view, edit, delete, and visualize data.
- **RGB Images**: Upload images, view histograms, perform image manipulations.
- **Textual Data**: Upload text and perform various text analyses.

## Installation

### Prerequisites
- Node.js (version 14+)
- Docker

### Local Setup
1. Navigate to the frontend directory:
    ```sh
    cd frontend
    ```

2. Install dependencies:
    ```sh
    npm install
    ```

3. Start the application:
    ```sh
    npm start
    ```

The frontend will start at `http://localhost:3000`.

## Running with Docker
1. Build and run the Docker container:
    ```sh
    docker build -t data-handler-frontend .
    docker run -p 3000:3000 data-handler-frontend
    ```