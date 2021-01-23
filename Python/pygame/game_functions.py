import sys
import pygame
from bullet import Bullet


#监测键盘
def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


        
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_UP:
        ship.moving_up=True
    elif event.key==pygame.K_DOWN:
        ship.moving_down=True
    elif event.key==pygame.K_q:
        sys.exit()              
        
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key==pygame.K_UP:
        ship.moving_up=False
    elif event.key==pygame.K_DOWN:
        ship.moving_down=False




#图像
def update_screen(ai_settings,screen,ship,alien,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in  bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()

    pygame.display.flip()

#子弹功能
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
