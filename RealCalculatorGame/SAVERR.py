
# Data Sharing
from LOADING import checkInt
from ti_system import recall_list,store_list

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
getMsg = "\n What Save File? (Overwrite = 0)\n Well?"
getNum = "What Save File do you want to overwrite?"
invalid = "Invalid Input"

def storeName(name,save):
  save.append(0)
  for char in name: 
    for i in range(0,26,1):
      if char == alphabet[i]:
        save.append(i+1)
  return save

def getName(file):
  namel=recall_list(int(file))
  snamel=namel
  #t=input()
  for i in namel:
    if i==0:
      break
    snamel=snamel[1:]
  snamel=snamel[1:]
  name=""
  for num in snamel:
    name=name+alphabet[int(num)-1]
  return name


def getSave(file):
  loader=recall_list(file)
  return loader

def display(start,stop):
  for i in range(start,stop):
    loader=recall_list(i)
    name=str(getName(int(i)))
    print(" File",i)
    print(" Name:"+name)

def getFile(start,stop):
  inp=int(input(getMsg))
  while stop<=inp and inp<=start:
    print(invalid)
    inp=int(input(getMsg))
  if inp==0:
    inp=int(input(getNum))
    while start<=inp and inp<=stop:
      print(invalid)
      inp=int(input(getNum))
    return (inp*10)
  else:
    return inp



def saveGame(file,health,attack,level,gold,enemies,name):
  saver=1
  if 1<=file<=3:
    saver=file
    savef=[health,attack,level,gold,enemies]
    savef=storeName(name,savef)
    store_list(int(saver),savef)
    print("Saved!")
  else:
    print("Failed to save")


#saveGame(2,1000,147,15,47,33,"abby")