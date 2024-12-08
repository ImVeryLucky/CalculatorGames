
def checkInt(msg):
  out=input(msg)
  while out.isdigit()==False:
    print("Invalid")
    out=input(msg)
  out=int(out)
  return out

def weapons(gold,atk):
  cgold=gold
  attack=atk
  print("Welcome to the weapon shop")
  print("You have ",attack,"attack")
  print("Availible Weapons")
  attackName=["Gold Dagger  ","Bronze Sword ","Iron Sword   ","Steel Sword  ","Plat Halberd "]
  for i in range(0,len(attackName),1):
    print(i+1,attackName[i]+"Cost:",(2*i+1), "Atk:",(i*i+1))
  print("Type number of weapon to purchase, or 0 to return back")
  inputW=checkInt("What would you like to buy?")
  while inputW!=0:
    if 0<inputW<6 and 0<cgold:
      c=checkInt("Quantity?")
      cgold-=c*(2*(inputW-1)+1)
      attack+=c*((inputW-1)**2+1)
      print("Item Bought")
    else:
      print("Invalid Input")
    inputW=checkInt("What else would you like to buy?")
  print("Heading back to shop...")
  stat=[cgold,attack]
  return stat

def armors(gold,health):
  cgold=gold
  chealth=health
  print("Welcome to the armor shop")
  print("You have ",health,"health")
  print("Availible Armors")
  armorName=["Leather Armor","Bronze Armor ","Iron Armor   ","Steel Armor  ","Platnum Armor"]
  for i in range(0,len(armorName),1):
    print(i+1,armorName[i]+"Cost:",(5*i+1), "Def:",(i*i*7))
  print("Type number of armor to purchase, or 0 to return back")
  inputA=checkInt("What would you like to buy?")
  while inputA!=0:
    if 0<inputA<6 and 0<cgold:
      c=checkInt("Quantity?")
      cgold-=c*(5*(inputA-1)+1)
      chealth+=c*((inputA-1)**2)*7
    else:
      print("Invalid")
    inputA=checkInt("What else would you like to buy?")
  print("See you soon")
  stat=[cgold,chealth]
  return stat

def shop(gold,weapon,maxHealth):
  cash=gold
  attack=weapon
  health=maxHealth
  inp="y"
  while inp!="0":
    cash=int(cash)
    print("\nWelcome to the shop    \nWe sell armor and weapons here")
    print("\nYou have ",cash," gold\n")
    print("Enter: \n 7 for weapons \n 9 for armor\n 0 to quit\n")
    inp=input("Where would you like to go?")
    if inp=="7":
      print("Heading to Weapons...")
      sub=weapons(cash,attack)
      cash=sub[0]
      attack=sub[1]
    elif inp=="9":
      print("Heading to Armors...")
      sub=armors(cash,health)
      cash=sub[0]
      health=sub[1]
    else:
      print("Invalid Input")
      print("Try Again")
  print("Heading Back...\n")
  stat=[cash,attack,health]
  return stat
