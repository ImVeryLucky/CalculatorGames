import SAVERR as svr
import SHOP as shp
import BATTLE as btl
import INFO as inf
import LOADING as ld 


options = "Enter:\n8 to go to the shop \n6 to battle \n4 for info \n2 to quit\n" 

def endlessMode(file, maxHealt, move, leve, gol, enemie, nam):   
    filer = file
    maxHealth = maxHealt
    moves = move
    level = leve
    gold = gol
    enemies = enemie
    name = nam

    exit = "y"

    while exit!="n":
        svr.saveGame(filer,maxHealth,moves,level,gold,enemies,name)
        print("Hello "+ name)
        print("You have ",int(gold)," gold" )
        print()
        print(options)
        i=input("What will you do?")
        while i != "8" and i!="6"and i!="4"and i!="2" :
            print("That wasnt an option.\nTry again")
            print(options )
            i=input("What will you do?")
        if i=="8":
            ld.load(1)
            #print("Heading to shop...")
            stat=shp.shop(gold,moves,maxHealth)
            gold=stat[0]
            moves=stat[1]
            maxHealth=stat[2]
            ld.load(1)
            
        elif i=="6" :
            ld.load(1)
            #print("Heading to battle...")
            stats=btl.battle(name,gold,maxHealth,moves,enemies,level)
            ld.load(1)
            gold=stats[0]
            moves=stats[2]
            maxHealth=stats[1]
            level=stats[3]
            if gold==-978:
            exit="n"
            print("Game Over")
            inf.displayInfo(name,maxHealth,moves,enemies,level)
            svr.saveGame(filer,0,0,0,0,0,"empty")
            enemies=enemies+1
        elif i=="4" :
            ld.load(1)
            #print("Heading to info...")
            inf.displayInfo(name,maxHealth,moves,enemies,level)
            ld.load(1)
        elif i=="2" :
            print("I hope you had fun!")
            exit="n"
            inf.displayInfo(name,maxHealth,moves,enemies,level)