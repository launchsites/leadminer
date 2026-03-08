import database
from database import *
from dotenv import load_dotenv, set_key
import os


def campaign(command: str, option: str | None = None):

    if command == "create":
        make_campaign(option)

    elif command == "select":
        campaign_id = get_campaign_id(option)
        if campaign_id:
            load_dotenv(".env")
            set_key(".env", "ACTIVE_CAMPAIGN_NAME", option)
            set_key(".env", "ACTIVE_CAMPAIGN_ID", campaign_id)

    elif command == "list":
        if option:
            #handle listing the data from campaign
            list_campaign_data(option)
        else:
            # list all the campaigns
            list_campaigns()

    elif command == "remove":
        # remove the campaign
        remove_campaign(option)