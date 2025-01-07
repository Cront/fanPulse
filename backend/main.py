from flask import request, jsonify
from config import app, db
from models import Taps
from datetime import datetime

# basic implementation team scores dict (WILL REMOVE)
team_scores = {
    "team_1": 0,
    "team_2": 0
}


def fetch_all_taps():
    # get all taps
    return Taps.query.all()

# @app.route("/taps", methods=["GET"])
# def get_all_taps():
#     # fetch all taps
#     taps = fetch_all_taps()
#
#     # convert taps to JSON
#     json_taps = list(map(lambda x: x.to_json(), taps))
#
#     return jsonify({"Taps": json_taps})


@app.route("/taps_data", methods=["GET"])
def get_taps_data():
    # user_id = request.args.get("user_id")
    #
    # # if no user_id provided, output all user_ids
    # if not user_id:
    #     taps = fetch_all_taps()
    #
    #     for tap in taps:
    #         print(
    #             f"User:{tap.user_id}, Team: {tap.team_id}, Timestamp: {tap.timestamp}")
    #
    #     json_taps = [tap.to_json() for tap in taps]
    #     return jsonify({"Team scores": json_taps}), 200
    # # one user
    # else:
    #     tap = Taps.query.get(user_id)
    #
    #     if not tap:
    #         return jsonify({"message": "Error: invalid User ID"}), 400
    #
    #     print(
    #         f"User:{tap.user_id}, Team: {tap.team_id}, Timestamp: {tap.timestamp}")
    #
    #     json_tap = tap.to_json()
    #     return jsonify({"tap": json_tap})

    tap_counts = (
        db.sesion.query(Taps.team_id, db.func.count(
            Taps.id).label("tap_count")).group_by(Taps.team_id).all()
    )

    result = {team_id: tap_count for team_id, tap_count in tap_counts}

    return jsonify({"team_tap_counts": result}), 200


@app.route("/taps_add", methods=["POST"])
def add_taps():
    data = request.get_json()
    user_id = data.get("user_id")
    team_id = data.get("team_id")

    if not user_id:
        return jsonify({"Error": "Invalid entry for User ID"})
    elif not team_id:
        return jsonify({"Error": "Invalid entry for Team ID"})

    # update teams tap counter
    team_scores[f"team_{team_id}"] += 1

    # add users tap to database
    new_tap = Taps(user_id=user_id, team_id=team_id, timestamp=datetime.now())

    try:
        db.session.add(new_tap)
        db.session.commit()
    except Exception as e:
        return jsonify({"Error": str(e)}), 400

    return jsonify({
        "Message": "Tap entered",
        "Tap": new_tap.to_json(),
        "Team Scores": team_scores
    }), 201


@app.route("/get_scores", methods=["GET"])
def get_team_scores():
    return jsonify(team_scores)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
