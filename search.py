def search(
        business_type: str,
        location: str,
        website: str = "a",
        min_rating: float = 0,
        max_rating: float = 5,
        limit: int | None = None,
        min_reviews: int = 0,
        max_reviews: int = 999999999,
        output_format: str = "cli",
        api_key: str | None = None):

    print(business_type)
    print(location)

