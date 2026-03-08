"""place["id"],
        place["displayName"]["text"],
        place["formattedAddress"],
        place.get("rating"),
        place.get("userRatingCount"),"""
from numbers import Real


class Lead:
    def __init__(self, place_id: str, name: str, address: str, phone: str, website: str, rating: float, reviews: int):
        self.placeId: str = place_id
        self.name: str = name
        self.address: str = address
        self.phone: str = phone
        self.website: str = website
        self.rating: float = rating
        self.reviews: int = reviews

