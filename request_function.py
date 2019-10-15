import requests

key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiNDUzNTE3MzQ1IiwiYXV0aF9pZCI6IjIiLCJ0b2tlbl90eXBlIjoiQWNjZXNzVG9rZW4iLCJzZXJ2aWNlX2lkIjoiNDMwMDExNDgxIiwiWC1BcHAtUmF0ZS1MaW1pdCI6IjIwMDAwOjEwIiwibmJmIjoxNTY5MTIyNzM3LCJleHAiOjE2MzIxOTQ3MzcsImlhdCI6MTU2OTEyMjczN30.KYYiiOSbovCodNSk1lDC1NlI3ZEryWYW5TzbSYzz_UY"
headers = {'Authorization': key}

def user_info(nickname):
    URL = "https://api.nexon.co.kr/fifaonline4/v1.0/users?nickname=%s" % nickname
    response = requests.get(URL, headers=headers)
    user_info = response.json()
    return user_info

def maxdivision(user_id):
    URL = "https://api.nexon.co.kr/fifaonline4/v1.0/users/%s/maxdivision" % user_id
    response = requests.get(URL, headers=headers)
    return response.json()

def matches(user_id, matchtype):
    URL = "https://api.nexon.co.kr/fifaonline4/v1.0/users/%s/matches?matchtype=%s" % (user_id, matchtype)
    response = requests.get(URL, headers=headers)
    return response.json()

def trade(user_id, tradetype):
    URL = "https://api.nexon.co.kr/fifaonline4/v1.0/users/%s/markets?tradetype=%s" % (user_id, tradetype)
    response = requests.get(URL, headers=headers)
    return response.json()

def spid():
    URL = "https://static.api.nexon.co.kr/fifaonline4/latest/spid.json"
    response = requests.get(URL, headers=headers)
    spid = response.json()
    return spid

def seson_id(spid):
    si = spid[0:3]
    if si == "101":
        return "ICON"
    if si == "201":
        return "NHD"
    if si == "202":
        return "TKI"
    if si == "206":
        return "TB"
    if si == "207":
        return "TT"
    if si == "210":
        return "GR"
    if si == "211":
        return "19TOTY"
    if si == "212":
        return "18TOTY"
    if si == "213":
        return "MC ICON"
    if si == "214":
        return "TC"
    if si == "215":
        return "19TOTS"
    if si == "216":
        return "HOT"
    if si == "295":
        return "K19"
    if si == "297":
        return "MCC"
    if si == "298":
        return "K18"
    if si == "300":
        return "18"
    if si == "317":
        return "17"
    if si == "500":
        return "18A"
    if si == "501":
        return "18S"

def find_player(player_id):
    for i in spid():
        name = i["name"]
        id = str(i["id"])
        season = seson_id(id)
        if player_id == id:
            return season+' '+name
