from time import *
def eName(enemies,gold):
  if gold<-10:
    return "debt collector"
  elif (enemies%69==0):
    return "diddy"
  elif (enemies%25==0):
    return "dinorphan"
  elif (enemies%7==0):
    return "kid toucher"
  elif (enemies%3==0):
    return "dino"
  elif (enemies%2==0):
    return "goblin"
  else:
    return "homeless orphan"

def eHealth(enemies,level,name,gold):
  if name=="goblin":
    hp=int(10*(enemies+level)/2+1)
    return hp
  elif name=="diddy":
    hp=int(100*(enemies+level)/2+1)
    return hp
  elif name=="dino":
    hp=int(30*((enemies/2)+level+1))
    return hp
  elif name=="dinorphan":
    hp=int(69*((enemies/2)+level+1))
    return hp
  elif name=="kid toucher":
    hp=25*(1+enemies+level)
    return hp
  elif name=="debt collector":
    hp=(gold*gold)
    return hp
  else:
    hp=int(10*(enemies/2+level)/2+1)
    return hp

def eAttacks(enemies,level,name,gold):
  if name=="goblin":
    attack=5*((enemies/2)+level+1)
    return attack
  elif name=="diddy":
    attack=50*((enemies/2)+level+1)
  elif name=="dino":
    attack=10*(enemies+level)/2+1
    return attack
  elif name=="dinorphan":
    attack=50*(enemies+level)/2+1
    return attack
  elif name=="kid toucher":
    attack=1+(enemies+level)/50
    return attack
  elif name=="debt collector":
    attack=69
    return attack
  else:
    attack=(enemies/2+level)/2+1
    return attack




def display(name,mHp,cHp,atk):
  print("Name:"+name)
  print("Health:",int(cHp),"/",int(mHp))
  print("Attack",atk)


def battle(name,gold,health,attack,enemies,level):
  print("Starting Battle")
  stats=[gold,health,attack,level]
  eN=eName(enemies,gold)
  eHp=int(eHealth(enemies,level,eN,gold)) 
  eAtk=eAttacks(enemies,level,eN,gold)
  ceHp=eHp
  cHealth=stats[1]
  while 0<cHealth and 0<ceHp:
    display(eN ,eHp,ceHp,eAtk)
    a=input("")
    display(name ,stats[1],cHealth,stats[2])
    a=input("")
    print("Attack:",stats[2],"Rest:",int((stats[1]*0.1)))
    print("7 to Rest or 9 to Attack")
    num=input("What will you do?")
    sleep(0.5)
    while num=="" or num!="7" and num!="9":
      print("Stop Fumbling")
      num=input("What will you do?")
    num=int(num)
    if (num==7):
      cHealth=cHealth+stats[1]*0.1
      print("Rested")
    if(num==9):
      print("Attacked")
      ceHp=ceHp-stats[2]
    sleep(0.1)
    if(ceHp%8==0  or ceHp<eHp/2):
      print("Enemy Rested",
      end="")
      ceHp=ceHp+eHp*0.1
    else:
      print("Enemy Dealt",eAtk,end="")
    a=input("")
  if (cHealth<0):
    stats[0]=-978
    print("You died")
  elif (ceHp<0):
    stats[0]=1+stats[0]+enemies+stats[1]
    print("Enemy Defeated")
  if (enemies%10==0):
    stats[3]=1+stats[3]
    print("You Leveled Up")
    print("Your Level:",stats[3])
    stats[1]=1+stats[1]
    sleep(1)
    
  return stats