
def displayInfo(name,hp,attack,e,level):
  print("+------------------------------+")
  print("Name: "+name)
  print("Health: ",hp)
  print("Attack: ",attack)
  print("Enemies: ",e)
  print("Level: ",level)
  print("+------------------------------+",end="")
  e=input("")
  




def gameOver(name,health,attack,level):
  print("GAME OVER")
  print("STATS")
  print("Name: "+name)
  print("Health: ",health)
  print("Attack: ",attack)
  print("Level: ",level)