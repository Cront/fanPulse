from flask import request, jsonify
from config import app, db
from models import Taps 

def fetch_all_taps():
    # get all taps
    return Taps.query.all()

# get all taps accounts
@app.route("/taps", methods=["GET"])
def get_all_taps():
    # fetch all taps
    taps = fetch_all_taps() 

    # convert taps to JSON  
    json_taps = list(map(lambda x: x.to_json(), taps))

    return jsonify({"taps": json_taps})

@app.route("/taps_data", methods=["GET"])
def get_taps_data():
    user_id = request.args.get("user_id")
    
    # if no user_id provided, output all user_ids
    if not user_id:
        taps = fetch_all_taps()

        for tap in taps:
            print(f"User:{tap.user_id}, Team: {tap.team_id}, Timestamp: {tap.timestamp}")

        json_taps = [tap.to_json() for tap in taps]
        return jsonify({"taps": json_taps})
    # one user
    else:
        tap = Taps.query.get(user_id)
        print(f"User:{tap.user_id}, Team: {tap.team_id}, Timestamp: {tap.timestamp}")

        json_tap = tap.to_json()
        return jsonify({"tap": json_tap})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)