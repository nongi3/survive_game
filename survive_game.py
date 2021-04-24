import pygame
import pygame_menu
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.interface = Interface()
        self.player = Player()
        self.menu = pygame_menu.Menu(300, 400, 'Survive',
                                     theme=pygame_menu.themes.THEME_ORANGE)
        self.create_menu()
        self.menu.mainloop(self.interface.screen)
        

    def create_menu(self):
        self.player.nick = self.menu.add.text_input('Nick: ',
                                                    default='nongi')
        self.player.nick = self.player.nick.get_value()
        self.menu.add.button('Play', self.start)
        self.menu.add.button('Exit', pygame_menu.events.EXIT)

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
                        pass
                    elif event.key == pygame.K_DOWN:
                        pass
                    elif event.key == pygame.K_LEFT:
                        pass
                    elif event.key == pygame.K_RIGHT:
                        pass
                elif event.type == pygame.KEYUP:
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
    
    # отрисовка поля
    # здоровье/патроны/номер уровня (информация)
    # двери


class Player:
    def __init__(self):
        self.health = 100
        self.nick = 'nongi'


game = Game()
