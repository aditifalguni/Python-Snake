import tkinter #graphical user interface library 
import random  #randomly placinf food in differbt location each time 

#define constants for the window 
ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS #25*25 = 625
WINDOW_HEIGHT = TILE_SIZE * ROWS #25*25 = 625

#7. Tile class -> for storing the x,y position
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#1.game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

#3.Canvas to draw on (master-> window)
canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update() #add the canvas to the window 

#4.center the window; otherwise, the window opens up on the screen on different spaces everytime
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#5. calculate X, Y position
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#6.add X,Y to teh window  
# format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#8.initialize game
snake = Tile(TILE_SIZE * 5, TILE_SIZE * 5) #single tile, snake's head
food = Tile(TILE_SIZE * 10, TILE_SIZE * 10)

#11. Key listener for moving the snake
velocityX = 0 # snake is not moving 
velocityY = 0

#18. list for storing all teh body parts 
snake_body = [] #multiple snake tiles

#23. Gameover 
game_over = False

#25.Score
score = 0

#13. game loop
def change_direction(e): #e = event
    # print(e)
    # print(e.keysym)# able to register, which key have been pressed 
    #key symbol

    global velocityX, velocityY, game_over
    if (game_over):
        return #edit this code to reset game variables to play again

#while pressing a key, mae sure not gong to the opposite direction
#in a game of snake mouth cannot go towards the tail 
    if (e.keysym == "Up" and velocityY != 1):# while going up, not going down 
        velocityX = 0
        velocityY = -1
        
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1

    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0

    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0

#24. if gameover, the snake won't respond to key presses, snake will stop moving
def move():
    global snake, food, snake_body, game_over, score
    if (game_over):
        return
    #cross the bouderies of the window 
    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return
    #21. Move the snake body with the head
    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return
    
    #19.collision -> x,y pos of teh food and snake are the same 
    if (snake.x == food.x and snake.y == food.y): 
        #when this happens add a segment to the body 
        snake_body.append(Tile(food.x, food.y))
        #then move the food to another random location 
        food.x = random.randint(0, COLS-1) * TILE_SIZE #from 0 to 24
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1

    #22. update snake body
    #move the snakes body starting from the back 
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if (i == 0):#tile that is at the start of a snake's body, right before ethe snakes head
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

 #14. if not multiplied by tile size,it moves per pixel size 
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

#start drawing, draw function is called 10 times a second->  window.after(100, draw)
def draw():
    global snake, food, snake_body, game_over, score

    #15. 
    move() #call move function before drwaing the snake
    #calling move within draw function-> snake moves 10 frames per sec 
    
    #16.clear the previous frame everytime after drawing the new frame, otherwise gets overlapped
    canvas.delete("all")

    #17. draw the food first, so it doesn't cover the snake when tehy collide 
    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = 'red')

    #9. draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = 'green')

    #20.add snake body 
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = 'lime green')
 
   #26. draw GAME OVER & SCORE 
    if (game_over):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font = "Arial 20", text = f"Game Over: {score}", fill = "white")
    else:
        canvas.create_text(30, 20, font = "Arial 10", text = f"Score: {score}", fill = "white")
    
    #10. loop the snake
    window.after(100, draw) #call draw again every 100ms (1/10 of a second) = 10 frames per second

#12. key listener
draw()
window.bind("<KeyRelease>", change_direction) #when you press on any key and then let go

#2.keeps teh window open
window.mainloop() #used for listening to window events like key presses
