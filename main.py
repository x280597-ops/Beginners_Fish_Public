import read_files
import FISH
import time
main_display=FISH.Display()
main_button = FISH.Button()
main_display.fill(FISH.BLACK)
gamelist=read_files.load_file()
game_flug = False
game_num=0
game_num_max=len(gamelist)-1
def draw_set():
    main_display.set_display()
draw_set()
while True:
    if game_flug == True:
       draw_set()
       gamelist[game_num]()
       if main_button.reset_btn():
          main_display.fill(FISH.BLACK)
          game_flug=False
    else:
        if main_button.r_push():
            game_num+=1
            if (game_num>game_num_max):
                game_num=0
            draw_set()
            main_display.rect(0, 0, 20, 30, FISH.BLUE)
        elif main_button.l_push():
            game_num-=1
            if (game_num<0):
                game_num=game_num_max
            draw_set()
            main_display.rect(0,0,20,30,FISH.RED)
        if main_button.start_btn():
            game_flug = True
        main_display.text(str(game_num),50,50,FISH.WHITE,1)
    time.sleep(0.1)
    
    

    