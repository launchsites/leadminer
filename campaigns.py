import database
from database import *
from dotenv import load_dotenv, set_key, get_key
import os


def campaign(command: str, option: str | None = None):

    if command == "create":
        #check valid name

        make_campaign(option)

    elif command == "select":
        campaign_id = get_campaign_id(option)
        if campaign_id:
            load_dotenv(".env")
            set_key(".env", "ACTIVE_CAMPAIGN_NAME", option)
            set_key(".env", "ACTIVE_CAMPAIGN_ID", campaign_id)
        else:
            print("That campaign does not exist")

    elif command == "list":
        if option:
            campaign_id = get_campaign_id(option)
            if campaign_id:
                #handle listing the data from campaign
                list_campaign_data(option)
            else:
                print("That campaign does not exist")
        else:
            # list all the campaigns
            list_campaigns()

    elif command == "remove":
        campaign_id = get_campaign_id(option)
        if campaign_id:
            # remove the campaign
            remove_campaign(option)
        else: print("That campaign does not exist")

    elif command == "disconnect":
        load_dotenv(".env")
        exists = get_key(".env", "ACTIVE_CAMPAIGN_NAME")
        if exists:
            set_key(".env", "ACTIVE_CAMPAIGN_NAME", "")
        else: print("You are not currently connected to a campaign")
