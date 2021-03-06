from flask import Flask, render_template, request
import request_function as rf

app = Flask(__name__)
@app.route("/")
def get_nickname():
    return render_template("get_nickname.html")
@app.route("/", methods = ["POST"])
def result():
    nickname = request.form['nickname']

    user_info = rf.user_info(nickname)
    user_id = user_info['accessId']
    user_name = user_info['nickname']
    user_level = user_info['level']

    maxdivision = rf.past_glory(rf.maxdivision(user_id))
    matches_50 = rf.matches(user_id, "50")
    matches_52 = rf.matches(user_id, "52")
    trade_buy = rf.find_player(rf.trade(user_id, "buy"))
    trade_sell =rf.find_player(rf.trade(user_id, "sell"))


    return render_template("result.html", user_name = user_name, user_level = user_level, maxdivision = maxdivision, matches_50 = enumerate(matches_50), matches_52 = enumerate(matches_52), trade_buy = trade_buy, trade_sell = trade_sell)

@app.route("/match", methods = ["GET"])
def match_info():

    return

port_num = 8080

if __name__ == "__main__":
    app.run(port = port_num)
