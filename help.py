def help():
    print("""
    Search
        
        Used to search for businesses.
    
        Default Usage:
            search <business-type> <area> for default search e.g. \"search Barber London\"
        Additional Filters:
            - website (y / n)
            - min-rating (0-5)
            - max-rating (0-5)
            - min-reviews
            - max-reviews
            - output-format (cli / csv)
        Examples:
            search electrician london --output-format csv
            search restaurant croydon --website n
            search cafe manchester --min-rating 0 --max-rating 3
    
    Campaigns
        
        Used to store businesses that you've found under categories
        
        Create campaign:
            campaign create <name>
        Select campaign (searches will be stored under this campaign):
            campaign select <name>
        Stop storing searches:
            campaign disconnect
        Delete campaign:
            campaign remove <name>
        List all campaigns:
            campaign list
        List all data within a campaign:
            campaign list <name>
            
    Setup
        
        Set API key:
            setup key <api_key>
        Learn how to find your API key:
            setup key
        Set limit of businesses returned to you per search:
            setup limit <limit>
            
    """)