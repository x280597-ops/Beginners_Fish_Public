import FISH
import time
import random
display = FISH.Display()
button = FISH.Button()
sensor=FISH.Sensor()
class monster():
    def __init__(self,name,cond_temp,cond_hum):
        self.name=name
        self.temp=cond_temp
        self.hum=cond_hum

chara_01=monster("Steam Beast",10,10)
chara_02=monster("Misty Fang",9,10)
chara_03=monster("Swamp Maw",8,10)
chara_04=monster("Bog Crawler",7,10)
chara_05=monster("Marsh Stalker",6,10)
chara_06=monster("Mire Beast",5,10)
chara_07=monster("Moss Golem",4,10)
chara_08=monster("Damp Wisp",3,10)
chara_09=monster("Frost Moss",2,10)
chara_010=monster("Cold Mire",1,10)
chara_011=monster("Ice Bog",0,10)

chara_11=monster("Steam Serpent",10,9)
chara_12=monster("Mist Wolf",9,9)
chara_13=monster("Swamp Fang",8,9)
chara_14=monster("Bog Beast",7,9)
chara_15=monster("Marsh Wolf",6,9)
chara_16=monster("Mire Hound",5,9)
chara_17=monster("Moss Beast",4,9)
chara_18=monster("Wet Wraith",3,9)
chara_19=monster("Frost Wraith",2,9)
chara_110=monster("Cold Wraith",1,9)
chara_111=monster("Ice Wraith",0,9)

chara_21=monster("Heat Drake",10,8)
chara_22=monster("Mist Drake",9,8)
chara_23=monster("Swamp Drake",8,8)
chara_24=monster("Bog Drake",7,8)
chara_25=monster("Marsh Drake",6,8)
chara_26=monster("Mire Drake",5,8)
chara_27=monster("Moss Drake",4,8)
chara_28=monster("Damp Drake",3,8)
chara_29=monster("Frost Drake",2,8)
chara_210=monster("Cold Drake",1,8)
chara_211=monster("Ice Drake",0,8)

chara_31=monster("Heat Serpent",10,7)
chara_32=monster("Mist Serpent",9,7)
chara_33=monster("Swamp Serpent",8,7)
chara_34=monster("Bog Serpent",7,7)
chara_35=monster("Marsh Serpent",6,7)
chara_36=monster("Mire Serpent",5,7)
chara_37=monster("Moss Serpent",4,7)
chara_38=monster("Damp Serpent",3,7)
chara_39=monster("Frost Serpent",2,7)
chara_310=monster("Cold Serpent",1,7)
chara_311=monster("Ice Serpent",0,7)

chara_41=monster("Sunscale",10,6)
chara_42=monster("Mistscale",9,6)
chara_43=monster("Swampscale",8,6)
chara_44=monster("Bogscale",7,6)
chara_45=monster("Marshscale",6,6)
chara_46=monster("Mirescale",5,6)
chara_47=monster("Mossscale",4,6)
chara_48=monster("Dampscale",3,6)
chara_49=monster("Frostscale",2,6)
chara_410=monster("Coldscale",1,6)
chara_411=monster("Icescale",0,6)

chara_51=monster("Ember Hound",10,5)
chara_52=monster("Mist Hound",9,5)
chara_53=monster("Swamp Hound",8,5)
chara_54=monster("Bog Hound",7,5)
chara_55=monster("Marsh Hound",6,5)
chara_56=monster("Mire Hound",5,5)
chara_57=monster("Moss Hound",4,5)
chara_58=monster("Damp Hound",3,5)
chara_59=monster("Frost Hound",2,5)
chara_510=monster("Cold Hound",1,5)
chara_511=monster("Ice Hound",0,5)

chara_61=monster("Fire Beetle",10,4)
chara_62=monster("Mist Beetle",9,4)
chara_63=monster("Swamp Beetle",8,4)
chara_64=monster("Bog Beetle",7,4)
chara_65=monster("Marsh Beetle",6,4)
chara_66=monster("Mire Beetle",5,4)
chara_67=monster("Moss Beetle",4,4)
chara_68=monster("Damp Beetle",3,4)
chara_69=monster("Frost Beetle",2,4)
chara_610=monster("Cold Beetle",1,4)
chara_611=monster("Ice Beetle",0,4)

chara_71=monster("Ember Crow",10,3)
chara_72=monster("Mist Crow",9,3)
chara_73=monster("Swamp Crow",8,3)
chara_74=monster("Bog Crow",7,3)
chara_75=monster("Marsh Crow",6,3)
chara_76=monster("Mire Crow",5,3)
chara_77=monster("Moss Crow",4,3)
chara_78=monster("Damp Crow",3,3)
chara_79=monster("Frost Crow",2,3)
chara_710=monster("Cold Crow",1,3)
chara_711=monster("Ice Crow",0,3)

chara_81=monster("Fire Moth",10,2)
chara_82=monster("Mist Moth",9,2)
chara_83=monster("Swamp Moth",8,2)
chara_84=monster("Bog Moth",7,2)
chara_85=monster("Marsh Moth",6,2)
chara_86=monster("Mire Moth",5,2)
chara_87=monster("Moss Moth",4,2)
chara_88=monster("Damp Moth",3,2)
chara_89=monster("Frost Moth",2,2)
chara_810=monster("Cold Moth",1,2)
chara_811=monster("Ice Moth",0,2)

chara_91=monster("Sun Scorpion",10,1)
chara_92=monster("Mist Scorpion",9,1)
chara_93=monster("Swamp Scorpion",8,1)
chara_94=monster("Bog Scorpion",7,1)
chara_95=monster("Marsh Scorpion",6,1)
chara_96=monster("Mire Scorpion",5,1)
chara_97=monster("Moss Scorpion",4,1)
chara_98=monster("Damp Scorpion",3,1)
chara_99=monster("Frost Scorpion",2,1)
chara_910=monster("Cold Scorpion",1,1)
chara_911=monster("Ice Scorpion",0,1)

chara_a1=monster("Inferno",10,0)
chara_a2=monster("Sun Fang",9,0)
chara_a3=monster("Dune Beast",8,0)
chara_a4=monster("Sand Crawler",7,0)
chara_a5=monster("Dust Stalker",6,0)
chara_a6=monster("Ash Hound",5,0)
chara_a7=monster("Dry Golem",4,0)
chara_a8=monster("Dust Wisp",3,0)
chara_a9=monster("Frost Dust",2,0)
chara_a10=monster("Cold Shade",1,0)
chara_a11=monster("Winter Shade",0,0)
chara_list=[]
all_chara_list = [
    chara_01, chara_02, chara_03, chara_04, chara_05, chara_06, chara_07, chara_08, chara_09, chara_010, chara_011,
    chara_11, chara_12, chara_13, chara_14, chara_15, chara_16, chara_17, chara_18, chara_19, chara_110, chara_111,
    chara_21, chara_22, chara_23, chara_24, chara_25, chara_26, chara_27, chara_28, chara_29, chara_210, chara_211,
    chara_31, chara_32, chara_33, chara_34, chara_35, chara_36, chara_37, chara_38, chara_39, chara_310, chara_311,
    chara_41, chara_42, chara_43, chara_44, chara_45, chara_46, chara_47, chara_48, chara_49, chara_410, chara_411,
    chara_51, chara_52, chara_53, chara_54, chara_55, chara_56, chara_57, chara_58, chara_59, chara_510, chara_511,
    chara_61, chara_62, chara_63, chara_64, chara_65, chara_66, chara_67, chara_68, chara_69, chara_610, chara_611,
    chara_71, chara_72, chara_73, chara_74, chara_75, chara_76, chara_77, chara_78, chara_79, chara_710, chara_711,
    chara_81, chara_82, chara_83, chara_84, chara_85, chara_86, chara_87, chara_88, chara_89, chara_810, chara_811,
    chara_91, chara_92, chara_93, chara_94, chara_95, chara_96, chara_97, chara_98, chara_99, chara_910, chara_911,
    chara_a1, chara_a2, chara_a3, chara_a4, chara_a5, chara_a6, chara_a7, chara_a8, chara_a9, chara_a10, chara_a11
]
chara_num=0
def draw_title():
    display.text("Monster_Get", 30, 60, FISH.WHITE, 2)
    display.rect(48, 140, 56, 24, FISH.GREEN)
    display.rect(104, 146, 10, 12, FISH.GREEN)
    display.rect(114, 140, 20, 24, FISH.GREEN)
    display.rect(54, 143, 6, 6, FISH.BLACK)
def env_check():
    temp=sensor.temp()
    hum=sensor.hum()
    temp_score=int(temp/4)
    hum_score=int(hum/10)
    return temp_score,hum_score
def get_monster():
    global chara_num
    get_flug=False
    get_chance=random.randint(0,10)
    print(1)
    if get_chance==0:
        temp_score,hum_score=env_check()
        for chara in all_chara_list:
            if temp_score==chara.temp and hum_score==chara.hum:
                chara_list.append(chara)
                get_chara=chara
                chara_num+=1
                get_flug=True
                break
    if (get_flug):
        display.fill(FISH.BLACK)
        while True:
            
            display.text("Get:"+get_chara.name, 50, 190, FISH.WHITE, 2)
            if button.r_push():
                display.fill(FISH.BLACK)
                break
def view_zukan():
    num=0
    display.text("zukan:", 10, 10, FISH.WHITE, 2)
    for z_chara in chara_list:
        z_x=20+(num%6)*30
        z_y=20+(num//6)*30
        num+=1
        display.text(z_chara.name, z_x, z_y, FISH.WHITE, 2)
    while True:
        if button.r_push():
                display.fill(FISH.BLACK)
                break
def update():
    if button.l_push():
        display.fill(FISH.BLACK)
        view_zukan()
    else: 
        get_monster()
def main():
    draw_title()
    