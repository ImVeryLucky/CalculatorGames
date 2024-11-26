import SHOP as shp
import BATTLE as btl
import SAVERR as svr
import LOADING as ld 
from time import *
from random import *




def s(filer,maxHealth,moves,level,gold,enemies,name):
  svr.saveGame(filer,maxHealth,moves,level,gold,enemies,name)
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
    pri("\nContinue->")
    j=input("")

start=["It was a cold day in Los Angelos","You walked into a shop and...","'You shold buy some tools'"]
two=["As your leaving the shop,","A man walks toward you","He does a weird shuffle"]

def story(file,maxHealt,move,leve,gol,enemie,nam):
  gold=gol
  enemies=enemie
  moves=move
  level=leve
  filer=file
  
  maxHealth=maxHealt
  name=nam
  read(start)
  stat=shp.shop(gold,moves,maxHealth)
  gold=stat[0]
  moves=stat[1]
  maxHealth=stat[2]
  
  s(filer,maxHealth,moves,level,gold,enemies,name)
  read(two)
  s(filer,maxHealth,moves,level,gold,enemies,name)
  opt=choice("Step aside","Confront him")
  if opt==2 or randint(0,10)>7:
    stats=btl.battle(name,gold,maxHealth,moves,14,level)
    gold=stats[0]
    maxHealth=stats[1]
    moves=stats[2]
    level=stats[3]
    
  else:
    print("Evaded successfully")
    