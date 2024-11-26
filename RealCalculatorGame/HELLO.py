
def GetName():
  print("")
  print("Enter your name.")
  print("(Press [alpha] for letters \nor [alpha] again for Uppercase")
  print("")
  n=input("What is your name? ")
  print("Hello ",n)
  print("")
  return n

def start():
  i=input("would you like to play a game?(1/0)")
  while i!="1":
    print("you have no choice -_-")
    i=input("would you like to play a game?(1/0)")
