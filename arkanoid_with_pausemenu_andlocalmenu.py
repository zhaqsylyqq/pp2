import pygame
import random

pygame.init()

W, H = 800, 600
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (255, 192, 203)

default_paddle_speed = 20
default_ball_speed = 6

paddle_speed = default_paddle_speed
ball_speed = default_ball_speed

paddleW = 200
paddleH = 25
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

ballRadius = 20
ball = pygame.Rect(random.randrange(ballRadius, W - ballRadius), H // 2, ballRadius, ballRadius)
dx, dy = 1, -1

font = pygame.font.SysFont('comicsansms', 40)
text = font.render('Game Over', True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (W // 2, H // 2)

unbreakable_bricks = [pygame.Rect(10 + 80 * i, 50 + 40 * j, 70, 30) for i in range(10) for j in range(2)]

bonus_brick = pygame.Rect(200, 100, 60, 30)
bonus_active = False

bonus_perks = {
    'speed_up': 3,
    'paddle_shrink': 40 #gpt... :)
}

catch_sound = pygame.mixer.Sound('catch.mp3')


def activate_bonus(perk):
    global ball_speed, paddleW
    if perk == 'speed_up':
        ball_speed += bonus_perks[perk]
    elif perk == 'paddle_shrink':
        paddleW -= bonus_perks[perk]


def main_menu():
    global paddle_speed, ball_speed
    menu_font = pygame.font.SysFont('comicsansms', 30)
    setting_index = 0
    settings = [("Paddle Speed", paddle_speed), ("Ball Speed", ball_speed)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    setting_index = (setting_index - 1) % len(settings)
                elif event.key == pygame.K_DOWN:
                    setting_index = (setting_index + 1) % len(settings)
                elif event.key == pygame.K_LEFT:
                    settings[setting_index] = (settings[setting_index][0], max(1, settings[setting_index][1] - 1))
                elif event.key == pygame.K_RIGHT:
                    settings[setting_index] = (settings[setting_index][0], settings[setting_index][1] + 1)
                elif event.key == pygame.K_RETURN:
                    paddle_speed, ball_speed = settings[0][1], settings[1][1]
                    return
                elif event.key == pygame.K_p:
                    pause_menu() #pause

        screen.fill(bg)
        for i, (setting_name, setting_value) in enumerate(settings):
            color = (0, 255, 0) if i == setting_index else (255, 255, 255)
            text_surface = menu_font.render(f"{setting_name}: {setting_value}", True, color)
            text_rect = text_surface.get_rect(center=(W // 2, H // 2 + i * 50))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(FPS)


def pause_menu(): #pause settings and main menu
    menu_font = pygame.font.SysFont('comicsansms', 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                return

        screen.fill(bg)
        pause_text = menu_font.render('Game Paused', True, (0, 0, 0))
        pause_text_rect = pause_text.get_rect(center=(W // 2, H // 2 - 50))
        resume_text = menu_font.render('Press P to Resume', True, (0, 0, 0))
        resume_text_rect = resume_text.get_rect(center=(W // 2, H // 2 + 50))

        screen.blit(pause_text, pause_text_rect)
        screen.blit(resume_text, resume_text_rect)
        pygame.display.update()
        clock.tick(FPS)


main_menu()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause_menu()

    screen.fill(bg)

    pygame.draw.rect(screen, pygame.Color(234, 250, 177), paddle)
    pygame.draw.circle(screen, pygame.Color(250, 241, 157), ball.center, ballRadius)

    for brick in unbreakable_bricks:
        pygame.draw.rect(screen, pygame.Color(100, 100, 100), brick)

    if bonus_active:
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), bonus_brick)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddle_speed

    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dy = -dy
        catch_sound.play()  # Play catch sound

    for brick in unbreakable_bricks:
        if ball.colliderect(brick):
            dx, dy = -dx, -dy

    if bonus_active and ball.colliderect(bonus_brick):
        bonus_active = False
        activate_bonus(random.choice(list(bonus_perks.keys())))

    if ball.y > H or ball.x > W:
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)

    pygame.display.update()
    clock.tick(FPS)
