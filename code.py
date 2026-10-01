import turtle
import time

screen = turtle.Screen()
screen.title("Ricochet")
screen.bgcolor("#000000")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("#00FFFF")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        new_x = x + 20
        paddle.setx(new_x)
    screen.update()

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        new_x = x - 20
        paddle.setx(new_x)
    screen.update()

screen.listen()
screen.onkey(paddle_right, "Right")
screen.onkey(paddle_left, "Left")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("#FFFFFF")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.penup()
ball.goto(0, 0)

ball_dx = 2
ball_dy = -2

screen.update()

def create_brick(x, y, color):
    brick = turtle.Turtle()
    brick.shape("square")
    brick.color(color)
    brick.shapesize(stretch_wid=1, stretch_len=2)
    brick.penup()
    brick.goto(x, y)
    return brick

bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

for row in range(5):
    for col in range(11):
        x = -350 + col * 70
        y = 250 - row * 30
        brick = create_brick(x, y, colors[row])
        bricks.append(brick)

score = 0

score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.goto(-370, 260)
score_display.hideturtle()
score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

lives = 3

lives_display = turtle.Turtle()
lives_display.color("white")
lives_display.penup()
lives_display.goto(300, 260)
lives_display.hideturtle()
lives_display.write(f"Lives: {lives}", font=("Arial", 16, "normal"))

game_over = False

try:
    while True:
        time.sleep(0.02)
        screen.update()

        if game_over:
            continue

        new_x = ball.xcor() + ball_dx
        new_y = ball.ycor() + ball_dy
        ball.goto(new_x, new_y)

        if ball.xcor() > 390 or ball.xcor() < -390:
            ball_dx *= -1

        if ball.ycor() > 290:
            ball_dy *= -1

        paddle_top = paddle.ycor() + 10

        if ball_dy < 0 and paddle_top <= ball.ycor() <= paddle_top + 10:
            if ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50:
                ball_dy *= -1

        for brick in bricks:
            if abs(ball.xcor() - brick.xcor()) < 35 and abs(ball.ycor() - brick.ycor()) < 15:
                brick.hideturtle()
                bricks.remove(brick)
                ball_dy *= -1
                score += 10
                score_display.clear()
                score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))
                break

        if len(bricks) == 0:
            game_over = True
            score_display.goto(0, 0)
            score_display.write(f"YOU WIN! Final Score: {score}", align="center", font=("Arial", 24, "normal"))

        if ball.ycor() < -280:
            lives -= 1
            lives_display.clear()
            lives_display.write(f"Lives: {lives}", font=("Arial", 16, "normal"))

            if lives == 0:
                game_over = True
                score_display.goto(0, 0)
                score_display.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

            else:
                ball.goto(0, 0)
                ball_dx = 2
                ball_dy = -2

except turtle.Terminator:
    print("Game window closed.")
except Exception:
    print("Game window closed.")
