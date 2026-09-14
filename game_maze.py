import FISH
import time


# ========================================
# FISH
# ========================================

display = FISH.Display()
sensor = FISH.Sensor()


# ========================================
# 画面設定
# ========================================

WIDTH = 240
HEIGHT = 240


# ========================================
# 迷路設定
#
# 1 = 壁
# 0 = 通路
# 2 = ゴール
# ========================================

MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,1,0,1],
    [1,1,1,1,1,1,0,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,1,0,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1]
]


MAP_WIDTH = 13
MAP_HEIGHT = 13

CELL_SIZE = 18


# ========================================
# プレイヤー
# ========================================

player_x = 0
player_y = 0

PLAYER_SIZE = 8

PLAYER_SPEED = 1.5


# ========================================
# センサー
# ========================================

# gyro_list() の判定に使う角度
TILT_RATE = 4

tilt_x = 0
tilt_y = 0
tilt_z = 0


# ========================================
# ゲーム状態
# ========================================

game_state = "PLAYING"


# ========================================
# main
# ========================================

def main():

    global player_x
    global player_y

    global tilt_x
    global tilt_y
    global tilt_z

    global game_state

    # ------------------------------------
    # プレイヤー初期位置
    # ------------------------------------

    player_x = CELL_SIZE + CELL_SIZE // 2
    player_y = CELL_SIZE + CELL_SIZE // 2

    # ------------------------------------
    # 傾き初期化
    # ------------------------------------

    tilt_x = 0
    tilt_y = 0
    tilt_z = 0

    # ------------------------------------
    # ゲーム状態
    # ------------------------------------

    game_state = "PLAYING"

    # ------------------------------------
    # 背景
    # ------------------------------------

    draw_background()

    # ------------------------------------
    # 迷路
    # ------------------------------------

    draw_maze()

    # ------------------------------------
    # プレイヤー
    # ------------------------------------

    draw_player()


# ========================================
# 背景
# ========================================

def draw_background():

    display.fill(FISH.WHITE)


# ========================================
# 迷路描画
# ========================================

def draw_maze():

    for y in range(MAP_HEIGHT):

        for x in range(MAP_WIDTH):

            cell = MAZE[y][x]

            draw_x = x * CELL_SIZE
            draw_y = y * CELL_SIZE

            # --------------------------------
            # 壁
            # --------------------------------

            if cell == 1:

                display.rect(
                    draw_x,
                    draw_y,
                    CELL_SIZE,
                    CELL_SIZE,
                    FISH.BLACK
                )

            # --------------------------------
            # ゴール
            # --------------------------------

            elif cell == 2:

                display.rect(
                    draw_x,
                    draw_y,
                    CELL_SIZE,
                    CELL_SIZE,
                    FISH.GREEN
                )


# ========================================
# センサー取得
# ========================================

def read_tilt():

    global tilt_x
    global tilt_y
    global tilt_z

    # ------------------------------------
    # FISH の gyro_list を使用
    # ------------------------------------

    tilt = sensor.gyro_list(TILT_RATE)

    tilt_x = tilt[0]
    tilt_y = tilt[1]
    tilt_z = tilt[2]


# ========================================
# プレイヤー移動
# ========================================

def move_player():

    global player_x
    global player_y

    # ------------------------------------
    # X方向
    # ------------------------------------

    new_x = player_x + tilt_x * PLAYER_SPEED

    if not check_collision(new_x, player_y):

        player_x = new_x

    # ------------------------------------
    # Y方向
    # ------------------------------------

    new_y = player_y + tilt_y * PLAYER_SPEED

    if not check_collision(player_x, new_y):

        player_y = new_y


# ========================================
# 壁判定
# ========================================

def check_collision(x, y):

    half = PLAYER_SIZE // 2

    # プレイヤーの四隅を確認

    if is_wall(x - half, y - half):
        return True

    if is_wall(x + half, y - half):
        return True

    if is_wall(x - half, y + half):
        return True

    if is_wall(x + half, y + half):
        return True

    return False


# ========================================
# マップの壁判定
# ========================================

def is_wall(x, y):

    # 画面外
    if x < 0:
        return True

    if y < 0:
        return True

    if x >= WIDTH:
        return True

    if y >= HEIGHT:
        return True

    # マップ座標
    map_x = int(x // CELL_SIZE)
    map_y = int(y // CELL_SIZE)

    if map_x < 0 or map_x >= MAP_WIDTH:
        return True

    if map_y < 0 or map_y >= MAP_HEIGHT:
        return True

    return MAZE[map_y][map_x] == 1


# ========================================
# プレイヤー消去
# ========================================

def erase_player():

    # ------------------------------------
    # プレイヤーがいる周辺だけ
    # 迷路を描き直す
    # ------------------------------------

    center_x = int(player_x // CELL_SIZE)
    center_y = int(player_y // CELL_SIZE)

    for y in range(center_y - 1, center_y + 2):

        for x in range(center_x - 1, center_x + 2):

            if x < 0 or x >= MAP_WIDTH:
                continue

            if y < 0 or y >= MAP_HEIGHT:
                continue

            cell = MAZE[y][x]

            draw_x = x * CELL_SIZE
            draw_y = y * CELL_SIZE

            if cell == 1:

                display.rect(
                    draw_x,
                    draw_y,
                    CELL_SIZE,
                    CELL_SIZE,
                    FISH.BLACK
                )

            elif cell == 2:

                display.rect(
                    draw_x,
                    draw_y,
                    CELL_SIZE,
                    CELL_SIZE,
                    FISH.GREEN
                )

            else:

                display.rect(
                    draw_x,
                    draw_y,
                    CELL_SIZE,
                    CELL_SIZE,
                    FISH.WHITE
                )


# ========================================
# プレイヤー描画
# ========================================

def draw_player():

    half = PLAYER_SIZE // 2

    display.rect(
        int(player_x - half),
        int(player_y - half),
        PLAYER_SIZE,
        PLAYER_SIZE,
        FISH.RED
    )


# ========================================
# ゴール判定
# ========================================

def check_goal():

    map_x = int(player_x // CELL_SIZE)
    map_y = int(player_y // CELL_SIZE)

    if map_x < 0 or map_x >= MAP_WIDTH:
        return False

    if map_y < 0 or map_y >= MAP_HEIGHT:
        return False

    if MAZE[map_y][map_x] == 2:

        return True

    return False


# ========================================
# ゴール画面
# ========================================

def draw_goal():

    display.fill(FISH.WHITE)

    display.text(
        "GOAL!",
        80,
        75,
        FISH.BLACK,
        2
    )

    display.text(
        "CLEAR",
        82,
        120,
        FISH.GREEN,
        1
    )


# ========================================
# update
# ========================================

def update():

    global game_state

    # ====================================
    # プレイ中
    # ====================================

    if game_state == "PLAYING":

        # 前のプレイヤーを消す
        erase_player()

        # 傾きを取得
        read_tilt()

        # プレイヤー移動
        move_player()

        # プレイヤー描画
        draw_player()

        # ゴール判定
        if check_goal():

            game_state = "GOAL"

            draw_goal()

        return "PLAYING"


    # ====================================
    # ゴール後
    # ====================================

    if game_state == "GOAL":

        return "GOAL"


    return "END"