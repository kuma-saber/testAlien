class Settings:
    """存储游戏中所有设置的类。"""

    def __init__(self):
        """初始化游戏的静态设置。"""
        # 屏幕设置。
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 30, 30)

        # 飞船设置。
        self.ship_limit = 3

        # 子弹设置。
        self.bullet_width = 15
        self.bullet_height = 7
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 20

        # 外星人设置。
        self.fleet_drop_speed = 10

        # 加快游戏节奏的速度。
        self.speedup_scale = 1.1
        
        # 外星人分数的提高速度。
        self.score_scale = 1.5
        
<<<<<<< HEAD
=======
        # 音效设置
        # self.bullet_sound = pygame.mixer.Sound("../sounds/bullet.wav")
        # self.super_bullet_sound = pygame.mixer.Sound("../sounds/super_bullet.wav")
        # self.ship_hit_sound = pygame.mixer.Sound("../sounds/ship_hit.wav")
        # self.start_new_level_sound = pygame.mixer.Sound("../sounds/start_new_level.wav")
        # self.super_mode_sound = pygame.mixer.Sound("../sounds/super_mode.wav")
        # self.gameover_sound = pygame.mixer.Sound("../sounds/gameover.wav")
        # self.recordbroken_sound = pygame.mixer.Sound("../sounds/recordbroken.wav")
        
>>>>>>> 49bc790eee7c9dccf112f83afad694180a23ce7e
        # 初始化游戏动态设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置。"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.5

<<<<<<< HEAD
        # fleet_direction为1表示向下，为-1表示向上。
=======
        # fleet_direction为1表示向右，为-1表示向左。
>>>>>>> 49bc790eee7c9dccf112f83afad694180a23ce7e
        self.fleet_direction = 1

        # 记分。
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置。"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
