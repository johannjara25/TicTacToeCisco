from random import randrange

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    turn = 2
    end = False
    make_list_of_free_fields(board)
    while turn < 10:
        sign = None
        while end == False:
            if turn % 2 == 0:
                enter_move(board)
                print("+-------+-------+-------+\n|       |       |       |\n|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |\n\
|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n\
|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |\n|       |       |       |\n\
+-------+-------+-------+\n|       |       |       |\n|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |\n\
|       |       |       |\n+-------+-------+-------+\n")
                turn +=1
                end = victory_for(board, sign)
            elif turn % 2 !=0:
                draw_move(board)
                print("+-------+-------+-------+\n|       |       |       |\n|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |\n\
|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n\
|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |\n|       |       |       |\n\
+-------+-------+-------+\n|       |       |       |\n|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |\n\
|       |       |       |\n+-------+-------+-------+\n")
                turn +=1
                end = victory_for(board, sign)
            break
    return


def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    global usuario
    v = 0
    usuario = input("Ingresa un número: ")
    while v == 0:
        try:
            usuario = int(usuario)
        except:
            usuario = input("Por favor ingresa un número entero: ")
        if type(usuario) == int:
            if usuario == 5:
                usuario = input("Ingresa otro valor, esta casilla ya fue seleccionada: ")
            elif usuario == 1:
                if usuario in tiles:
                    board[0][0] = "O"
                    tiles.remove(usuario)
                    v=1
                else:
                    usuario = input("Ingresa otro número, esa casilla está ocupada: ")
            elif usuario == 2:
                if usuario in tiles:
                    board[0][1] = "O"
                    tiles.remove(usuario)
                    v=1
                else:
                    usuario = input("Ingresa otro número, esa casilla está ocupada: ")
            elif usuario == 3:
                if usuario in tiles:
                    board[0][2] = "O"
                    tiles.remove(usuario)
                    v=1
                else:
                    usuario = input("Ingresa otro número, esa casilla está ocupada: ")
            elif usuario == 4:
                if usuario in tiles:
                    board[1][0] = "O"
                    tiles.remove(usuario)
                    v=1
                else:
                    usuario = input("Ingresa otro número, esa casilla está ocupada: ")
            elif usuario == 6:
                if usuario in tiles:
                    board[1][2] = "O"
                    tiles.remove(usuario)
                    v=1
                else:
                    usuario = input("Ingresa otro número, esa casilla está ocupada: ")
            elif usuario == 7:
                if usuario in tiles:
                    board[2][0] = "O"
                    tiles.remove(usuario)
                    v=1
                else:
                    usuario = input("Ingresa otro número, esa casilla está ocupada: ")
            elif usuario == 8:
                if usuario in tiles:
                    board[2][1] = "O"
                    tiles.remove(usuario)
                    v=1
                else:
                    usuario = input("Ingresa otro número, esa casilla está ocupada: ")
            elif usuario == 9:
                if usuario in tiles:
                    board[2][2] = "O"
                    tiles.remove(usuario)
                    v=1
                else:
                    usuario = input("Ingresa otro número, esa casilla está ocupada: ")
            else:
                usuario = input("Ingresa un valor válido, por favor:")
        else:
            usuario = input("Ingresa un valor válido, por favor:")
    return

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    for i in range(len(board)):
        for j in range(len(board)):
            tiles.append(board[i][j])
    return tiles

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    #draw = 0
    if board[0][0] == board [0][1] and board[0][0] == board [0][2]: #primera línea horizontal
        sign = board[0][0]
        if sign == "O":
            print("Has ganado, jugador")
            return True
        elif sign == "X":
            print("He ganado")
            return True
    elif board[0][0] == board [1][0] and board[0][0] == board [2][0]: #primera línea vertical
        sign = board[0][0]
        if sign == "O":
            print("Has ganado, jugador")
            return True
        elif sign == "X":
            print("He ganado")
            return True
    elif board[0][0] == board [1][2] and board[0][0] == board [2][2]: #diagonal a derecha
        sign = board[0][0]
        if sign == "O":
            print("Has ganado, jugador")
            return True
        elif sign == "X":
            print("He ganado")
            return True
    elif board[1][1] == board [1][0] and board[1][1] == board [1][2]: #segunda línea horizontal
        sign = board[1][0]
        if sign == "O":
            print("Has ganado, jugador")
            return True
        elif sign == "X":
            print("He ganado")
            return True
    elif board[2][0] == board [2][1] and board[2][0] == board [2][2]: #tercera línea horizontal
        sign = board[2][0]
        if sign == "O":
            print("Has ganado, jugador")
            return True
        elif sign == "X":
            print("He ganado")
            return True
    elif board[0][1] == board [1][1] and board[0][1] == board [2][1]: #segunda línea vertical
        sign = board[0][1]
        if sign == "O":
            print("Has ganado, jugador")
            return True
        elif sign == "X":
            print("He ganado")
            return True
    elif board[0][2] == board [1][2] and board[0][2] == board [2][2]: #tercera línea vertical
        sign = board[0][2]
        if sign == "O":
            print("Has ganado, jugador")
            return True
        elif sign == "X":
            print("He ganado")
            return True
    elif board[0][2] == board [1][1] and board[0][2] == board [2][0]: #diagonal a izquierda
        sign = board[0][2]
        if sign == "O":
            print("Has ganado, jugador")
            return True
        elif sign == "X":
            print("He ganado")
            return True
    else:
        draw = len(tiles)
        if draw == 1:
            return print("El juego queda empatado")
        else:
            return False


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    machine = randrange(1,9)
    s=0
    while s == 0:
        if machine == 5:
            machine = randrange(1,9)
        elif machine == 1:
            if machine in tiles:
                board[0][0] = "X"
                tiles.remove(machine)
                s=1
            else:
                machine = randrange(1,9)
        elif machine == 2:
            if machine in tiles:
                board[0][1] = "X"
                tiles.remove(machine)
                s=1
            else:
                machine = randrange(1,9)
        elif machine == 3:
            if machine in tiles:
                board[0][2] = "X"
                tiles.remove(machine)
                s=1
            else:
                machine = randrange(1,9)
        elif machine == 4:
            if machine in tiles:
                board[1][0] = "X"
                tiles.remove(machine)
                s=1
            else:
                machine = randrange(1,9)
        elif machine == 6:
            if machine in tiles:
                board[1][2] = "X"
                tiles.remove(machine)
                s=1
            else:
                machine = randrange(1,9)
        elif machine == 7:
            if machine in tiles:
                board[2][0] = "X"
                tiles.remove(machine)
                s=1
            else:
                machine = randrange(1,9)
        elif machine == 8:
            if machine in tiles:
                board[2][1] = "X"
                tiles.remove(machine)
                s=1
            else:
                machine = randrange(1,9)
        elif machine == 9:
            if machine in tiles:
                board[2][2] = "X"
                tiles.remove(machine)
                s=1
            else:
                machine = randrange(1,9)
        print(machine)
    return


#+-------+-------+-------+
#|       |       |       |
#|   1   |   2   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   6   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   8   |   9   |
#|       |       |       |
#+-------+-------+-------+ 

global sign
global turn
global machine
global end
global tiles
global cont

tiles = []
end = False
turn = 0
machine = 0
usuario = 0
cont = 2
board = [
        [1,2,3],
        [4,"X",6],
        [7,8,9]
    ]

print("¡Bienvenido a Tic Tac Toe!\nPara jugar, ingresa un valor del 1 al 9, siendo esta tu figura: O\n")
print("El tablero actualmente se ve así:\n")
print("+-------+-------+-------+\n|       |       |       |\n|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |\n\
|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n\
|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |\n|       |       |       |\n\
+-------+-------+-------+\n|       |       |       |\n|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |\n\
|       |       |       |\n+-------+-------+-------+\n")

display_board(board)