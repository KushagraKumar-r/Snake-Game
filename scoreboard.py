from turtle import Turtle

class Scoreboard(Turtle):
    #Scoreboard class can do every thing that a turtle class do
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
        

    def update(self):
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",24,"normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()
