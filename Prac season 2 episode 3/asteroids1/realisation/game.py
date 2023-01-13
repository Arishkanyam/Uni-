import pygame
from config import *
from asteroid import Asteroid
from bullet import Bullet
from spaceship import Player
from explosion import Explosion

pygame.init()

c = pygame.display.set_mode((sw, sh))  
fps_counter = pygame.time.Clock()  #counting fps

gameover = False  #check if loose

score = 0  
highestscr = 0  
lives = start_lives


def redrawGameWindow():  # обновление окна
    c.blit(bg, (0, 0))  # задний фон обновляем
    font = pygame.font.SysFont('Calibri', 30)  # шрифт
    Ltext = font.render('Lives left: ' + str(lives), 1, (255, 255, 255))  # отображение жизней
    Replaytext = font.render("Press 'ENTER' to Play Again", 1, (255, 255, 255))  # текст начать сначала
    Stext = font.render('Score: ' + str(score), 1, (255, 255, 255))  # отображение очков
    HStext = font.render('Record: ' + str(highestscr), 1, (255, 255, 255))  # отображение рекорда

    player.draw(c)  # отрисовываем игрока
    for a in asteroids:  # отрисовываем все астероиды
        a.draw(c)
    for b in playerBullets:  # отрисовываем все снаряды
        b.draw(c)
    for d in explosions:  # отрисовываем все взрывы
        d.draw(c)

    if gameover:  # если проиграли, то выводим текст
        c.blit(Replaytext, (sw // 2 - Replaytext.get_width() // 2, sh // 2 - Replaytext.get_height() // 2))

    c.blit(Stext, (sw - Stext.get_width() - 25, 25))  # обновляем очки
    c.blit(Ltext, (25, 25))  # обновляем жизни
    c.blit(HStext, (sw - HStext.get_width() - 25, 35 + Stext.get_height()))  # обновлячем рекорд
    pygame.display.update()  # запуск перерисовки экрана


player = Player()  # объект игрока
playerBullets = []  # список снарядов на сцене
asteroids = []  # список астероидов на сцене
explosions = []  # список взрывов на сцене
count = 0  # счетчик времени

run = True
while run:
    fps_counter.tick(fps)  # привязываемся к ФПС

    count += 1
    if not gameover:
        if count % asteroid_spawn_delay == 0:  # каждые n тиков добавляем новый астероид
            asteroids.append(Asteroid())

        player.updateLocation()  # тороидальное перемещение
        for b in playerBullets:  # обновляем снаряды
            b.move()  # передвигаем снаряд
            if b.outside() or b.checkdist():  # если вышел за экран или пролетел максимальное расстоянме
                playerBullets.pop(playerBullets.index(b))  # то удаляем его

        for a in asteroids:  # проверяем астероиды
            a.x += a.xv  # двигаем астероид по Х
            a.y += a.yv  # двигаем астероид по У
            # Проверяем столкновение игрока и астероида
            if (a.x >= player.x - player.w // 2 and a.x <= player.x + player.w // 2) or (
                    a.x + a.w <= player.x + player.w // 2 and a.x + a.w >= player.x - player.w // 2):
                if (a.y >= player.y - player.h // 2 and a.y <= player.y + player.h // 2) or (
                        a.y + a.h >= player.y - player.h // 2 and a.y + a.h <= player.y + player.h // 2):
                    lives -= 1  # если столкнулись то отнимаем жизнь
                    asteroids.pop(asteroids.index(a))  # удаляем астероид
                    explosions.append(Explosion(a))  # добавляем взрыв

                    asteroids.clear()  # очищаем поле
                    player.respawn()  # возвращем игрока в центр
                    break

            for b in playerBullets:  # проверяем пули
                # проверяем столкновение пули и астероида
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                    if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                        # если есть столкновение
                        score += score_per_hit  # то прибавлячем очко
                        asteroids.pop(asteroids.index(a))  # удаляем астероид
                        playerBullets.pop(playerBullets.index(b))  # удаляем пулю
                        explosions.append(Explosion(a))  # добавляем взрыв
                        break

        if lives <= 0:  # если закончились жизни то включаем gameover
            gameover = True

        keys = pygame.key.get_pressed()  # получаем список нажатых клавиш
        if keys[pygame.K_LEFT]:  # кнопка влево
            player.turnLeft()
        if keys[pygame.K_RIGHT]:  # кнопка вправо
            player.turnRight()
        if keys[pygame.K_UP]:  # кнопка вверх
            player.accel = 0.5  # добавляем ускорения
            player.isTorque = True  # включаем анимацию огня
            player.moveForward()  # передвигаем корабль
        else:  # если кнопка не нажата
            player.accel = 0  # ускорение ноль чтоб корабль тормозил
            player.isTorque = False  # выключаем огонь
            player.moveForward()  # передвигаем

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:  # если нажали пробел
            if event.key == pygame.K_SPACE:
                if not gameover:  # если игра идет
                    playerBullets.append(Bullet(player))  # выстрел

            if event.key == pygame.K_RETURN:  # нажимаем enter для продолжения игры
                if gameover:
                    gameover = False  # выключаем gameover
                    lives = start_lives  # обновляем жизни
                    asteroids.clear()  # очищаем поле
                    player.distance = 0  # убираем скорость у корабля
                    player.respawn()  # перемещаем в центр

                    if score > highestscr:  # если побили рекорд
                        highestscr = score  # обновляем
                    score = 0  # обнуляем очки

    redrawGameWindow()  # перерисовываем окно
pygame.quit()