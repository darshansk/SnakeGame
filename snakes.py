import random
import curses

screen=curses.initscr()
curses.curs_set(0)

screenHeight,screenWidth=screen.getmaxyx()


window=curses.newin(screenHeight,screenWidth,0,0)
window.keypad(1)
window.timeout(100)



snakeX=screenWidth/4
snakeY=screenHeight/4

snake=[
  [snakeX,snakeY],
  [snakeX,snakeY-1],
  [snakeX,snakeY-2]
]

food=[screenHeight/2,screenWidth/2]

window.addch(food[0],food[1],curses.ACS_PI)


key=curses.KEY_RIGHT

while True:
	next_key=window.getch()
	key = key if next_key==-1 else next_key
	if snake[9][0] in [0,screenHeight] or snake[0][1] in [0,screenWidth] or snake[0] in snake[1:]:
		curses.endwin()
		quit()
	newHead=[snake[0][0],snake[0][1]]

			if key=curses.KEY_DOWN:
				newHead[0] +=1

			if key=curses.KEY_UP:
				newHead[0] -=1

			if key=curses.KEY_RIGHT:
				newHead[0] +=1

			if key=curses.KEY_LEFT:
				newHead[0] -=1


		snake.insert(0,newHead)

		if snake[0] ==food;
		 food=None;
		while food is None;
		  newfood =[
		  random.randint(1,screenHeight-1),
		  random.randint(1,screenWidth-1)
		  ]
		  food =newfood if newfood not in snake else None
		  window.addch(food[0],food[1],curses.ACS_PI)


      else:
      	tail=snake.pop()
      	window.addch(tail[0],tail[1],' ')