from .score import Score
import json
import os

class ScoreManager:
    def __init__(self, filename="scores.json"):
        """ Sets ScoreManager attributes """
        self._scores = dict()
        self._filename = filename

        if not os.path.exists(filename):
            return None

        with open(filename, 'r') as the_file:
            json_data = json.load(the_file)
            for score in json_data:
                new_score = Score(score=score["score"], identifier=score["id"], date=score["date"])
                self._scores[str(score["id"])] = new_score


    def add_score(self, score):
        """ Adds score to list of scores """
        new_id = len(self._scores) + 1
        self._scores[str(new_id)] = Score(score=score, identifier=new_id)


    def return_json(self):
        """ Returns all scores as a jsonable list """
        new_json = list()
        for score in self._scores.values():
            new_json.append(score.to_json())
        return new_json


    def save(self):
        """ Saves current scores to a json file """
        with open(self._filename, "w") as the_file:
            json.dump([score.to_json() for score in self._scores.values()], the_file)
