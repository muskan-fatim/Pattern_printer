import turtle

# Setup turtle
t = turtle.Turtle()
t.speed(1)
screen = turtle.Screen()
screen.bgcolor("white")

print("Pattern Printer")
print("Choice of shape:", {"pyramid", "square", "circle", "rectangle"})

# Get user input
choice = input("Enter your choice: ").lower()
try:
    number_row = int(input("Enter number of rows: "))
except Exception as e:
    print("Enter a valid number for rows:", str(e))
    turtle.bye()
    exit()

# Function to draw a square
def draw_square(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(40)
        t.right(90)

# Function to draw a rectangle
def draw_rectangle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(60)
        t.right(90)
        t.forward(30)
        t.right(90)

# Function to draw a circle
def draw_circle(x, y):
    t.penup()
    t.goto(x, y - 20)  # Move to start circle centered
    t.pendown()
    t.circle(20)

# Function to draw a pyramid with triangles
def draw_pyramid_row(x, y, count):
    for i in range(count):
        t.penup()
        t.goto(x + i * 45, y)
        t.pendown()
        for _ in range(3):
            t.forward(40)
            t.left(120)

# Draw pattern based on user choice
start_x = -number_row * 25
start_y = 200

for row in range(number_row):
    count = row + 1
    y = start_y - row * 50
    x = start_x - row * 20  # to center align

    if choice == "square":
        for i in range(count):
            draw_square(x + i * 50, y)
    elif choice == "rectangle":
        for i in range(count):
            draw_rectangle(x + i * 70, y)
    elif choice == "circle":
        for i in range(count):
            draw_circle(x + i * 50, y)
    elif choice == "pyramid":
        draw_pyramid_row(x, y, count)
    else:
        print("Invalid choice")
        break

t.hideturtle()
turtle.done()
