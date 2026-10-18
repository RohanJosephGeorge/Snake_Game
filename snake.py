from turtle import Turtle
up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.creation()
        self.head=self.snakebody[0]
    def creation(self):
        self.snakebody=[]
        for i in range(3):
            snake=Turtle()
            snake.color("white")
            snake.shape("square")
            snake.penup()
            snake.goto(x=-20*i,y=0)
            self.snakebody.append(snake)
    def move(self):
        for i in range(len(self.snakebody)-1,0,-1):
            xcor=self.snakebody[i-1].xcor()
            ycor=self.snakebody[i-1].ycor()
            self.snakebody[i].goto(xcor,ycor)
        self.head.forward(20)
    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)
    def extend(self):
        snake = Turtle()
        snake.speed('fastest')
        snake.hideturtle()
        snake.shape("square")
        snake.penup()
        snake.goto(self.snakebody[-1].xcor(),self.snakebody[-1].ycor())
        snake.color("white")
        self.snakebody.append(snake)
        snake.showturtle()