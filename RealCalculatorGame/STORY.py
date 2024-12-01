import SHOP as shp
import BATTLE as btl
import SAVERR as svr
import LOADING as ld 
from time import *
from random import *
import INFO as inf



def save(stats):
  svr.saveGame(stats[0],stats[1],stats[2],stats[3],stats[4],stats[5],stats[6])

def battle(enemy,stats):
  statb=btl.battle(stats[6],stats[4],stats[1],stats[2],enemy,stats[3])
  stats[4]=statb[0]
  stats[1]=statb[1]
  stats[2]=statb[2]
  stats[3]=statb[3]
  return stats

def pri(msg):
  for i in msg:
    print(i,end="")
    sleep(0.05)
def choice(choice1,choice2):
  enter=""
  while enter!="1" and enter!="2":
    print("Options")
    print("1."+choice1)
    print("2."+choice2)
    enter=input("Well?")
  return int(enter)

def read(list):
  for i in list:
    pri(i)
    sleep(2)
    #j=input("")

def checkDead(gold):
  if(gold == -978):
    inf.gameOver(name,maxHealth,moves,level)
    svr.saveGame(filer,0,0,0,0,0,"empty")
  return 1;
start=[
"You are a detective investigating supernatural activities in Los Angeles. ", 
"Your current target is a mansion in the middle of a dense forest. Because of its location, the higher ups think it is too abnormal.", 
"The plan is as follows. ",
"You will be airdropped into the forest nearby. ",
"After landing using the parachute provided to you, you are to sneak into the mansion.",
"Your outfit will be hidden inside the farthest toilet tank in the left bathroom of the mansion.",
"After retrieving the outfit, wear it and enter the basement.",
"If possible, find any incriminating evidence. Worse comes to worse, eliminate any threats.",
"You have been provided with a map with the mansion’s layout in case you are lost.",
"Before the mission starts, you are given a chance to buy some weapons and equipment before you sneak into the mansion. "
"Now is the time to buy equipment. "
]
two=[
"November 29th, 2024. Midnight, Unknown Forest.",
"You airdrop down and land safely. ",
"As you walk toward the Mansion. You realize that there have been some renovations.",
"For one, there is a very tall fence.",
"Many strange small humans are also walking around the perimeter, guarding the mansion."
]
twoc=["You managed to sneak in successfully. You then proceed to slowly creep up the stairs", "Having taken down the goblins,you quickly run up the stairs"]
three=["However ur footing is unstable, and you slip and crash.",
"Suddenly a bunch of goblins on dinosaurs appear."]
four=[
"After beating the dinosaurs, you hear the footsteps of more coming",
"Your eyes scramble around and see a sewer manhole cover.",
"You jump in, and climb down.",
"You scramble, and eventually climb out of one to arrive near the mansion walls.",
"There is a half open window with light shining out of it. A pair of voices are inside.",
"You peak into the window, and see the bathroom.",
"You can’t make out what they’re saying, but the stall where your equipment is stored is open."
]
fourc=["You wait, but the people don’t leave. You're on a time constraint. You must fight.", "You take a peek, but the people inside see you. "
]
five=[
"Inside the bag is a red and black robe, with magic inscriptions written on either side. Is this an occultist uniform?",
"After wearing the robes, you head out of the bathroom",
"You’ve memorized the floor plan already. You know exactly where to go. You head down a corridor and see stairs descending into the basement.",
"You head down the stairs, and walk down the corridor.", 
"Although it is pitch black at first, you eventually see the neon glow of cylinders.",
"They’re as tall as two humans stacked on top of each other, and house a enlarged embryo of some sort.",
"At the end of the corridor is a man working at a computer. His eyes are focused on the computer.",
"Your not supposed to be here.” He murmurs. Suddenly, two goblins spring down from the roof. A surprise attack!"
]
six=[
"You beat the goblins. “Stupid goblins.” He rises from the chair. “Always failing at the most basic of tasks.”",
"Your heart starts beating rapidly.",
"Time to fight."
]
end=[
"Well you’ve done it. Congratulations.",
"The commotion you made while fighting the mad scientist had attracted all the occultists around,",
"but with they’re leader completely and utterly stomped, there was not much they could’ve done.",
"As you turned to walk back up the stairs, the crowd that had formed parted in two.",
"Only your footsteps were heard as you headed out of the mansion."
"Thank you for playing!"
]
def story(file,maxHealt,move,leve,gol,enemie,nam):

  stats=[file, maxHealt, move, leve, gol, enemie, nam]

  read(start)
  stat=shp.shop(stats[4],stats[2],stats[1])
  stats[4]=stat[0]
  stats[2]=stat[1]
  stats[1]=stat[2]
  
  save(stat)
  read(two)
  opt=choice("Sneak into the mansion","Don't sneak in")
  if opt==2 or randint(0,10)>7:
    if opt != 2:
      pri("You tried to sneak in, but unfortunately got caught")
    stats=battle(14,stats)
    pri(twoc[2])
    if(checkDead(stats[4])):
      return 0
  else:
    pri(twoc[1])
  save(stats)

  read(three)
  stats=battle(14,stats)
  pri(twoc[2])
  if(checkDead(stats[4])):
    return 0
  
  read(four)
  opt=choice("Wait it out", "Take a")
  if opt==2:
    pri("You wait, but the people don’t leave. You're on a time constraint. You must fight.")
  else:
    pri("You take a peek, but the people inside see you.")
  stats=battle(14,stats)
  pri(twoc[2])
  if(checkDead(stats[4])):
    return 0
  save(stats)

  read(five)
  stats=battle(14,stats)
  pri(twoc[2])
  if(checkDead(stats[4])):
    return 0
  save(stats)

  read(six)
  stats=battle(14,stats)
  pri(twoc[2])
  if(checkDead(stats[4])):
    return 0
  save(stats)

  read(end)
  return 1
    