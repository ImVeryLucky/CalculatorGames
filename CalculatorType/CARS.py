
cars=["Mustang","Prius","Tesla","Porshe","Ford T"]
carCost=[10,6969,2,88,1947]

def browse():
  cur=1
  a="y"
  while a!="3":
    for i in range(cur,cur+3):
      if 0<=i and i<len(cars):
        print(i,cars[i])
        print("Cost:",carCost[i])
    print("\n1 to go back")
    print("2 to go forward")
    print("3 to quit")
    a=input("Well?")
    if a=="1":
      cur-=3
    elif a=="2":
      cur+=3
    else:
      print("Invalid")


def shop(gold,level,ccar):
  cash=gold
  car=ccar
  i="gg"
  while i!="3":
    print("Are you here to browse or buy?")
    print("1 to browse")
    print("2 to buy")
    print("3 to quit")
    i=input("Well?")
    if i=="1":
      browse()
    elif i=="2" :
      j=input("What do you want to buy?")
      while j.isdigit()==False:
        j=input("Invalid input.What do you want to buy?")
      j=int(j)
      if j>len(car):
        print("Not a car")
      else:
        if cash>=carCost[j]:
          cash-=carCost[j]
          car=cars[j]
        else:
          print("Not enough cash")
    else:
      print("Invalid")
  stat=[cash,car]
  return stat

