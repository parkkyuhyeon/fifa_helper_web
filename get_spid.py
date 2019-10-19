import request_function as rf

user_info = rf.user_info("폭풍저그콩")
user_id = user_info['accessId']
user_name = user_info['nickname']
user_level = user_info['level']

maxdivision = rf.maxdivision(user_id)
matches_50 = rf.matches(user_id, "50")
matches_52 = rf.matches(user_id, "52")
trade_buy = rf.trade(user_id, "buy")
trade_sell = rf.trade(user_id, "sell")

print(rf.find_player(trade_buy))