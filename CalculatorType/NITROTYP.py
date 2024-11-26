from random import *
import LOADING as ld
import CARS as cars

adj=["black","strong"]
nouns=[]

def makeSent(level):
  length=randint(1,level+randint(2,7))
  sentence=""
  for i in range(length):
    sentence+=adj[randint(0,len(adj)-1)]+" "
  return sentence

def check(sentence):
  print("Tutorial\n")
  print("Hit the blue button then the \ngreen button to covert the\nkeyboard to alphabet(The green\ntext above every button)\n")
  print("When the game starts,type the\nfirst word on the left,then\nclick enter on the bottom right")
  l=input("Are you ready??")
  totalChar=0
  total=0
  missed=0
  sent=sentence.split()
  csent=sent
  cur=0
  while len(csent)!= 0:
    print("\n\n\n\n\n\n\n")
    for j in csent:
      print(j+" ",end="")
    print("\n\n\n\n\n\n\n")
    type=input("\nType the first word>>")
    if (type!=sent[cur]):
      missed+=1
    totalChar+=len(sent[cur])
    total+=1
    del csent[0]
  stat=[total,totalChar,missed]
  print("\n\n\n\n\n\n\n")
  print("You finished!")
  print()
  print("Stats")
  print("Total Words",total)
  print("Total Characters",totalChar)
  print("Missed Words",missed)
  print("Cash",(total-missed)*50)
  print("\n")
  b=input("Continue>>")
  print("\n\n\n\n\n\n\n")
  return stat


ld.load(1)
cash=0
choice=""
level=1
races=0
car="Wagon"
while choice!="3":
  print("Welcome to nitrotype")
  print("\nLevel:",level)
  print("Races:",races)
  print("Car:",car)
  print("Cash:",cash)
  print("\n1.Race")
  print("2.Shop(NEW)")
  print("3.Quit")
  choice=input("Well?")
  if choice=="1":
    ld.load(1)
    sentence=makeSent(level)
    stat=check(sentence)
    cash+=(stat[0]-stat[2])*50
    races+=1
    if races%10==0:
      level+=1
    ld.load(1)
  elif choice=="2":
    ld.load(1)
    stat=cars.shop(cash,level,car)
    cash=stat[0]
    car=stat[1]
    ld.load(1)
  else:
    print("Invalid input")
