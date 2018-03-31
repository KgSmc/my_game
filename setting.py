from random import randint
class Setting():
    '''存储《外星人入侵》的所有设置类'''
    def __init__(self):
        '''初始化游戏的静态设置'''
        #屏幕设置
        self.screen_width = 1400
        self.screen_height = 760
        self.bg_color = (230,230,230)

        #飞船设置
        self.ship_limit = 3

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255,77,77
        self.bullets_allowed = 5

        #外星人设置
        self.fleet_drop_speed = 10

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #外星人点数提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        self.random_number = randint(4,10)


    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #记分
        self.alien_points = 50

        #fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1
    def increase_speed(self):
        '''提高速度设置和外星人点数'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)




