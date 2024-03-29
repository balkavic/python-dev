import sys, pygame
pygame.init()



size = width, height = 1200, 800
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

moving = True

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()



def toggle_move():
    global speed
    global moving
    if moving:
        speed = [0, 0]
        moving = False
    else:
        speed = [1, 1]
        moving = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            toggle_move()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()





