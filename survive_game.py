import pygame
import pygame_menu
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.interface = Interface()
        self.player = Player()
        self.menu = pygame_menu.Menu(width=300, height=400, title='Survive',
                                     theme=pygame_menu.themes.THEME_ORANGE)
        self.create_menu()
        self.menu.mainloop(self.interface.screen)
        

    def create_menu(self):
        self.player.nick = self.menu.add.text_input('Nick: ',
                                                    default='nongi')
        self.player.nick = self.player.nick.get_value()
        value=self.menu.add.selector('Difficulty: ', [('Easy', 1), ('Medium', 2), ('Hard', 3)],
                               onchange=self.set_difficulty)
        self.set_difficulty(value.get_value()[0][0], value.get_value()[0][1])
        self.menu.add.button('Play', self.start)
        self.menu.add.button('Exit', pygame_menu.events.EXIT)

    
    def set_difficulty(self, value, diff):
        if diff ==  1:
            self.player.health = 150
        elif diff == 2:
            self.player.health = 100
        elif diff == 3:
            self.player.health = 50


    def start(self):
        self.interface.screen.fill((0,0,0))
        while True:
            self.interface.draw(self.player)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.direction = 'up'
                    elif event.key == pygame.K_DOWN:
                        self.player.direction = 'down'
                    elif event.key == pygame.K_LEFT:
                        self.player.direction = 'left'
                    elif event.key == pygame.K_RIGHT:
                        self.player.direction = 'right'
                elif event.type == pygame.KEYUP:
                    self.player.direction = None
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pass

            pygame.display.flip()



class Interface:
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
    def draw(self, player):
        font = pygame.font.SysFont('couriernew', 30)
        text = font.render(f'Nick: {player.nick}    Health = {player.health}',
                           True, (255,0,0))
        self.screen.blit(text, (0, 0))

        player.draw(self.screen)


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.health = 100
        self.nick = 'nongi'
        self.direction = None
        self.sprite = pygame.image.load("player.png")

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

game = Game()
