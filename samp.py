import FISH
main_display=FISH.Display()
main_button = FISH.Button()
x=100
def main():
    global x
    main_display.rect(x, 0, 20, 30, FISH.BLUE)
    main_display.rect(30+x, 30, 20, 30, FISH.RED)
    if main_button.r_push():
        x+=1
    if main_button.l_push():
        x-=1