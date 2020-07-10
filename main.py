import pygame
from pygame.locals import *

# ボタンの変換
button_key = [4, 2, 0, 5, -1, 1, 3, -1, -1]

# ボタンの画像
img = pygame.image.load("water.png")
img = pygame.transform.scale(img, (50, 80))
img2 = pygame.image.load("black.png")
img2 = pygame.transform.scale(img2, (50, 80))

# ジョイスティックの初期化
pygame.joystick.init()
try:
    # ジョイスティックインスタンスの生成
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print('ジョイスティックの名前:', joystick.get_name())
    print('ボタン数 :', joystick.get_numbuttons())
except pygame.error:
    print('ジョイスティックが接続されていません')

# pygameの初期化
pygame.init()

# 画面の生成
screen = pygame.display.set_mode((300, 260))

def button(button_num, on_off):
    #print(button_num, 'pushed' if on_off == 0 else 'released')
    if button_num % 2 == 0:
        x = button_num // 2 * 70 + 20
    else:
        x = button_num // 2 * 70 + 55
    y = button_num % 2 * -100 + 140
    # ボタン画像の表示・非表示
    if on_off == 0:
        screen.blit(img, (x, y))
    else:
        screen.blit(img2, (x, y))
    pygame.display.update()

# ループ
active = True
while active:
    # イベントの取得
    for e in pygame.event.get():
         # 終了ボタン
        if e.type == QUIT:
            active = False

        # ジョイスティックのボタンの入力
        if e.type == pygame.locals.JOYAXISMOTION:
            if joystick.get_axis(0) == -1 and joystick.get_axis(1) == -0.007843017578125:
                button(6, 0)
            elif joystick.get_axis(0) == -0.007843017578125 and joystick.get_axis(1) == -0.007843017578125:
                button(6, 1)
        elif e.type == pygame.locals.JOYBUTTONDOWN:
            if int(e.button) <= 7:
                button(button_key[int(e.button) - 1], 0)
        elif e.type == pygame.locals.JOYBUTTONUP:
            if int(e.button) <= 7:
                button(button_key[int(e.button) - 1], 1)

