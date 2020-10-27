import config
import snake
import scores
import food
import os

#apple_image = None


def end_screen():
    background(150)
    fill(255)
    textSize(64)
    text(config.GAME_OVER_MESSAGE, config.WINDOW_WIDTH / 2 - len(config.GAME_OVER_MESSAGE) * 20, config.WINDOW_HEIGHT / 2)
    if scores.score > scores.highscore:
        text(config.HIGHSCORE_BEATED_MESSAGE, config.WINDOW_WIDTH / 2 - len(config.HIGHSCORE_BEATED_MESSAGE) * 17, config.WINDOW_HEIGHT / 4)


def setup():
    size(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    frameRate(10)
    
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            scores.highscore = int(file.read())
    food.food_img = loadImage("images/apple.png")
    
def draw():
    background(0)
    snake.show()
    snake.move()
    food.show()
    scores.show()
    
    if snake.touches_food():
        snake.eat_food()
        food.reset()
        scores.increase()
        
    if snake.eat_self():
        print("GAME OVER!")
        end_screen()
        scores.update_highscore()
        noLoop()
    
    #image(apple_image, food.food_pos[0], food.food_pos[1], config.SCALE, config.SCALE)
    
def keyPressed():
    if keyCode == UP:
        if config.CURRENT_DIR != 'down':
            config.CURRENT_DIR = 'up'
    elif keyCode == RIGHT:
        if config.CURRENT_DIR != 'left':
            config.CURRENT_DIR = 'right'
    elif keyCode == DOWN:
        if config.CURRENT_DIR != 'up':
            config.CURRENT_DIR = 'down'
    elif keyCode == LEFT:
        if config.CURRENT_DIR != 'right':
            config.CURRENT_DIR = 'left'
    
