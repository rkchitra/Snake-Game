import turtle
import time  
import random
import winsound

delay = 0.1

wn = turtle.Screen()
wn.title("Snake")
wn.setup(height=600,width=600)
wn.tracer(0)
wn.bgcolor("black")

#snake 
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
shapes = random.choice(['square','circle','triangle'])
food.shape(shapes)
colors = random.choice(['red','green','blue'])
food.color(colors)
food.penup()
food.goto(0,100)

segments = [] #for the body; add a segment to the snake whenever the head touches food

#Display game over message 
disp = turtle.Turtle()
disp.speed(0)
disp.hideturtle()
disp.penup()
disp.color("white")
disp.goto(-10,0)

cur_score = 0
#score 
score = turtle.Turtle()
score.speed(0)
score.hideturtle()
score.penup()
score.color("white")
score.goto(-10,260)
score.write("Score: 0",align="center", font=("Courier",24,"normal"))

#Functions

def go_left() :
    if snake.direction != "right" :
        snake.direction = "left"
def go_right() :
    if snake.direction != "left" :
        snake.direction = "right"
def go_up() :
    if snake.direction != "down" :
        snake.direction = "up"
def go_down() :
    if snake.direction != "up" :
        snake.direction = "down"

def move() :
    if snake.direction == "up" :
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down" :
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left" :
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right" :
        x = snake.xcor()
        snake.setx(x + 20)
def game_over() :
    snake.direction = "stop"
    global running
    running = False
    winsound.PlaySound("game_over.wav",winsound.SND_ASYNC)
    disp.write("Game Over!",align="center", font=("Courier",30,"normal"))
    
    

#Keyboard Bindings 
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(game_over,"q")

running = True
while running:
    wn.update()

    #Collision 
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290 :
        game_over()
        break
    
    #Collision with body 
    for segment in segments :
        if segment.distance(snake) < 20 :
            game_over()
            break

    #Collision with food 
    if snake.distance(food) < 20 :
        #Play music
        winsound.PlaySound("eating.wav",winsound.SND_ASYNC) 
        #Update score 
        cur_score += 1
        score.clear()
        score.write("Score: {}".format(cur_score),align="center", font=("Courier",24,"normal"))
        #Move the food to a random spot on the screen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        shapes = random.choice(['square','circle','triangle'])
        food.shape(shapes)
        colors = random.choice(['red','green','blue'])
        food.color(colors)
        food.goto(x,y)

        #Add a segment 
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    #Move segments in reverse order 
    for index in range(len(segments)-1,0,-1) :
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #Move segment 0 
    if len(segments) > 0 :
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)
    move()
    time.sleep(delay)

wn.mainloop()