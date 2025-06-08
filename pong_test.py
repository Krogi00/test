import pygame

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game, PonG!")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20
FPS = 60
BALL_RADIUS = 10

class Paddle:

    COLOR = WHITE
    VEL = 5
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win,self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
    
class Ball:
    COLOR = WHITE
    MAX_VEL = 10

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
        
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        
def handle_paddle_movement(ball, left_player, right_player):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_player.y and ball.y <= left_player.y + left_player.height:
            if ball.y + ball.radius <= left_player.x + left_player.width:
                ball.y_vel *= -1
    else:
        if ball.y >= right_player.y and ball.y <= right_player.y + left_player.height:
            if ball.y + ball.radius >= right_player.x:
                ball.y_vel *= -1

def handle_paddle_movement(keys, left_player, right_player):
    if keys[pygame.K_w] and left_player.y - left_player.VEL >= 0:
        left_player.move(up=True)
    if keys[pygame.K_s] and left_player.y + left_player.height + left_player.VEL <= HEIGHT:
        left_player.move(up=False)

    if keys[pygame.K_UP] and right_player.y - right_player.VEL >= 0:
        right_player.move(up=True)
    if keys[pygame.K_DOWN] and right_player.y + right_player.height +left_player.VEL <= HEIGHT:
        right_player.move(up=False)

def draw(win, players, ball):
    win.fill(BLACK)

    for player in players:
        player.draw(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//40))
    ball.draw(win)

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    

    left_player = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_player = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

    while run:
        clock.tick(FPS)

        draw(WIN, [left_player, right_player], ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_player, right_player)
        ball.move()
        handle_paddle_movement(ball, left_player, right_player)

    pygame.quit()


if __name__ == '__main__':
    main()
