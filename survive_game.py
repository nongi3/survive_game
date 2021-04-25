import pygame
import pygame_menu
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.interface = Interface()
        self.player = Player()
        self.menu = pygame_menu.Menu(width=400, height=500, title='Survive',
                                     theme=pygame_menu.themes.THEME_ORANGE)
        self.create_menu()
        self.menu.mainloop(self.interface.screen)

    def create_menu(self):
        self.player.nick = self.menu.add.text_input('Nick: ',
                                                    default='nongi')
        self.player.nick = self.player.nick.get_value()
        value = self.menu.add.selector('Difficulty: ', [('Easy', 1), ('Medium', 2), ('Hard', 3)],
                                       onchange=self.set_difficulty)
        self.set_difficulty(value.get_value()[0][0], value.get_value()[0][1])
        self.menu.add.button('Play', self.start)
        self.menu.add.button('Exit', pygame_menu.events.EXIT)

    def set_difficulty(self, value, diff):
        if diff == 1:
            self.player.health = 150
        elif diff == 2:
            self.player.health = 100
        elif diff == 3:
            self.player.health = 50

    def start(self):
        while True:
            self.player.move()
            self.interface.draw(self.player)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.player.direction = 'up'
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player.direction = 'down'
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player.direction = 'left'
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player.direction = 'right'
                elif event.type == pygame.KEYUP:
                    self.player.direction = None
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pass

            pygame.display.flip()


class Interface:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        self.map = [
            [1] * 25,
            [1] + [2] * 23 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] + [2] + [3] + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] * 3 + [3] + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] * 3 + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] * 3 + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] * 3 + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] * 3 + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] * 3 + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] * 3 + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] * 3 + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] * 3 + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] * 3 + [2] * 3 + [1],
            [1] + [2] * 15 + [3] + [2] + [3] * 3 + [2] * 3 + [1],
            [1] * 25,
        ]
        self.hp_mp_exp_bar = pygame.image.load('images/hp10_mp10_exp10.png')
        self.background_stone = pygame.image.load('images/background_stone.png')
        self.background_floor = pygame.image.load('images/background_floor.png')
        self.background_tree = pygame.image.load('images/background_tree.png')

    def draw(self, player):
        self.screen.fill((0, 0, 0))
        x = 0
        y = 0
        for i in self.map:
            for j in i:
                if j == 1:
                    self.screen.blit(self.background_stone, (x, y))
                elif j == 2:
                    self.screen.blit(self.background_floor, (x, y))
                elif j == 3:
                    self.screen.blit(self.background_tree, (x, y))
                x += 40
            y += 40
            x = 0
        # font = pygame.font.SysFont('couriernew', 30)
        # text = font.render(f'Nick: {player.nick}    Health = {player.health}',
        #                    True, (255, 0, 0))
        # self.screen.blit(text, (0, 0))

        player.draw(self.screen)


class Player:
    def __init__(self):
        self.x = 120
        self.y = 120
        self.speed = 1
        self.health = 100
        self.nick = 'nongi'
        self.direction = None
        self.sprite = pygame.image.load("images/player.png")

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def move(self):
        if self.direction == 'up':
            if self.y > self.speed + 80:
                self.y -= self.speed
        elif self.direction == 'down':
            if self.y + self.speed < 550:
                self.y += self.speed
        elif self.direction == 'left':
            if self.x > self.speed:
                self.x -= self.speed
        elif self.direction == 'right':
            if self.x + self.speed < 970:
                self.x += self.speed


game = Game()
