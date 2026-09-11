import FISH
import time
import random


display = FISH.Display()
button = FISH.Button()


mine = {
    "x": 50,
    "y": 200,
    "old_x": 50,
    "old_y": 200,
    "score": 0,
    "gameflug": False,
    "speed": 5
}


enemylist = []


# ========================================
# ゲームリセット
# ========================================

def reset_game():

    global mine
    global enemylist

    mine = {
        "x": 50,
        "y": 200,
        "old_x": 50,
        "old_y": 200,
        "score": 0,
        "gameflug": False,
        "speed": 5
    }

    enemylist = []

    display.clear()


# ========================================
# 当たり判定
# ========================================

def hit(mine, enemylist):

    for e in enemylist:

        if (
            mine["x"] < e["x"] + 10 and
            mine["x"] + 10 > e["x"] and
            mine["y"] < e["y"] + 10 and
            mine["y"] + 10 > e["y"]
        ):

            mine["gameflug"] = True
            display.clear()

    return mine


# ========================================
# 敵生成
# ========================================

def enemys(enemylist):

    chance = random.randint(0, 3)

    if chance == 1:

        newx = random.randint(0, 230)
        newspeed = random.randint(1, 10)

        enemylist.append({
            "x": newx,
            "y": 0,
            "old_x": newx,
            "old_y": 0,
            "speed": newspeed
        })

    return enemylist


# ========================================
# 前の敵を消す
# ========================================


# ========================================
# 敵を移動
# ========================================

def fall(enemylist, mine):

    survived = []

    for e in enemylist:

        # 現在位置を保存
        e["old_x"] = e["x"]
        e["old_y"] = e["y"]

        # 移動
        e["y"] += e["speed"]

        if e["y"] <= 230:

            survived.append(e)

        else:

            mine["score"] += 1

    return survived, mine


# ========================================
# 敵を描画
# ========================================

def draw_enemies(enemylist):

    for e in enemylist:

        display.rect(
            e["x"],
            e["y"],
            10,
            10,
            FISH.BLUE
        )


# ========================================
# プレイヤーを消す
# ========================================


# ========================================
# プレイヤー描画
# ========================================

def draw_player():

    display.rect(
        mine["x"],
        mine["y"],
        10,
        10,
        FISH.WHITE
    )


# ========================================
# スコア描画
# ========================================

def draw_score():

    # スコア部分だけ消す
    display.rect(
        0,
        0,
        100,
        10,
        FISH.BLACK
    )

    display.text(
        "SCORE:{}".format(mine["score"]),
        0,
        0,
        FISH.WHITE,
        1
    )


# ========================================
# ゲームオーバー
# ========================================

def game_over():

    display.text(
        "GAME OVER",
        20,
        20,
        FISH.WHITE,
        2
    )

    display.text(
        "SCORE:{}".format(mine["score"]),
        20,
        45,
        FISH.WHITE,
        1
    )

    display.text(
        "R: retry",
        20,
        70,
        FISH.WHITE,
        1
    )


# ========================================
# メイン
# ========================================

def main():

    global enemylist
    global mine


    # ====================================
    # GAME OVER
    # ====================================

    if mine["gameflug"]:

        game_over()

        if button.r_push():

            reset_game()

            time.sleep(0.2)

        return


    # ====================================
    # 前フレームを部分的に消す
    # ====================================

   
    # ====================================
    # 敵生成
    # ====================================

    enemylist = enemys(enemylist)


    # ====================================
    # 敵移動
    # ====================================

    enemylist, mine = fall(
        enemylist,
        mine
    )


    # ====================================
    # ボタン操作
    # ====================================

    # プレイヤーの現在位置を保存
    mine["old_x"] = mine["x"]
    mine["old_y"] = mine["y"]


    if button.r_push():

        mine["x"] = max(
            0,
            mine["x"] - mine["speed"]
        )


    if button.l_push():

        mine["x"] = min(
            230,
            mine["x"] + mine["speed"]
        )


    # ====================================
    # 当たり判定
    # ====================================

    mine = hit(
        mine,
        enemylist
    )


    # ====================================
    # 描画
    # ====================================

    if not mine["gameflug"]:

        #draw_score()

        draw_enemies(enemylist)

        draw_player()