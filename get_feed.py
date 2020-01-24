import json
import os
from pathlib import Path
import requests
import feedparser


def get_feed():
    """ get the feed data, cache if needed """

    if Path('output.json').exists:
        # if the file already exists
        with open('output.json', 'r') as file_obj:
            # load the file
            # read the json data
            feed = json.load(file_obj)
    else:

        response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Region=33')
        feed = feedparser.parse(response.text)

        #save the content to a file so we can understand it!
        with open('output.json', 'w') as file_obj:
            # the above line tells us to open a new file
            # but only keep it open for the following lines
            # the line below puts the content in the file
            json.dump(feed, file_obj, indent=2)

    return feed