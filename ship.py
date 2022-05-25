import pygame
 
from pygame.sprite import Sprite
 
class Ship(Sprite):
    """管理飞船的类。"""
 
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置。"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形。
<<<<<<< HEAD
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕左边缘的中央。
=======
        self.image = pygame.image.load('Alien/scoring/images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央。
>>>>>>> 49bc790eee7c9dccf112f83afad694180a23ce7e
        # self.rect.midbottom = self.screen_rect.midbottom
        self.rect.midleft = self.screen_rect.midleft

        # 在飞船中的属性x中存储小数值。
        self.x = float(self.rect.x)
        
        # 在飞船中的属性y中存储小数值。
        self.y = float(self.rect.y)
        
        # 移动标志。
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
<<<<<<< HEAD
=======
        # 无敌标志
        # self.super_mode = False
>>>>>>> 49bc790eee7c9dccf112f83afad694180a23ce7e

    def update(self):
        """根据移动标志调整飞船位置。"""
        # 更新飞船而不是rect对象的x值。
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
            
         # 更新飞船而不是rect对象的y值
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        
        # 根据self.x更新rect对象。
        self.rect.x = self.x
        
        # 根据self.y更新rect对象
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船。"""
<<<<<<< HEAD
        self.screen.blit(self.image, self.rect)  
=======
        self.screen.blit(self.image, self.rect)
        
        # if self.super_mode:
        #     # 无敌模式，绘制金色边框
        #     pygame.draw.rect(self.screen, (200, 200, 0),(self.rect), 2)
>>>>>>> 49bc790eee7c9dccf112f83afad694180a23ce7e

    def center_ship(self):
        """让飞船在屏幕底部边缘"""
        # self.rect.midbottom = self.screen_rect.midbottom
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    