# Database: SQLite Notes

## Overview
- single file database meaning all data is stored in a single disk file
- serverless architecture meaning it does not require a separate server process

## FastApi, Pydantic and uvicorn
- FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- Pydantic is a data validation and settings management library using Python type annotations.
- Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

### Commands to run FastAPI with Uvicorn
```bash
uvicorn file_name:app
```

- after u run the command, open the browser and go to `http://127.0.0.1:8000/docs` to see the automatic interactive API documentation (provided by Swagger UI).

### Running streamlit app
```bash
streamlit run file_name.py
```