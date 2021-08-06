import os
import random
import colorama
import time

print("")
colorama.init()
from colorama import init, Fore, Back, Style
init(autoreset = True)

Tablero = [] ; Figuras = ["☺","☻","♥","♣","♦","♠"] ; Puntaje = 0 ; Revisar = 1

#imprime el tablero completo, con ejes e intentos/puntajes
def ImprimirTablero():
    os.system('cls')
    print(Back.CYAN+Fore.BLACK+"   1  2  3  4  5  6  7  8  9 ", "  Intentos: ", Intentos)
    for i in range (20) : 
        if i<9:
            print(Back.CYAN+Fore.BLACK+" "+str(i+1), end="")
        else:
            print(Back.CYAN+Fore.BLACK+str(i+1), end="")
        for j in range(9):            
            if Tablero[i][j] == 1:
                print(Fore.BLACK+Back.YELLOW+" "+Figuras[0]+" ", end="")
            elif Tablero[i][j] == 2:
                print(Fore.WHITE+Back.BLACK+" "+Figuras[1]+" ", end="")
            elif Tablero[i][j] == 3:
                print(Fore.RED+Back.WHITE+" "+Figuras[2]+" ", end="")
            elif Tablero[i][j] == 4: 
                print(Fore.GREEN+Back.WHITE+" "+Figuras[3]+" ", end="")
            elif Tablero[i][j] == 5:
                print(Fore.BLUE+Back.WHITE+" "+Figuras[4]+" ", end="")
            elif Tablero[i][j] == 6:
                print(Fore.BLACK+Back.WHITE+" "+Figuras[5]+" ", end="")
        print("")
    print("Intentos: ",Intentos)
    print("Puntaje: ", Puntaje)

#elimina una ficha, suma su puntaje,  baja toda la columna (desde la fila de la ficha eliminada) y genera una nueva ficha random al inicio de la columna
def EliminarFicha(FilaJugada,ColumnaJugada):
    global Puntaje, Revisar
    for i in range (FilaJugada,-1,-1):
        if i==0:
            Tablero[i][ColumnaJugada] = random.randint(1,6)
        else:
            Tablero[i][ColumnaJugada] = Tablero[i-1][ColumnaJugada]
    Revisar = 1
    Puntaje+=Tablero[FilaJugada][ColumnaJugada]

#limpia toda una fila, usando la fx eliminarficha, con un caso minimo de 3 fichas seguidas iguales y un max de 5 fichas iguales
def LimpiarFila(FilaJugada):
    global Puntaje, Revisar
    for j in range(9):
        if j<5:
            if Tablero[FilaJugada][j]==Tablero[FilaJugada][j+1] and Tablero[FilaJugada][j]==Tablero[FilaJugada][j+2] and Tablero[FilaJugada][j]==Tablero[FilaJugada][j+3] and Tablero[FilaJugada][j]==Tablero[FilaJugada][j+4]:
                EliminarFicha(FilaJugada,j);EliminarFicha(FilaJugada,j+1);EliminarFicha(FilaJugada,j+2);EliminarFicha(FilaJugada,j+3);EliminarFicha(FilaJugada,j+4)

            elif Tablero[FilaJugada][j]==Tablero[FilaJugada][j+1] and Tablero[FilaJugada][j]==Tablero[FilaJugada][j+2] and Tablero[FilaJugada][j]==Tablero[FilaJugada][j+3]:
                EliminarFicha(FilaJugada,j);EliminarFicha(FilaJugada,j+1);EliminarFicha(FilaJugada,j+2);EliminarFicha(FilaJugada,j+3)
            elif Tablero[FilaJugada][j]==Tablero[FilaJugada][j+1] and Tablero[FilaJugada][j]==Tablero[FilaJugada][j+2]:
                EliminarFicha(FilaJugada,j);EliminarFicha(FilaJugada,j+1);EliminarFicha(FilaJugada,j+2)
        if j<6:
            if Tablero[FilaJugada][j]==Tablero[FilaJugada][j+1] and Tablero[FilaJugada][j]==Tablero[FilaJugada][j+2] and Tablero[FilaJugada][j]==Tablero[FilaJugada][j+3]:
                EliminarFicha(FilaJugada,j);EliminarFicha(FilaJugada,j+1);EliminarFicha(FilaJugada,j+2);EliminarFicha(FilaJugada,j+3)
            elif Tablero[FilaJugada][j]==Tablero[FilaJugada][j+1] and Tablero[FilaJugada][j]==Tablero[FilaJugada][j+2]:
                EliminarFicha(FilaJugada,j);EliminarFicha(FilaJugada,j+1);EliminarFicha(FilaJugada,j+2)
        if j<7:
            if Tablero[FilaJugada][j]==Tablero[FilaJugada][j+1] and Tablero[FilaJugada][j]==Tablero[FilaJugada][j+2]:
                EliminarFicha(FilaJugada,j);EliminarFicha(FilaJugada,j+1);EliminarFicha(FilaJugada,j+2)
        
#limpia todo el tablero (desde la fila que se elimino una ficha hacia arriba) de fichas iguales seguidas, de un min de 3 y max de 5, usando fx limpiarfila y eliminarficha
def LimpiarTablero():
    global Puntaje, FilaJugada, Revisar
    Revisar = 1
    while Revisar == 1:
        input("Presiona enter para ver si tienes otros grupos extra formados y obtener un bonus")
        Revisar = 0
        for i in range(FilaJugada,-1,-1):
            LimpiarFila(i)
        ImprimirTablero()
# # # programa principal # # #

#llenado del tablero con fichas
for i in range(20):
    Tablero.append([])
    for j in range(9):
        Tablero[i].append(random.randint(1,6))
        if j>1:
            while Tablero[i][j]==Tablero[i][j-1] and Tablero[i][j]==Tablero[i][j-2]:
                Tablero[i][j]= random.randint(1,6)


#comienzo de juego
Intentos = 20

ImprimirTablero()
while Intentos > 0:
    FilaJugada = int(input("Ingresa la fila de la ficha a eliminar: "));FilaJugada -= 1
    ColumnaJugada = int(input("Ingresa la columna de la ficha a eliminar: "));ColumnaJugada-=1
    EliminarFicha(FilaJugada,ColumnaJugada); ImprimirTablero(), input("Tu ficha fue eliminada, presiona enter para ver si juntaste un grupo de fichas iguales")
    LimpiarFila(FilaJugada); ImprimirTablero()
    LimpiarTablero()
    Intentos = Intentos - 1
    ImprimirTablero()
input()