from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.n=0
        self.color('white')
        self.goto(0,250)
        self.write(f'Score: {self.n}', True, align='center', font=('Arial', 24, 'normal'))
    def increase_score(self):
        self.n+=1
        self.clear()
        self.goto(0,250)
        self.write(f'Score: {self.n}', True, align='center', font=('Arial', 24, 'normal'))
    def alert(self):
        self.goto(0,0)
        self.write('GAME OVER', True, align='center', font=('Helvetica', 24, 'normal'))