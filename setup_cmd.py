import typer
from dotenv import load_dotenv, set_key

# setup command
    # setup places api key
    # set max limit



def setup(choice: str = typer.Argument(...), value: str | None = typer.Argument(None)):

    if choice == "key" and value:
        set_key(".env", "API_KEY", value)
    elif choice == "limit":
        set_key(".env", "LIMIT", value)

    elif choice == "key" and not value:
        print("""
        To use leadminer, you need a Google Places API key.
        
        1. Go to this link, sign in, and click "enable":
        https://console.cloud.google.com/apis/library/places-backend.googleapis.com

        2. Create an API key:
        https://console.cloud.google.com/apis/credentials
        
        3. Copy the key and run:
        leadminer setup key <YOUR_API_KEY>
        """)

