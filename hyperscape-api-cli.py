import urllib.request
import json
import os

platformCheck = False # For the while statement, if True, the platform variable has been set
platform = "" # The platform that the user chose
platformID = 0 # The number the user typed that corresponds to the platform in the variable platform

# Set a user-agent to access the API, gives a HTTP error 403 (Forbidden) if you don't
UAheader = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
user = input("What Hyperscape username would you like to search for? : ")

# Clears the console (Windows CMD)
os.system("cls")

# Check that the given input is valid, if so, assign the correct platform
while platformCheck == 0:
    try:
        platformID = int(input("What platform does this user play on? \n 1. UPlay \n 2. Playstation \n 3. Xbox \n"))
    except ValueError:
        print("Please enter a valid integer.")
    if platformID == 1:
        platform = "uplay"
    elif platformID == 2:
        platform = "psn"
    elif platformID == 3:
        platform = "xbl"
    if platform != "":
        platformCheck = True
    os.system("cls")

# Contact the API with our gathered input, note that the API must be contacted twice, as the username
# (when sent to the API) gives the Ubisoft account UUID, which can then be sent back to the API to retrieve statistics
url = "https://hypers.apitab.com/search/{}/{}"
request = urllib.request.Request(url.format(platform, user), data=None, headers=UAheader)

# Parse the retrieved JSON (has Ubisoft UUID) from the API into a Python Dictionary
with urllib.request.urlopen(request) as openURL:
    data = json.loads(openURL.read())

# This retrieves the UUID by reading the only key of the child dictionary "players" which contains a child dictionary
# named the UUID we need. Then parses that data as a string, then uses string slicing [12:48] to remove any excess
# information, leaving us with the UUID assigned to the variable "uid"
uid = str(data["players"].keys())[12:48]

# The UID request URL has a slightly different format, as is defined here
uidURL = "https://hypers.apitab.com/player/{}"
request = urllib.request.Request(uidURL.format(uid), data=None, headers=UAheader)

# Parse the retrieved JSON (has player statistics) from the API into a Python Dictionary
with urllib.request.urlopen(request) as openURL:
    fullData = json.loads(openURL.read())
try:
    # Prints a few retrieved player statistics
    print("Victories : " + str(fullData["data"]["stats"]["wins"]) +
          "\nCrown Victories : " + str(fullData["data"]["stats"]["crown_wins"]) +
          "\nOverall Damage : " + str(fullData["data"]["stats"]["damage"]) +
          "\nMatches : " + str(fullData["data"]["stats"]["matches"]) +
          "\nKills : " + str(fullData["data"]["stats"]["kills"]) +
          "\nFusions : " + str(fullData["data"]["stats"]["fusions"]) +
          "\nTime Played : " + str(fullData["data"]["stats"]["time_played"]) +
          "\nCareer Best: Kills : " + str(fullData["data"]["stats"]["careerbest_kills"]) +
          "\nCareer Best: Damage Done : " + str(fullData["data"]["stats"]["careerbest_damage_done"]) +
          "\nKD : " + str(fullData["data"]["stats"]["kd"]))
except AttributeError:
    # Only occurs when the API cannot find that username
    print("The statistics for that username could not be retrieved.")

# Pauses the console window so the statistics are readable
os.system("pause")
