from pygame import font
from os import path


class LeaderBoard():
    """Leaderborad class that saves scores and display them at the end of game.
    """

    def __init__(self, parent_surface):
        """Create leaderBoard instance.

        Args:
            parent_surface (pygame.display): Parent screen where leaderboard will be displayed.
        """
        self.parent_surface = parent_surface
        self.filename = 'scores.txt'
        self.font = font.SysFont('arial', 30)

    def save_score(self, score):
        """Save score to file.

        Args:
            score (int): Score at the end of game.
        """
        if path.exists(self.filename):
            score = '\n' + str(score)
        else:
            score = str(score)

        with open(self.filename, 'a') as f:
            f.write(score)

    def show(self):
        """Show top 5 scores in "Leader board" form.
        """
        text = self.font.render("Top 5 Scores:", True, (255, 255, 255))
        self.parent_surface.blit(text, (200, 350))

        scores = self.get_top_5()
        self.show_scores(scores)

    def show_scores(self, scores):
        """Show scores on screen

        Args:
            scores (list): List of scores to be displayed.
        """
        position = 400
        place = 1
        for score in scores:
            text = self.font.render(f"{place}. {score}", True, (255, 255, 255))
            self.parent_surface.blit(text, (230, position))
            position += 50
            place += 1

    def get_top_5(self):
        """Get top 5 unique scores.

        Returns:
            list: Top 5 unique scores.
        """
        scores = self.get_uniquescores()
        return scores[:5]

    def get_uniquescores(self):
        """Get uniquescores from file.

        Returns:
            list: Unique scores from scores.txt file
        """
        f = open(self.filename, "r")

        uniquescores = []
        for score in f:
            score = int(score)
            if score not in uniquescores:
                uniquescores.append(score)

        uniquescores.sort(reverse=True)
        return uniquescores

    def which_place(self, score):
        """Return the place gained by the player.

        Args:
            score (int): Score at the end of game.

        Returns:
            int: Place gained by user.
        """
        scores = self.get_uniquescores()
        print(score)
        print(scores)
        return scores.index(score) + 1
