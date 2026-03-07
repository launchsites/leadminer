import typer
from dotenv import load_dotenv
import os
from pathlib import Path

# check that .env exists otherwise create
if not os.path.exists(".env"):
   Path(".env").touch()

load_dotenv(".env")

searchLimit = os.getenv("LIMIT")
api_key = os.getenv("API_KEY")

app = typer.Typer()


#help function
@app.command()
def helps():
    print()

#search function
@app.command()
def search(
        business_type: str,
        location: str,
        website: bool = "a",
        min_rating: float = 0,
        max_rating: float = 5,
        limit: int = searchLimit,
        min_reviews: int = 0,
        max_reviews: int = 999999999,
        output_format: str = "cli"):

    print("search")

# campaign command
    # create campaign
    # select campaign
    # list campaigns
    # remove campaigns
    # list data of campaign

# setup command
    # setup places api key
    # set max limit

app()