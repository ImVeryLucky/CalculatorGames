from time import sleep

def findEnemy(enemies,level,gold):
  if(gold < -10):
    eStats=["debt collector",int(gold*gold),69]
  elif (enemies%69==0):
    eStats=["diddy",int(100*(enemies+level)/2+1),50*((enemies/2)+level+1)]
  elif (enemies%25==0):
    eStats=["dinorphan",int(69*((enemies/2)+level+1)),50*(enemies+level)/2+1]
  elif (enemies%7==0):
    eStats=["kid toucher",25*(1+enemies+level),1+(enemies+level)/50]
  elif (enemies%3==0):
    eStats=["dino",int(30*((enemies/2)+level+1)),10*(enemies+level)/2+1]
  elif (enemies%2==0):
    eStats=["goblin",int(10*(enemies+level)/2+1),5*((enemies/2)+level+1)]
  else:
    eStats=["homeless orphan",int(10*(enemies/2+level)/2+1),(enemies/2+level)/2+1]
  return eStats

def display(name,mHp,cHp,atk):
  print("Name:"+name)
  print("Health:",int(cHp),"/",int(mHp))
  print("Attack",atk)


def battle(name,gold,health,attack,enemies,level):
  print("Starting Battle")
  stats=[gold,health,attack,level]
  enStats=findEnemy(enemies,level, gold)
  eN=eStats[0]
  eHp=eStats[1] 
  eAtk=eStats[2]
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






