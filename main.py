import turtle

screen=turtle.Screen()
image="indian_map.gif"
screen.addshape(image)
turtle.shape(image)

# def coor(x,y):
# 	print(x,y)

# turtle.onscreenclick(coor)
# turtle.mainloop()


import pandas 
data = pandas.read_csv("states_data.csv")
all_states=data.state.to_list()



missed_state=[]
guessed_state=[]
while len(guessed_state) < 28:
	answer=screen.textinput(title=f"{len(guessed_state)}/28 States Correct", prompt="What is the another state's name").title()

	if answer == "Exit":
		for miss in all_states:
			if miss not in guessed_state:
				missed_state.append(miss)
		to_learn=pandas.DataFrame(missed_state)
		to_learn.to_csv("States_To_Learn")

		break 
	if answer in all_states:
		guessed_state.append(answer)
		t=turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data=data[data.state==answer]
		t.goto(state_data.x.item(), state_data.y.item())
		t.write(state_data.state.item(), font=("Arial", 10, "bold"))

