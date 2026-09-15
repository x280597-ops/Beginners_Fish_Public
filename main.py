import read_files
import FISH
import time
main_display=FISH.Display()
main_button = FISH.Button()
gamelist,game_updatelist=read_files.load_file()
game_flug = False
game_num=0
game_num_max=len(gamelist)-1
def draw_B_F():
    main_display.rect(48, 140, 56, 24, FISH.BLUE)
    main_display.rect(104, 146, 10, 12, FISH.YELLOW)
    main_display.rect(114, 140, 20, 24, FISH.YELLOW)
    main_display.rect(54, 143, 6, 6, FISH.BLACK)
def draw_set():
    main_display.fill(FISH.BLACK)
draw_set()
while True:
    if game_flug == True:
       game_updatelist[game_num]()
       if main_button.reset_btn():
          main_display.fill(FISH.BLACK)
          game_flug=False
    else:
        if main_button.r_push():
            draw_set()
            game_num+=1
            if (game_num>game_num_max):
                game_num=0
            main_display.rect(0, 0, 20, 30, FISH.BLUE)
        elif main_button.l_push():
            draw_set()
            game_num-=1
            if (game_num<0):
                game_num=game_num_max
            main_display.rect(0,0,20,30,FISH.RED)
        main_display.text("BIGINNERS FISH", 30, 60, FISH.WHITE, 2)
        draw_B_F()
        main_display.text("Game_Number:", 50, 190, FISH.WHITE, 2)
        main_display.text(str(game_num),205,185,FISH.WHITE,3)
        if main_button.start_btn():
            draw_set()
            gamelist[game_num]()
            game_flug = True
    time.sleep(0.1)
    
    

    