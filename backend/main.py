from flask import request, jsonify
from config import app, db
from models import Taps 

# get all taps accounts
@app.route("/taps", methods=["GET"])
def get_all_taps():
    # get all the taps
    taps = Taps.query.all()

    # convert taps to JSON  
    json_taps = list(map(lambda x: x.to_json(), taps))

    return jsonify({"taps": json_taps})