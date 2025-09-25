##CLASE 16

print("PIEDRA, PAPEL O TIJERA")

name_player1 = input("JUGADOR 1 INGRESA TU NOMBRE")
name_player2 = input("JUGADOR 2 INGRESA TU NOMBRE")

valid_moves = ["piedra","papel","tijera"]

#Eligiendo movimientos
move_player1 = input("Jugado 1 elija: piedra, papel o tijera")
move_player2 = input("Jugador 2 elija: piedra, papel o tijera")

#fixing string capitalization
move_player1 = move_player1.lower()
move_player2 = move_player2.lower()


#Verificando si el movimiento es valido
if move_player1 or move_player2 not in valid_moves:
    print("Por favor ingrese un moviento valido")
    move_player1 = input("Jugado 1 elija: piedra, papel o tijera")
    move_player2 = input("Jugador 2 elija: piedra, papel o tijera")

#Quien es el ganador

#(EMPATE)
if move_player1 == move_player2:
    print("HA SIDO UN EMPATE")
# PIEDRA LE GANA A TIJERA
# TIJERA LE GANA A PAPEL 
# PAPEL LE GANA A PIEDRA
if move_player1 == "tijera":




