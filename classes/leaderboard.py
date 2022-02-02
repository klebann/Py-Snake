from pygame import font
from os import path


class LeaderBoard():
    def __init__(self, parent_surface):
        self.parent_surface = parent_surface
        self.filename = 'scores.txt'
        self.font = font.SysFont('arial', 30)

    def save_score(self, score):
        if path.exists(self.filename):
            score = '\n' + str(score)
        else:
            score = str(score)

        with open(self.filename, 'a') as f:
            f.write(score)

    def show(self):
        text = self.font.render("Top 5 Scores:", True, (255, 255, 255))
        self.parent_surface.blit(text, (200, 350))

        scores = self.get_top_5()
        self.show_scores(scores)

    def show_scores(self, scores):
        position = 400
        place = 1
        for score in scores:
            text = self.font.render(f"{place}. {score}", True, (255, 255, 255))
            self.parent_surface.blit(text, (230, position))
            position += 50
            place += 1

    def get_top_5(self):
        scores = self.get_uniquescores()
        return scores[:5]

    def get_uniquescores(self):
        f = open(self.filename, "r")

        uniquescores = []
        for score in f:
            score = int(score)
            if score not in uniquescores:
                uniquescores.append(score)

        uniquescores.sort(reverse=True)
        return uniquescores

    def which_place(self, score):
        scores = self.get_uniquescores()
        print(score)
        print(scores)
        return scores.index(score) + 1
