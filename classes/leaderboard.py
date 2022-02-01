from os import path


class LeaderBoard():
    def __init__(self):
        self.filename = 'scores.txt'

    def save_score(self, score):
        if path.exists(self.filename):
            score = '\n' + str(score)
        else:
            score = str(score)

        with open(self.filename, 'a') as f:
            f.write(score)
