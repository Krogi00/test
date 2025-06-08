import pygame


WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

def main():
    run = True
    pygame.time.Clock()
    
    while run:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
    
    pygame.quit()
    
if __name__ == '__main__':
    main()