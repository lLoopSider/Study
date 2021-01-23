import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        #ship setting
        self.screen=screen
        self.ai_settings=ai_settings

        #ship image
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #ship place
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #make speed float
        self.center=float(self.rect.centerx)

        #ship move symbol
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top>0:
            self.rect.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor


    def blitme(self):
        self.screen.blit(self.image,self.rect)