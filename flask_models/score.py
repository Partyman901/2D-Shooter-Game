import datetime

class Score:
    def __init__(self, score, identifier, date=datetime.datetime.now()):
        """ Sets score attributes """
        self._identifier = identifier
        self._score = score
        print("The date is:", date)
        if type(date) is str:
            self._date = date
        else:
            self._date = date.strftime('%d-%m-%y %H:%M')

    def to_json(self):
        """ Converts score attributes to a jsonable format """
        return {
                "id": self._identifier,
                "score": self._score,
                "date": self._date
            }

