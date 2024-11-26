from time import *

def load(stop):
  count=0
  char=["|","/","-","\\"]
  while count<stop:
    for i in char:
      print("Loading        "+i)
      print("\n\n\n\n\n\n\n\n")
      sleep(0.2)
      
    count+=1
