import random
import pygame
import os

pygame.init()
pygame.mixer.init()


#Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#Creating Window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))


# Game Title
pygame.display.set_caption("SnakeWithHarry")
pygame.display.update()
 
#background image


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)
    
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake (gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
               
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((0,160,70))
        text_screen("Welcome to Snakes", white, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)

        for event in pygame.event.get():
            pygame.mixer.music.load('sound\\welcome.wav')
            pygame.mixer.music.play()
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('sound\\background music.mp3')
                    pygame.mixer.music.play(-1)
                    gameLoop()
        pygame.display.update()
        clock.tick(60)

#Game loop
def gameLoop():
    #game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, int(screen_width/2))
    food_y = random.randint(20, int(screen_width/2))
    score = 0
    init_velocity = 10
    snake_size = 20
    fps = 30
    snake_list = []
    snake_length = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                    f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('sound\\background music.mp3')
                        pygame.mixer.music.play(-1)
                        gameLoop()


        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # snake_x = snake_x + 10
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        # snake_x = snake_x - 10
                        velocity_x = -init_velocity
                        velocity_y = 0
                    
                    if event.key == pygame.K_UP:
                        # snake_y = snake_y - 10
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        # snake_y = snake_y + 10
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs (snake_x-food_x)<20 and abs(snake_y - food_y)<20:
                score+=10
                print("Score: ",score)

                food_x = random.randint(20, int(screen_width/2))
                food_y = random.randint(20, int(screen_width/2))
                snake_length+=5
                if score > int(hiscore):
                    hiscore = score


            gameWindow.fill(white)
            
            text_screen("Score: "+ str(score) + "  Hiscore: "+ str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                pygame.mixer.music.load('sound\cry.mp3')
                pygame.mixer.music.play()
                game_over = True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('sound\Hitloud.wav')
                pygame.mixer.music.play()
                print("Game Over")
                
            plot_snake(gameWindow, black, snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    quit()

welcome()
gameLoop()