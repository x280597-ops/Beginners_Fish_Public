import FISH
import time
import random
import math


# =========================================================
# 初期化
# =========================================================

display = FISH.Display()
button = FISH.Button()


# =========================================================
# 魚データ
# =========================================================

FISHES = [
    {"name": "アジ",   "speed": 0.45, "amplitude": 7,  "change": 0.020, "catch_time": 3.0},
    {"name": "サバ",   "speed": 0.75, "amplitude": 10, "change": 0.035, "catch_time": 4.0},
    {"name": "タイ",   "speed": 0.60, "amplitude": 15, "change": 0.045, "catch_time": 5.0},
    {"name": "ブリ",   "speed": 1.00, "amplitude": 18, "change": 0.060, "catch_time": 6.0},
    {"name": "マグロ", "speed": 1.35, "amplitude": 25, "change": 0.080, "catch_time": 7.0},
]

TIME_LIMIT = 30.0  # 1匹あたりの制限時間(秒)


# =========================================================
# ゲージ設定
# =========================================================

GAUGE_X = 218
GAUGE_TOP = 65
GAUGE_BOTTOM = 150
SAFE_TOP = 100
SAFE_BOTTOM = 120


# =========================================================
# ゲーム状態(呼び出しをまたいで保持する)
# =========================================================

gauge_y = 120.0
gauge_velocity = 0.0
fish_force = 0.0

current_fish = None
safe_time = 0.0

game_start = 0
last_time = 0

game_state = "FISHING"
reel_animation = 0

catches = 0       # 今のセッションで釣った数(連続記録)
high_score = 0     # 自己ベスト


# =========================================================
# 背景
# =========================================================

def draw_background():
    # 空
    display.fill(FISH.WHITE)
    # 海
    display.rect(0, 100, 240, 70, FISH.BLUE)
    # 水平線
    display.h_line(0, 103, 240, FISH.BLACK)
    # 海の波
    display.h_line(10, 118, 30, FISH.WHITE)
    display.h_line(65, 128, 35, FISH.WHITE)
    display.h_line(125, 115, 30, FISH.WHITE)
    display.h_line(170, 132, 40, FISH.WHITE)
    display.h_line(205, 118, 25, FISH.WHITE)
    # 奥の丘
    display.line(0, 150, 30, 120, FISH.GREEN)
    display.line(30, 120, 65, 140, FISH.GREEN)
    display.line(65, 140, 110, 112, FISH.GREEN)
    display.line(110, 112, 155, 140, FISH.GREEN)
    display.line(155, 140, 205, 115, FISH.GREEN)
    display.line(205, 115, 240, 135, FISH.GREEN)
    display.rect(0, 145, 240, 20, FISH.GREEN)
    # 手前の地面
    display.rect(0, 165, 240, 75, FISH.GREEN)
    # 釣り竿
    display.line(35, 210, 185, 55, FISH.BLACK)
    display.line(38, 210, 188, 58, FISH.WHITE)
    # 竿先
    display.line(185, 55, 215, 105, FISH.WHITE)
    # 糸
    display.line(215, 105, 215, 165, FISH.BLACK)
    # リール
    display.rect(55, 190, 38, 28, FISH.BLACK)
    display.rect(60, 195, 28, 18, FISH.WHITE)
    display.rect(66, 198, 16, 12, FISH.BLACK)
    # リールハンドル
    display.line(84, 200, 100, 188, FISH.BLACK)
    display.line(100, 188, 107, 194, FISH.BLACK)


# =========================================================
# ゲージ背景
# =========================================================

def draw_gauge_background():
    display.rect(205, 55, 30, 105, FISH.GREEN)
    # 枠
    display.rect(GAUGE_X - 4, GAUGE_TOP, 12, GAUGE_BOTTOM - GAUGE_TOP, FISH.BLACK)
    # 安全帯
    display.rect(GAUGE_X - 2, SAFE_TOP, 8, SAFE_BOTTOM - SAFE_TOP, FISH.WHITE)
    # 中央線
    display.h_line(GAUGE_X - 3, (SAFE_TOP + SAFE_BOTTOM) // 2, 10, FISH.BLACK)


# =========================================================
# ゲージ
# =========================================================

def draw_gauge():
    # ゲージ内部を消す
    display.rect(GAUGE_X - 2, GAUGE_TOP + 2, 8, GAUGE_BOTTOM - GAUGE_TOP - 4, FISH.GREEN)
    # 安全帯
    display.rect(GAUGE_X - 2, SAFE_TOP, 8, SAFE_BOTTOM - SAFE_TOP, FISH.WHITE)
    # 現在位置
    y = int(gauge_y)
    display.rect(GAUGE_X - 4, y - 3, 12, 6, FISH.RED)


# =========================================================
# リール
# =========================================================

def draw_reel():
    # リール周辺を消す
    display.rect(83, 180, 30, 35, FISH.GREEN)
    # 本体
    display.rect(85, 190, 15, 15, FISH.BLACK)
    # 回転
    angle = reel_animation * 0.8
    x = int(92 + math.cos(angle) * 10)
    y = int(197 + math.sin(angle) * 10)
    display.line(92, 197, x, y, FISH.WHITE)


# =========================================================
# 魚選択(釣った数が増えるほど強い魚が出やすくなる)
# =========================================================

def pick_weighted_fish():
    weights = []
    for i in range(len(FISHES)):
        w = 12 - i * 2 + min(catches, 8)
        if w < 1:
            w = 1
        weights.append(w)

    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0.0
    for fish, w in zip(FISHES, weights):
        upto += w
        if r <= upto:
            return fish
    return FISHES[-1]


def new_fish():
    global current_fish
    current_fish = pick_weighted_fish()


# =========================================================
# 1匹分の準備
# =========================================================

def reset_round():
    global gauge_y, gauge_velocity, fish_force
    global safe_time, game_state, game_start, last_time, reel_animation

    gauge_y = 120.0
    gauge_velocity = 0.0
    fish_force = 0.0
    safe_time = 0.0
    reel_animation = 0

    new_fish()

    game_state = "FISHING"
    game_start = time.ticks_ms()
    last_time = game_start


# =========================================================
# ゲージ更新
# =========================================================

def update_gauge(dt):
    global gauge_y, gauge_velocity, fish_force, reel_animation

    # 魚の動き
    if random.random() < current_fish["change"]:
        fish_force = random.uniform(-current_fish["amplitude"], current_fish["amplitude"])

    fish_force *= 0.96

    # ボタン
    push_up = button.r_push()
    push_down = button.l_push()

    player_force = 0
    if push_up:
        player_force = -current_fish["speed"] * 18
        reel_animation += 1
    if push_down:
        player_force = current_fish["speed"] * 18
        reel_animation += 1

    # ゲージ速度
    gauge_velocity += fish_force * dt
    gauge_velocity += player_force * dt
    gauge_velocity *= 0.90

    gauge_y += gauge_velocity

    # 上限
    if gauge_y < GAUGE_TOP + 5:
        gauge_y = GAUGE_TOP + 5
        gauge_velocity *= -0.5

    # 下限
    if gauge_y > GAUGE_BOTTOM - 5:
        gauge_y = GAUGE_BOTTOM - 5
        gauge_velocity *= -0.5


# =========================================================
# 安全帯
# =========================================================

def check_safe(dt):
    global safe_time
    if SAFE_TOP <= gauge_y <= SAFE_BOTTOM:
        safe_time += dt
    else:
        safe_time -= dt * 0.5
        if safe_time < 0:
            safe_time = 0


# =========================================================
# UI
# =========================================================

def draw_ui():
    # 左側:魚名・進行度
    display.rect(0, 0, 170, 48, FISH.WHITE)
    display.text(current_fish["name"], 8, 5, FISH.BLACK, 1)
    display.text("KEEP!", 8, 20, FISH.BLACK, 1)

    progress = safe_time / current_fish["catch_time"]
    if progress > 1:
        progress = 1

    display.rect(8, 33, 120, 10, FISH.BLACK)
    width = int(116 * progress)
    if width > 0:
        display.rect(10, 35, width, 6, FISH.WHITE)

    display.text("L/R", 145, 5, FISH.BLACK, 1)
    display.text("REEL", 140, 20, FISH.BLACK, 1)

    # 右側:釣果・自己ベスト・残り時間
    display.rect(174, 0, 66, 48, FISH.WHITE)
    display.text("F:" + str(catches), 178, 3, FISH.BLACK, 1)
    display.text("B:" + str(high_score), 178, 16, FISH.BLACK, 1)

    if game_state == "FISHING":
        elapsed = time.ticks_diff(time.ticks_ms(), game_start) / 1000.0
        remaining = TIME_LIMIT - elapsed
        if remaining < 0:
            remaining = 0
        display.text(str(int(remaining)) + "s", 178, 30, FISH.BLACK, 1)


# =========================================================
# 魚の絵
# =========================================================

def draw_fish_picture(name, cx, cy):
    if name == "アジ":
        display.rect(cx - 18, cy - 6, 28, 12, FISH.WHITE)
        display.line(cx + 10, cy, cx + 18, cy - 7, FISH.WHITE)
        display.line(cx + 10, cy, cx + 18, cy + 7, FISH.WHITE)
        display.line(cx - 5, cy - 6, cx, cy - 11, FISH.WHITE)
        display.rect(cx - 12, cy - 3, 3, 3, FISH.BLACK)

    elif name == "サバ":
        display.rect(cx - 20, cy - 7, 30, 14, FISH.WHITE)
        display.line(cx + 10, cy, cx + 20, cy - 9, FISH.WHITE)
        display.line(cx + 10, cy, cx + 20, cy + 9, FISH.WHITE)
        display.line(cx - 8, cy - 6, cx - 3, cy + 6, FISH.BLACK)
        display.line(cx, cy - 6, cx + 5, cy + 6, FISH.BLACK)
        display.rect(cx - 14, cy - 3, 3, 3, FISH.BLACK)

    elif name == "タイ":
        display.rect(cx - 18, cy - 12, 28, 24, FISH.WHITE)
        display.line(cx + 10, cy, cx + 21, cy - 10, FISH.WHITE)
        display.line(cx + 10, cy, cx + 21, cy + 10, FISH.WHITE)
        display.line(cx - 5, cy - 12, cx, cy - 18, FISH.WHITE)
        display.line(cx, cy - 18, cx + 5, cy - 12, FISH.WHITE)
        display.rect(cx - 13, cy - 5, 4, 4, FISH.BLACK)

    elif name == "ブリ":
        display.rect(cx - 22, cy - 9, 35, 18, FISH.WHITE)
        display.line(cx + 13, cy, cx + 24, cy - 10, FISH.WHITE)
        display.line(cx + 13, cy, cx + 24, cy + 10, FISH.WHITE)
        display.line(cx - 15, cy - 9, cx - 8, cy - 15, FISH.WHITE)
        display.line(cx - 8, cy - 15, cx + 2, cy - 9, FISH.WHITE)
        display.rect(cx - 17, cy - 4, 4, 4, FISH.BLACK)

    elif name == "マグロ":
        display.rect(cx - 25, cy - 10, 40, 20, FISH.WHITE)
        display.line(cx + 15, cy, cx + 28, cy - 12, FISH.WHITE)
        display.line(cx + 15, cy, cx + 28, cy + 12, FISH.WHITE)
        display.line(cx - 5, cy - 10, cx + 2, cy - 18, FISH.WHITE)
        display.line(cx + 2, cy - 18, cx + 7, cy - 10, FISH.WHITE)
        display.rect(cx - 20, cy - 5, 4, 4, FISH.BLACK)


# =========================================================
# 結果画面
# 戻り値: True = もう一度遊ぶ / False = ゲーム終了(リセット扱い)
# =========================================================

def result_screen(caught):
    global catches, high_score

    if caught:
        catches += 1
        if catches > high_score:
            high_score = catches
    else:
        catches = 0

    draw_background()

    display.rect(25, 35, 175, 150, FISH.BLACK)
    display.rect(29, 39, 167, 142, FISH.WHITE)

    if caught:
        display.text("GET!", 88, 48, FISH.BLACK, 2)
        display.text(current_fish["name"], 92, 75, FISH.BLACK, 1)
        draw_fish_picture(current_fish["name"], 112, 115)
        display.text("SUCCESS!", 82, 145, FISH.BLACK, 1)
    else:
        display.text("ESCAPE!", 72, 60, FISH.BLACK, 2)
        display.text(current_fish["name"], 92, 95, FISH.BLACK, 1)
        display.text("FISH GOT AWAY", 62, 125, FISH.BLACK, 1)

    display.text("SCORE " + str(catches) + " / BEST " + str(high_score), 45, 150, FISH.BLACK, 1)
    display.text("PRESS L/R", 78, 165, FISH.BLACK, 1)
    display.text("HOLD RESET TO QUIT", 45, 180, FISH.BLACK, 1)

    # リトライ待ち(ここでも常にリセットボタンを見て抜けられるようにする)
    while True:
        if button.reset_btn():
            return False
        if button.r_push() or button.l_push():
            time.sleep(0.3)
            return True
        time.sleep(0.05)


# =========================================================
# 1ラウンド実行
# 戻り値: True = 続行する / False = リセットで終了
# =========================================================

def play_one_round():
    global game_state, last_time

    reset_round()
    draw_background()
    draw_gauge_background()
    draw_ui()
    last_time = time.ticks_ms()

    while game_state == "FISHING":
        if button.reset_btn():
            return False

        now = time.ticks_ms()
        dt = time.ticks_diff(now, last_time) / 1000.0
        last_time = now
        if dt > 0.1:
            dt = 0.1

        update_gauge(dt)
        check_safe(dt)

        draw_gauge()
        draw_ui()
        draw_reel()

        if safe_time >= current_fish["catch_time"]:
            game_state = "CAUGHT"

        elapsed = time.ticks_diff(now, game_start) / 1000.0
        if elapsed > TIME_LIMIT:
            game_state = "ESCAPED"

        time.sleep(0.03)

    caught = (game_state == "CAUGHT")
    return result_screen(caught)


# =========================================================
# エントリーポイント
# main.py から gamelist[game_num]() として呼ばれる想定
# =========================================================

def main():
    global catches
    catches = 0  # 新しいセッションとして連続記録をリセット
def update():
    keep_going = play_one_round()
    if not keep_going:
        return


if __name__ == "__main__":
    main()