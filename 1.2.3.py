#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height=-200
apple_letter_x_offset = -25
apple_letter_y_offset= -50

screen_width = 400
screen_height = 400 
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

wn.bgpic("tree.gif")
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

#new
def reset_apple(active_apple):
  length_of_list = len(letter_list)
  if (length_of_list !=0):
    index = rand.randint(0, length_of_list)
    active_apple.goto(rand.randint(-(screen_width)/2, screen_width/2),rand.randint(-(screen_height)/2,(screen_height)/2))
    draw_apple(active_apple,letter_list.pop(index))
  wn.update()

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(active_apple, letter)
  wn.update()

#drops apple and hides it 
def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)

#letter is of type
#active apple is a turtle
def draw_letter(active_apple, letter):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial",74, "bold"))
  active_apple.setpos(remember_position)

'''
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

turtle_list = []

temp_turtle = trtl.Turtle()
temp_turtle.pencolor("red")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("blue")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("green")
turtle_list.append(temp_turtle)

print(turtle_list)

turtle_list[0].forward(500)
turtle_list[1].setheading(45)
turtle_list[1].forward(500)
turtle_list[2].setheading(315)
turtle_list[2].forward(500)
turtle_list[3].setheading(turtle_list[0].heading()+180)
turtle_list[3].forward(500)
turtle_list[4].forward(400)
'''

draw_apple(apple, "A")
wn.onkeypress(drop_apple, "a")

wn.listen()
trtl.mainloop()