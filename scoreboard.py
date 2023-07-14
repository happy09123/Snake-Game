from turtle import Turtle
ALIGNMENT = "center"
FONTS = {
    "default": ("Courier", 15, "normal"),
    "big": ("Courier", 25, "normal"),
}

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.high_score = open("data.txt").read()
        self.color("white")
        self.penup()
        self.color("#DCDCDC")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONTS["default"])
        self.goto(0, 240)
        self.write(f"High Score: {self.high_score}", False, ALIGNMENT, FONTS["default"])


    def restart(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as high_score:
                high_score.write(str(self.score))

            self.high_score = open("data.txt").read()

        self.score = 0

        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONTS["big"])
        self.goto(0, -30)
        self.write("Press 'A' to retry.", False, ALIGNMENT, FONTS["default"])

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
