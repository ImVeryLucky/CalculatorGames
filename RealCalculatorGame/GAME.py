
version="1.2.5"
import gc
import SAVERR as svr
import HELLO as begin
import LOADING as ld 

gc.collect()
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
svr.display(1,4)
filer=svr.getFile(1,3)
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

if mode=="1":
  import STORY as sty 
  ld.load(1)
  svr.saveGame(filer,maxHealth,moves,level,gold,enemies,name)
  
  sty.story(filer,maxHealth,moves,level,gold,enemies,name)
  
if mode=="2":
  import ENDLESS as end
  ld.load(1)
  svr.saveGame(filer,maxHealth,moves,level,gold,enemies,name)
  end.endlessMode(filer,maxHealth,moves,level,gold,enemies,name)

