from dotenv import load_dotenv, set_key

# setup command
    # setup places api key
    # set max limit



def setup(choice: str, value: str):
    if choice == "key":
        set_key(".env", "API_KEY", value)
    elif choice == "limit":
        set_key(".env", "LIMIT", value)