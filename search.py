import requests, os
from dotenv import load_dotenv


url = "https://places.googleapis.com/v1/places:searchText"

load_dotenv(".env")
searchLimit = os.getenv("LIMIT")
places_api_key = os.getenv("API_KEY")

def search(
        business_type: str,
        location: str,
        website: str = "a",
        min_rating: float = 0,
        max_rating: float = 5,
        limit: int | None = searchLimit,
        min_reviews: int = 0,
        max_reviews: int = 999999999,
        output_format: str = "cli",
        api_key: str | None = places_api_key):

    # print(limit, api_key)

    all_good = True
    while all_good:
        if api_key is None:
            print("You have not set an API key, please set one using 'setup key <api_key>'")
            all_good = False
        if limit is None:
            print("You have not set a search limit, please set one using 'setup limit <limit>'")
            all_good = False

        query = f"{business_type} in {location}"

        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.websiteUri,places.nationalPhoneNumber"
        }

        data = {
            "textQuery": query,
            "pageSize": limit
        }

        response = requests.post(url, headers=headers, json=data)
        results = response.json()

        print(results)
        all_good = False