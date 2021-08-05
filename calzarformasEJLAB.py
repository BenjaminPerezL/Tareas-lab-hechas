import os
import random
import colorama

colorama.init()

from colorama import init, Fore, Back, Style
init(autoreset = True)

def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None

TabBack = []
for i in range (10):
    TabBack.append([0]*10)

Cupos = 100
while Cupos > 0:
    os.system("cls")
    FilPos = random.randint(0,9)
    ColPos = random.randint(0,9)
    while TabBack[FilPos][ColPos] != 0:
        FilPos = random.randint(0,9)
        ColPos = random.randint(0,9)
    if FilPos<9 and ColPos<9 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos][ColPos+1]==0 and TabBack[FilPos+1][ColPos+1]==0 and TabBack[FilPos+1][ColPos]==0:
        TabBack[FilPos][ColPos] = 1
        TabBack[FilPos][ColPos+1] = 1
        TabBack[FilPos+1][ColPos+1] = 1
        TabBack[FilPos+1][ColPos] = 1
        Cupos -= 4
    elif FilPos<9 and ColPos>0 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos+1][ColPos] == 0 and TabBack[FilPos+1][ColPos-1] == 0 and TabBack[FilPos][ColPos-1] == 0:
        TabBack[FilPos][ColPos] = 1
        TabBack[FilPos+1][ColPos] = 1
        TabBack[FilPos+1][ColPos-1] = 1
        TabBack[FilPos][ColPos-1] = 1
        Cupos -= 4
    elif ColPos>0 and FilPos > 0 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos][ColPos-1] == 0 and TabBack[FilPos-1][ColPos-1] == 0 and TabBack[FilPos-1][ColPos] == 0:
        TabBack[FilPos][ColPos] =1
        TabBack[FilPos][ColPos-1]=1
        TabBack[FilPos-1][ColPos-1] =1
        TabBack[FilPos-1][ColPos] =1
        Cupos -= 4
    elif  FilPos > 0 and ColPos<9 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos-1][ColPos] == 0 and TabBack[FilPos-1][ColPos+1] == 0 and TabBack[FilPos][ColPos+1] == 0:
        TabBack[FilPos][ColPos] =1
        TabBack[FilPos-1][ColPos] =1
        TabBack[FilPos-1][ColPos+1] =1
        TabBack[FilPos][ColPos+1] =1
        Cupos -= 4
    else:
        if FilPos>0 and ColPos<9 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos-1][ColPos] == 0 and TabBack[FilPos][ColPos+1] == 0:
            TabBack[FilPos][ColPos] = 2
            TabBack[FilPos-1][ColPos] =2
            TabBack[FilPos][ColPos+1] =2
            Cupos += 3
        elif FilPos<9 and ColPos<9 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos+1][ColPos] == 0 and TabBack[FilPos+1][ColPos+1] == 0:
            TabBack[FilPos][ColPos] = 2
            TabBack[FilPos+1][ColPos] = 2
            TabBack[FilPos+1][ColPos+1] =2
            Cupos += 3
        elif FilPos>0 and ColPos>0 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos][ColPos-1] == 0 and TabBack[FilPos-1][ColPos-1] == 0:
            TabBack[FilPos][ColPos] = 2
            TabBack[FilPos][ColPos-1] = 2
            TabBack[FilPos-1][ColPos-1]=2
            Cupos += 3
        elif ColPos>0 and FilPos>0 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos-1][ColPos] == 0 and TabBack[FilPos][ColPos-1] == 0:
            TabBack[FilPos][ColPos] = 3
            TabBack[FilPos-1][ColPos] =3
            TabBack[FilPos][ColPos-1] =3
            Cupos += 3
        elif ColPos>0 and FilPos<9 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos+1][ColPos] == 0 and TabBack[FilPos+1][ColPos-1] == 0:
            TabBack[FilPos][ColPos] = 3
            TabBack[FilPos-1][ColPos] =3
            TabBack[FilPos-1][ColPos-1] =3
            Cupos += 3
        elif ColPos<9 and FilPos>0 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos-1][ColPos+1] == 0 and TabBack[FilPos][ColPos+1] == 0:
            TabBack[FilPos][ColPos] = 3
            TabBack[FilPos-1][ColPos+1] =3
            TabBack[FilPos][ColPos+1] =3
            Cupos += 3
        elif ColPos<9 and FilPos<9 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos][ColPos+1] == 0 and TabBack[FilPos+1][ColPos] == 0:
            TabBack[FilPos][ColPos] = 4
            TabBack[FilPos][ColPos+1] = 4
            TabBack[FilPos+1][ColPos]  = 4
            Cupos += 3
        elif ColPos>0 and FilPos<9 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos][ColPos-1] == 0 and TabBack[FilPos+1][ColPos-1] == 0:
            TabBack[FilPos][ColPos] = 4
            TabBack[FilPos][ColPos-1] = 4
            TabBack[FilPos+1][ColPos-1] = 4
            Cupos += 3
        elif ColPos<9 and FilPos>0 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos-1][ColPos] == 0 and TabBack[FilPos-1][ColPos+1] == 0:
            TabBack[FilPos][ColPos] = 4
            TabBack[FilPos-1][ColPos]=4
            TabBack[FilPos-1][ColPos+1] = 4
            Cupos += 3        
        elif ColPos>0 and FilPos<9 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos+1][ColPos] == 0 and TabBack[FilPos][ColPos-1] ==0:
            TabBack[FilPos][ColPos] =5
            TabBack[FilPos+1][ColPos] =5
            TabBack[FilPos][ColPos-1] =5
            Cupos+=3
        elif ColPos<9 and FilPos<9 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos][ColPos+1] == 0 and TabBack[FilPos+1][ColPos+1] ==0:
            TabBack[FilPos][ColPos] =5
            TabBack[FilPos][ColPos+1]=5
            TabBack[FilPos+1][ColPos+1] =5
            Cupos+=3
        elif ColPos>0 and FilPos>0 and TabBack[FilPos][ColPos] == 0 and TabBack[FilPos-1][ColPos-1] == 0 and TabBack[FilPos-1][ColPos] ==0:
            TabBack[FilPos][ColPos] =5
            TabBack[FilPos-1][ColPos-1]=5
            TabBack[FilPos-1][ColPos] =5
            Cupos+=3
        else:
            if TabBack[FilPos][ColPos] == 0:
                TabBack[FilPos][ColPos] = 6

    for j in range(10):
        for k in range(10):
            if TabBack[j][k] == 1:
                print( Back.RED+" "+str(TabBack[j][k])+" "," ",end="")
            elif TabBack[j][k] == 2:
                print( Back.YELLOW +" "+str(TabBack[j][k])+" "," ",end="")
            elif TabBack[j][k] == 3:
                print( Back.LIGHTGREEN_EX +" "+str(TabBack[j][k])+" "," ",end="")
            elif TabBack[j][k] == 4:
                print( Back.LIGHTCYAN_EX +" "+str(TabBack[j][k])+" "," ",end="")
            elif TabBack[j][k] == 5:   
                print( Back.BLUE +" "+str(TabBack[j][k])+" "," ",end="")
            elif TabBack[j][k] == 6:
                print( Back.MAGENTA+" "+str(TabBack[j][k])+" "," ",end="")
            else:
                print(TabBack[j][k],"   ",end="")
        print()
        print()
    input()






