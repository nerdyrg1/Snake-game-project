# from turtle import Turtle, Screen
#
# snake_object = []
# x_positions = []
#
# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=600,height=600)
# screen.title("My Snake Game")
#
# x = 0
# for i in range(3):
#     object1 = Turtle(shape="square")
#     object1.color("white")
#     object1.goto(x=x, y=0)
#     snake_object.append(object1)
#     x -= 20
#
# screen.exitonclick()


class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    def __init__(self):
        #super().__init__()
        self.is_a_good_boy = True

    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")

Labrador().bark()


from turtle import Turtle

class Food(Turtle):
