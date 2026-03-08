import typer
from dotenv import load_dotenv, set_key
import os
from pathlib import Path

from search import search
from output import output
from setup import setup
from help import help
from campaigns import campaign


# check that .env exists otherwise create
if not os.path.exists(".env"):
   Path(".env").touch()

load_dotenv(".env")

searchLimit = os.getenv("LIMIT")
places_api_key = os.getenv("API_KEY")

# if no limit set
if searchLimit is None:
    set_key(".env", "LIMIT", "100")

app = typer.Typer()

# search
app.command()(search)
app.command()(output)
app.command()(help)
app.command()(campaign)
app.command()(setup)


app()