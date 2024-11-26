version="1.2.5"
import BATTLE as btl
import SHOP as shp
import STORY as sty 
import SAVERR as svr
import INFO as inf
import HELLO as begin
import LOADING as ld 



ld.load(2)
print("        Real\n           Calculator\n                    Game\n")
print("                  Version "+version)
print("\n 1.Story Mode")
print(" 2.Endless\n")
mode=input(" What will you do?")
while mode!="1" and mode!="2":
  print("Input invalid")
  print("Welcome to Real Calculator Game")
  print("Version "+version)
  print("\n1.Story Mode")
  print("2.Endless\n")
  mode=input("What will you do?")
print("Save Files\n")
svr.display()
filer=svr.getFile()
print(filer)
if filer<5:
  load=svr.getSave(filer)
  
  name=svr.getName(filer)
  maxHealth=load[0]
  level=load[2]
  moves=load[1]
  gold=load[3]
  enemies=load[4]
else:
  filer=(filer/10)
  begin.start()
  name=begin.GetName()
  maxHealth=100
  level=1
  moves=1
  gold=10
  enemies=0

exit="y"

if mode=="1":
  ld.load(1)
  svr.saveGame(filer,maxHealth,moves,level,gold,enemies,name)
  
  sty.story(filer,maxHealth,moves,level,gold,enemies,name)
  


while exit!="n" and mode=="2":
  svr.saveGame(filer,maxHealth,moves,level,gold,enemies,name)
  print("Hello "+ name)
  print("You have ",int(gold)," gold" )
  print()
  print("Enter:\n8 to go to the shop \n6 to battle \n4 for info \n2 to quit\n" )
  i=input("What will you do?")
  while i != "8" and i!="6"and i!="4"and i!="2" :
    print("That wasnt an option.\nTry again")
    print("Type 8 to go to the shop, 6 to battle, 4 for info,or 2 to quit" )
    i=input("What will you do?")
    
  if i=="8":
    ld.load(1)
    #print("Heading to shop...")
    stat=shp.shop(gold,moves,maxHealth)
    gold=stat[0]
    moves=stat[1]
    maxHealth=stat[2]
    ld.load(1)
    
  elif i=="6" :
    ld.load(1)
    #print("Heading to battle...")
    stats=btl.battle(name,gold,maxHealth,moves,enemies,level)
    ld.load(1)
    gold=stats[0]
    moves=stats[2]
    maxHealth=stats[1]
    level=stats[3]
    if gold==-978:
      exit="n"
      inf.gameOver(name,maxHealth,moves,level)
      svr.saveGame(filer,0,0,0,0,0,"empty")
    enemies=enemies+1
  elif i=="4" :
    ld.load(1)
    #print("Heading to info...")
    inf.displayInfo(name,maxHealth,moves,enemies,level)
    ld.load(1)
  elif i=="2" :
    print("I hope you had fun!")
    exit="n"
    inf.gameOver(name,maxHealth,moves,level)

