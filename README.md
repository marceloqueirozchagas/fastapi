# FastAPI Project

This project was developed as part of a study on Python and FastAPI. It is deployed on a free server and can be accessed at the following URL: [https://fastapi-n2df.onrender.com/docs.](https://fastapi-n2df.onrender.com/docs.)

## Project Overview

This project demonstrates the use of FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Features

- **FastAPI**: The core of the project, providing the API framework.
- **Deployment**: The project is deployed on Render, a platform for deploying web applications for free.

## Installation

To run this project locally, follow these steps:

1\. Clone the repository:

```python
git clone https://github.com/marceloqueiroz/fastapi.git
cd fastapi
```

2\. Create a virtual environment and activate it:

```python
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3\. Install the required packages:

```python
pip install -r requirements.txt
```

4\. Run the application:

```python
uvicorn main:app --reload
```

## Usage

Once the application is running, you can access the interactive API documentation at [http://127.0.0.1:8000/docs.](http://127.0.0.1:8000/docs.)

## Deployed Application

The deployed version of this application is available at: [https://fastapi-n2df.onrender.com/docs.](https://fastapi-n2df.onrender.com/docs.) it's a free instance and sometimes will spin down with inactivity, which can delay requests by 50 seconds or more.
