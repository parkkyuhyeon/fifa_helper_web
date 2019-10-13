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