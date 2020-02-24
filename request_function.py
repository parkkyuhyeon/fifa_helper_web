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
    if si == "217":
        return "COC"
    if si == "218":
        return "OTW"
    if si == "219":
        return "NG"
    if si == "220":
        return "20TOTY"
    if si == "222":
        return "20TOTN"
    if si == "295":
        return "K19"
    if si == "297":
        return "MCC"
    if si == "298":
        return "K18"
    if si == "300":
        return "19"
    if si == "317":
        return "17"
    if si == "318":
        return "18"
    if si == "500":
        return "18A"
    if si == "501":
        return "18S"
    if si == "502":
        return "19A"

def find_player(trade_list):
    li = spid()
    for i, a in enumerate(trade_list):
        player_id = str(a["spid"])
        for b in li:
            id = str(b["id"])
            if player_id == id:
                trade_date = a["tradeDate"]
                value = str(a["value"])
                name = b["name"]
                seson = seson_id(id)
                grade = str(a["grade"])
                trade_list[i] = [trade_date, seson, name, '+'+grade, value]
    return trade_list

def division(grade):
    if grade == "1100":
        return "챌린지"
    if grade == "2000":
        return "월드클래스1"
    if grade == "2100":
        return "월드클래스2"
    if grade == "2200":
        return "월드클래스3"
    if grade == "2300":
        return "프로1"
    if grade == "2400":
        return "프로2"
    if grade == "2500":
        return "프로3"
    if grade == "2600":
        return "세미프로1"
    if grade == "2700":
        return "세미프로2"
    if grade == "2800":
        return "세미프로3"
    if grade == "2900":
        return "아마추어1"
    if grade == "3000":
        return "아마추어2"
    if grade == "3100":
        return "아마추어3"
    if grade == "800":
        return "슈퍼챔피언스"
    if grade == "900":
        return "챔피언스"

def past_glory(maxdivision):
    for a in maxdivision:
        if a["matchType"] == 50:
            match_50 = a
        if a["matchType"] == 52:
            match_52 = a
    if 'match_50' in locals() and 'match_52' in locals():
        match_50_achieve = str(match_50["division"])
        match_50_achievementdate = match_50["achievementDate"]
        match_52_achieve = str(match_52["division"])
        match_52_achievementdate = match_52["achievementDate"]
        return [["공식경기", match_50_achievementdate, division(match_50_achieve)], ["감독모드" ,match_52_achievementdate, division(match_52_achieve)]]
    elif 'match_50' in locals():
        match_50_achieve = str(match_50["division"])
        match_50_achievementdate = match_50["achievementDate"]
        return [["공식경기", match_50_achievementdate, division(match_50_achieve)]]
    elif 'match_52' in locals():
        match_52_achieve = str(match_52["division"])
        match_52_achievementdate = match_52["achievementDate"]
        return [["공식경기", match_52_achievementdate, division(match_52_achieve)]]
    else:
        return [["-", "-", "-"]]


