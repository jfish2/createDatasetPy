from json import JSONDecodeError
import numpy as np
import pandas as pd
import requests
import json

# Create a dataset using the Twitch API pass through. Lines 9 through 21 test retrieve data from the FCC channel

# url = "https://wind-bow.glitch.me/twitch-api/channels/freecodecamp"
# response = requests.get(url).status_code
# print("API Response Code", ": ", response)
# try:
#     if response == 200:
#         json_content = requests.get(url).json()
#         print(json_content)
#     else:
#         print("Unsuccessful GET request", ": ", response)
# except JSONDecodeError as e:
#     print("JSON decoding failed. Trying again without JSON decoding...")
#     json_content = requests.get(url)
#     print(json_content)

# List of channels to access
channels = ["ESL_SC2", "OgamingSC2", "cretetion", "freecodecamp", "storbeck", "habathcx", "ninja", "shroud", "Dakotaz",
            "esltv_cs", "pokimane", "tsm_bjergsen", "boxbox", "nobs2ninjas", "a_seagull", "kinggothalion",
            "thenadeshot",
            "sivhd", "kingrichard"]

channels_lst = []
start_url = "https://wind-bow.glitch.me/twitch-api/channels/"
# Loop through each channel and GET data
for channel in channels:
    json_content = requests.get(start_url + channel).json()
    if 'error' not in json_content:
        channels_lst.append([json_content['_id'], json_content['display_name'], json_content['status'], json_content['followers'], json_content['views']])

dataset = pd.DataFrame(channels_lst)
# print(dataset.sample(5))

dataset.columns = ['ID', 'Display Name', 'Status', 'Followers', 'Views']
dataset.dropna(axis=0, how='any', inplace=True)
dataset.index = pd.RangeIndex(len(dataset.index))

# Print sample data to verify that columns/rows are cleaned
print(dataset.sample(5))

# Export data to csv file in directory
dataset.to_csv('twitch_channels_dataset', index=True)



