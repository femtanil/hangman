# Hangman

Simple hangman guessing game.

## Install

### Front

The frontend can be installed using `npm`. Inside the `front` directory run:
```commandline
npm install
```
### Back
Dependencies are defined in `pyproject.toml` and `requirements.txt`.
The backend can be installed in a virtual environment. For example using Poetry and inside the `app` directory:
```commandline
poetry install
```

## Start
### Front
Before starting the vite development server, create a `.env` file inside the `front` directory add these lines to it:
```commandline
VITE_BACKEND_URL="[BackendUrl]"
```
Replace BackendUrl with the URL of the uvicorn server, for example:
```commandline
VITE_BACKEND_URL="http://localhost:8000"
```
Start the vite development server using:
```commandline
npm run dev
```

### Back
Before starting the uvicorn development server, create a `.env` file at the root of project and add these lines to it:
```commandline
#!/bin/bash
export SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
export ALGORITHM="HS256"
export ACCESS_TOKEN_EXPIRE_MINUTES=30
```
This very public secret key is used to hash the passwords in the development server allowing (for now) to have two default users for testing.

Activate the virtual environment. For example using Poetry and inside the `app` directory:
```commandline
poetry shell
```
Then start the uvicorn server (development):
```commandline
uvicorn app.main:api --reload
