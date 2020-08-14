# TODO: Comment ALL of this code
import urllib.request
import json
import os
clear = lambda: os.system("cls")
pause = lambda: os.system("pause")
platformCheck = 0
platform = ""
platformID = 0
url = "https://hypers.apitab.com/search/{}/{}"
user = input("What Hyperscape username would you like to search for? : ")
clear()
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
        platformCheck = 1
    clear()
request = urllib.request.Request(url.format(platform, user), data=None, headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"})
with urllib.request.urlopen(request) as openURL:
    data = json.loads(openURL.read())
uid = str(data["players"].keys())[12:48]
uidURL = "https://hypers.apitab.com/player/{}"
request = urllib.request.Request(uidURL.format(uid), data=None, headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"})
with urllib.request.urlopen(request) as openURL:
    fullData = json.loads(openURL.read())
try:
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
    print("The statistics for that username could not be retrieved.")
pause()

