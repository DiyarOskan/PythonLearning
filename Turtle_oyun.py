import random
import turtle

screen = turtle.Screen()
screen = turtle.Screen()
screen.bgcolor("#DEB887")
screen.title("Catch The Turtle")

FONT = ("Arial" , 20 , "bold")
game_over = False
score = 0

#turtle list
turtle_list = []

#countdown turtle
count_down_turtle = turtle.Turtle()

# score turtle
score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()

    height= screen.window_height()
    i = height * 0.4
    score_turtle.setpos(0,i)
    score_turtle.write(arg="Score:0",move=False,align="center",font=FONT)

position_variable=10

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += + 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score:{score}", move=False, align="center", font=FONT)


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("#008080")
    t.setpos(x * position_variable,y * position_variable)
    t.pendown()
    turtle_list.append(t)


def turtles_positioning():
    for a in [-2,-1,0,1,2]:
        for b in [-2, -1, 0, 1, 2]:
            make_turtle(a,b)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)


def countdown(time):
    global game_over
    height = screen.window_height()
    i = height * 0.3
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0,i)
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write(f"Time: {time}",move=False,align="center",font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write("Game Over!", align='center', font=FONT)

def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_score_turtle()
    turtles_positioning()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game_up()
turtle.mainloop()