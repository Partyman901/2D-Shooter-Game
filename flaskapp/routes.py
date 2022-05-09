from flask import Blueprint, jsonify, request, render_template
from flask_models import Score, ScoreManager

bp_api = Blueprint("api", __name__)

@bp_api.route("/scores")
def show_scores():
    """ Displays scorted scores in html template """
    manager = ScoreManager()
    new_scores = list()
    for score in manager.return_json():
        score["score"] = int(score["score"])
        new_scores.append(score)
    new_scores = sorted(new_scores, key = lambda i : i['score'], reverse=True)
    return render_template("index.html", scores = new_scores)


@bp_api.route("/score", methods=["PUT"])
def create_score():
    """ Creates new score from json data """
    json_data = request.get_json()

    if "score" not in json_data:
        return "Invalid Data", 400

    manager = ScoreManager()
    manager.add_score(json_data["score"])
    manager.save()
    return "", 204
