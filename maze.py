from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        
        if keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed

        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed


class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 420:
            self.direction = "right"

        if self.rect.x >= 600:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed

        if self.direction == "right":
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"),(700, 500))

win_width = 700
win_height = 500

player = Player("hero.png", 80, win_height - 80, 5)
monster = Enemy("cyborg.png", 420, 310, 2)
final = GameSprite("treasure.png",230, 360, 0)

w1 = Wall(128, 0, 0, 20, 30, 500, 17)
w2 = Wall(128, 0, 0, 20, 47, 20, 373)
w3 = Wall(128, 0, 0, 520, 30, 140, 17)
w4 = Wall(128, 0, 0, 30, 100, 390, 10)
w5 = Wall(128, 0, 0, 640, 40, 20, 420)
w6 = Wall(128, 0, 0, 180, 440, 460, 20)
w7 = Wall(128, 0, 0, 180, 200, 20, 240)
w8 = Wall(128,0, 0, 200, 230, 320, 20)
w9 = Wall(128, 0, 0, 200, 327, 210, 13)

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

font.init()
font = font.SysFont("Arial", 70)
win = font.render('YOU WIN', True, (255, 0, 0))
lose = font.render('YOU LOSE', True, (255, 215, 0))

finish = False

 

game = True
FPS = 60
clock = time.Clock()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))

        monster.update()
        player.update()


        player.reset()
        final.reset()
        monster.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()

        if sprite.collide_rect(player,final):
            finish = True
            window.blit(win, (200,200))
            money.play()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9):
            finish = True
            window.blit(lose, (200,200))
            kick.play()


    display.update()
    clock.tick(FPS)