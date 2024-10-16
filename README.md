# Car Image Generator

Un projet FastAPI pour générer des images de voitures à l'aide de l'API OpenAI. L'application vous permet de spécifier un modèle de voiture et une couleur, puis utilise l'API OpenAI pour générer une image correspondante.

## Prérequis

- Python >= 3.12
- UV https://github.com/astral-sh/uv
- Une clé API OpenAI

## Installation (Mac/Linux)

`uv venv --python 3.12`

`source .venv/bin/activate`

`uv sync`

`cp .env.template .env`

Mettez votre clef OpenAI dans le .env nouvellement créé.

`source .env`

## Lancement

Pour lancer le serveur :

`uv run fastapi dev`

Pour utiliser le programme via la CLI :

`uv run cli.py --model [MODEL] --color [COLOR]`

## Deploy

Build le container :

`docker build -t car-project .`

Run :

`docker run -p 8000:80 -e OPENAI_API_KEY=your_super_secret_key car-project`
