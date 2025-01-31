# FastAPI Task Management API

This is a simple FastAPI-based Task Management API that allows you to create, read, update, and delete tasks. The API is versioned, with two versions (v1 and v2) available. Each version has its own set of endpoints for managing tasks.

## Features
Versioned API: Two versions of the API (v1 and v2) are available, each with its own set of endpoints.

Task Management: Create, read, update, and delete tasks.

API Key Authentication: Secure your API endpoints with an API key.

In-Memory Database: Tasks are stored in an in-memory list for simplicity.

## Prerequisites
Python 3.7 or higher

FastAPI

Uvicorn (for running the server)

python-dotenv (for loading environment variables)

## Installation
## Clone the repository:

``` bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

## Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Install dependencies:

```bash
pip install fastapi uvicorn python-dotenv
```

## Set up environment variables:
Create a .env file in the root directory and add your API key:

```env
LAB4_API_KEY=your_api_key_here
```

## Running the API
To run the API, use the following command:

```bash
uvicorn main:app --reload
```
The API will be available at http://127.0.0.1:8000.

# API Endpoints
## Root Endpoint
GET /: Welcome message.

```json
{
  "message": "Welcome! Use /apiv1 or /apiv2 for versioned API access."
}
```

## Health Check
GET /health: Check if the API is running.

```json
{
  "status": "API is up and running"
}
```

## Version 1 Endpoints (/apiv1)
GET /apiv1/{task_id}: Retrieve a task by its ID.

## POST /apiv1/: Create a new task.

## PATCH /apiv1/{task_id}: Update an existing task by its ID.

## DELETE /apiv1/{task_id}: Delete a task by its ID.

## Version 2 Endpoints (/apiv2)
## GET /apiv2/{task_id}: Retrieve a task by its ID.

## POST /apiv2/: Create a new task.

## PATCH /apiv2/{task_id}: Update an existing task by its ID.

## DELETE /apiv2/{task_id}: Delete a task by its ID.

## Authentication
All endpoints require an API key for authentication. The API key can be passed either as a query parameter (G-C-P-KEY) or in the request headers (G-C-P-KEY).

Example using query parameter:

```
GET /apiv1/1?G-C-P-KEY=your_api_key_here
```
Example using headers:


```bash
curl -X GET "http://127.0.0.1:8000/apiv1/1" -H "G-C-P-KEY: your_api_key_here"
```

## Example Requests
## Create a Task (v1)
```bash
curl -X POST "http://127.0.0.1:8000/apiv1/" -H "G-C-P-KEY: your_api_key_here" -H "Content-Type: application/json" -d '{"title": "New Task", "description": "This is a new task", "completed": false}'
```
## Retrieve a Task (v2)
```bash
curl -X GET "http://127.0.0.1:8000/apiv2/1" -H "G-C-P-KEY: your_api_key_here"
```
## Update a Task (v1)
```bash
curl -X PATCH "http://127.0.0.1:8000/apiv1/1" -H "G-C-P-KEY: your_api_key_here" -H "Content-Type: application/json" -d '{"completed": true}'
```
##Delete a Task (v2)
```bash
curl -X DELETE "http://127.0.0.1:8000/apiv2/1" -H "G-C-P-KEY: your_api_key_here"
```
## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests.

## License

