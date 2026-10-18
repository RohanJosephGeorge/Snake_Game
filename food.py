from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        x=random.randint(-275,+275)
        y=random.randint(-275,+275)
        self.speed("fastest")
        self.goto(x,y)
    def refresh(self):
        x=random.randint(-275,+275)
        y=random.randint(-275,+275)
        self.goto(x,y)