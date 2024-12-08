from time import sleep

def load(stop):
  count=0
  char=["|","/","-","\\"]
  while count<stop:
    for i in char:
      print("Loading        "+i)
      print("\n\n\n\n\n\n\n\n")
      sleep(0.2)
      
    count+=1

def pri(msg,time):
  for i in msg:
    print(i,end="")
    sleep(time)

def timer(sec):
  for i in range(sec,0,-1):
    print(i,end="")
    print("\n\n\n\n\n\n\n\n\n")
    sleep(0.8)

