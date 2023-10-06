# First we import Turtle, a simple builtin python game library
import turtle
import time
import winsound



# We need to create a window, the capitalization of Screen is important
wn = turtle.Screen()  # loading screen
wn.title("Pong by TTPanta")  # Giving a title name
wn.bgcolor("black")  # Setting up the background color
wn.setup(width=800, height=600)  # Configuring the resolution of the screen
wn.tracer(0)  # it has something to do with animation, I don't know what but since the tutorial kept it off, so will I
# Paddle A
paddle_a = turtle.Turtle()  # .Turtle() here is a turtle object
paddle_a.speed(0)  # .speed() is the speed of the animation
paddle_a.shape("square")  # "square is a built-in shape in the turtle module
paddle_a.shapesize(stretch_wid=5, stretch_len =1)  # by default, the shape is 20x20 pixels
paddle_a.color("white")
paddle_a.penup()  # .penup() won't draw the line which turtle objects draw by default
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 3 # dx or delta x means the rate of change of x-coordinate
ball.dy = 3 # Adjust the dx and dy to increase the speed of the ball

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

# Pen 2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, -260)
pen2.write("Player A: w = up, s = down", align="center", font=("Courier", 15, "normal"))

# Pen 3
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.color("white")
pen3.penup()
pen3.hideturtle()
pen3.goto(0, -240)
pen3.write("Player B: up button = up, down button = down", align= "center", font=("Courier", 15, "normal"))

# another pen
pen4 = turtle.Turtle()
pen4.speed(0)
pen4.color("white")
pen4.penup()
pen4.hideturtle()
pen4.goto(0, 200)
pen4.write("time remaining: 90 seconds", align= "center", font=("Courier", 10, "normal"))

# sighs, yet again another pen
pen5 = turtle.Turtle()
pen5.speed(0)
pen5.color("white")
pen5.penup()
pen5.hideturtle()
pen5.goto(0, 0)


# Time limit
start_time = time.time()
time_limit = 90

# Function
def paddle_a_up():
    if paddle_a.ycor() < 250:  # border configuration for the paddles
        y = paddle_a.ycor()  # .ycor() gives the current y coordinate
        y += 20  # we set the amount of movement we want when it goes up
        paddle_a.sety(y)  # updates the y-coordinate with the one we provide
def paddle_a_down():
    if paddle_a.ycor() > -240:
         y = paddle_a.ycor()
         y -= 20
         paddle_a.sety(y)

def paddle_b_up():
    if paddle_b.ycor() < 250:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() > -240:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)
# def speed_increase():
#     ball.dx *= 1.1
#     ball.dy *= 1.1
def final_game():
    if score_a > score_b:
        pen5.write("Time's up! Player A wins, Thanks for playing", align="center", font=("Courier", 15, "normal"))
    elif score_a < score_b:
        pen5.write("Time's up! Player B wins, Thanks for playing", align="center", font=("Courier", 15, "normal"))
    else:
        pen5.write("Time's up! Its a draw!, Thanks for playing", align="center", font=("Courier", 15, "normal"))


# Keyboard binding
wn.listen()  # This will basically check for inputs and events from the keyboard
wn.onkeypress(paddle_b_up, "Up")  # .onkeypress() is a method that has a function and keyboard key as parameters
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_a_down, "s")

score_a = 0
score_b = 0
flag = False

# Main game loop (Every game needs this, this is where our game will run)
while True:
    wn.update()
    time.sleep(0.01) # This is basically a delay. A delay of 0.01 seconds
    elapsed_time = round(time.time() - start_time)
    pen4.clear()
    pen4.write("time passed: {} seconds, max time: 90s, first to score 5 wins".format(elapsed_time), align="center", font=("Courier", 12, "normal"))
    if flag == True:
        time.sleep(6)
        break
    if elapsed_time == time_limit:
        final_game()
        flag = True

    if score_a == 5:
        pen5.write("Player A wins, Player B will wash the dishes", align="center", font=("Courier", 12, "normal"))

        flag = True

    elif score_b == 5:
        pen5.write("Player B wins, Player A will now watch Boku no Pico", align="center", font=("Courier", 12, "normal"))

        flag = True
    else:
        pass

    # movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Increase in speed of the ball
    # if elapsed_time == 4: #This glitches for some reason so I am just removing this
    #     speed_increase()
    #     time.sleep(0.1)

    # border config
    if ball.ycor() > 290:  # ycor() gives the y-coordinate
        ball.sety(290)  # sety() updates the y-coordinate
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 450:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -450:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # Ball and Paddle collision
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() - 55 ):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55 ):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
