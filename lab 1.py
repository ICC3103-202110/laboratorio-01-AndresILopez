# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:40:42 2021

@author: andre
"""

from numpy import random
def generate_board(a):
    board = []
    c = 0
    for i in range():
        board.append([])
        for j in range():
            c += 1
            board[i].append(c)
            board[i].append(c)
    return board  
def random_board(board):
    filas = len(board)
    columnas = len(board[0])
    for i in range(filas):
        for j in range(columnas):
            aleatorio_i = random.randint(0, columnas -1)
            aleatorio_j = random.randint(0, filas -1)
            temporary_board = board[i][j]
            board[i][j] = board[aleatorio_i][aleatorio_j]
            board[aleatorio_i][aleatorio_j] = temporary_board
    return board
def show_board1(board):
    z = board.copy()
    salida = ""
    for i in range(len(z)):
        for j in range(len(z[i])):
            salida += "*"
        salida += "\n"
    return salida    
def show_board2(board, coordinates1, coordinates2):
    u = board.copy()
    for i in range(len(u)):
        for j in range(len(u[i])):
            if coordinates1[0]==i and coordinates1[1]==j:
                u[i][j] = board[i][j]
            elif coordinates2[0]==i and coordinates2[1]==j:
                u[i][j] = board[i][j]
            else:
                u[i][j] = "*"
    salida = ""
    for i in range(len(u)):
        for j in range(len(u[i])):
            salida += str(u[i][j])
        salida += "\n"
    return salida
def find_a_pair(coordinates1, coordinates2, board, repeat, puntos):
    g = coordinates1[0]
    k = coordinates1[1]
    w = coordinates2[0]
    q = coordinates2[1]
    if board[g][k] == board[w][q]:
        board[g].pop(k)
        board[w].pop(q)
        repeat = True
        puntos += 1
    else:
        repeat = False
    return repeat,board,puntos  
def check_winner(board,jugador,terminado):
    k = True
    for i in range(len(board)):
        if len(board[i]) == 0:
            continue
        else:
            k = False
            break
    if k:
        terminado = True
    if terminado:
        print ("termino el juego, ha ganado ",jugador)
    return terminado
a = int(input("numero de cartas para jugar "))
generate_board(a)
random_board(board)
terminado = False
repeat = True
puntos1 = 0
puntos2 = 0
while terminado == False:
    while repeat:
        print ("turno de jugador 1, tiene ",puntos1," puntos")
        show_board1(board)
        a2 = int(input("ingresa la fila de la 1era carta que quieres voltear "))
        a3 = int(input("ingresa la columna de la 1era carta que quieres voltear "))
        coordinates1 = [a2,a3]
        a4 = int(input("ingresa la fila de la 2da carta que quieres voltear "))
        a5 = int(input("ingresa la columna de la 2da carta que quieres voltear "))
        coordinates2 = [a4,a5]
        show_board2(board, coordinates1, coordinates2)
        find_a_pair(coordinates1, coordinates2, board, repeat, puntos1)
        check_winner(board,"jugador1",terminado)
        if terminado:
            break
    if terminado:
        break
    repeat = True
    while repeat:
        print ("turno jugador 2, tiene",puntos2," puntos")
        show_board1(board)
        a2 = int(input("ingresa la fila de la 1era carta que quieres voltear "))
        a3 = int(input("ingresa la columna de la 1era carta que quieres voltear "))
        coordinates1 = [a2,a3]
        a4 = int(input("ingresa la fila de la 2da carta que quieres voltear "))
        a5 = int(input("ingresa la columna de la 2da carta que quieres voltear "))
        coordinates2 = [a4,a5]
        show_board2(board, coordinates1, coordinates2)
        find_a_pair(coordinates1, coordinates2, board, repeat, puntos2)
        check_winner(board,"jugador2",terminado)
    
