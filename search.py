import requests, os
from dotenv import load_dotenv, get_key
import classes
from database import save_lead
import output as output_functions

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

        object_results = []
        campaign_active = get_key(".env", "ACTIVE_CAMPAIGN_NAME")

        for place in results["places"]:
            place_id = place["id"]
            place_name = place["displayName"]["text"]
            place_address = place["formattedAddress"]
            place_rating = place.get("rating")
            place_reviews = place.get("userRatingCount")
            websiteUrl = place.get("websiteUri")
            place_phone = place.get("nationalPhoneNumber")

            temp = classes.Lead(place_id, place_name, place_address, place_phone, websiteUrl, place_rating, place_reviews)
            object_results.append(temp)
            output = []

        for lead in object_results:
            valid = True
            if not (website == "a" or (website == "y" and lead.website) or (website == "n" and not lead.website)):
                valid = False
            if min_rating > lead.rating:
                valid = False
            if max_rating < lead.rating:
                valid = False
            if min_reviews > lead.reviews:
                valid = False
            if max_reviews < lead.reviews:
                valid = False
            if valid:
                output.append(lead)
                if campaign_active:
                    save_lead(lead, campaign_active)

        if output_format == "cli":
            output_functions.output_cli(output)
        elif output_format == "csv":
            output_functions.output_csv(output)
        all_good = False