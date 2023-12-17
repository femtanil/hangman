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

### Back
Activate the virtual environment. For example using Poetry and inside the `app` directory:
```commandline
poetry shell
```
Then start the uvicorn server (development):
```commandline
uvicorn app.main:api --reload
