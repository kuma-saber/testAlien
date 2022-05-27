class Settings:
    """存储游戏中所有设置的类。"""

    def __init__(self):
        """初始化游戏的静态设置。"""
        # 屏幕设置。
        self.screen_width = 1200
        self.screen_height = 800
        # 黑色背景
        self.bg_color = (30, 30, 30)

        # 飞船数量设置。
        self.ship_limit = 3

        # 子弹大小设置。
        self.bullet_width = 15
        self.bullet_height = 7
        # 子弹颜色设置。
        self.bullet_color = (255, 255, 255)
        # 可发射子弹数目。
        self.bullets_allowed = 20

        # 外星人设置。
        self.fleet_drop_speed = 10

        # 加快游戏节奏的速度。
        self.speedup_scale = 1.2
        
        # 外星人分数的提高速度。
        self.score_scale = 1.5
        
        # 初始化游戏动态设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置。"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.5

        # fleet_direction为1表示向下，为-1表示向上。
        self.fleet_direction = 1

        # 击杀一个外星人分数。
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置。"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        # 击杀外星人分数翻倍
        self.alien_points = int(self.alien_points * self.score_scale)
