#####################################################
#       Rock scissors Paper little game
#####################################################
import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#bienvenida, y recolección de la opción que el usuario elija 
print("Bienvenido a Piedra, Papel o Tijeras:")
eleccion = int(input("Que eliges? elige 0 por Roca, 1 por Papel o 2 Por Tijeras?:\n"))

#crear una elección aleatoria para el ordenador
computadorEleccion = random.randint(0, 2)
#guardar las figuras de piedra, papel o tijera 
figuras = [piedra, papel, tijera]
#mostrar lo que el jugador tiene, y lo que la computadora tiene
print(f"Jugador eligio: \n{figuras[eleccion]}\n computadora eligio:\n{figuras[computadorEleccion]}")

#calcular quien gano el juego, o si hubo un empate
if eleccion != computadorEleccion:
    if (eleccion == 0 and computadorEleccion == 2) or (eleccion == 2 and computadorEleccion == 1):
        print("Ganaste")
    elif (eleccion == 0 and computadorEleccion == 1) or (eleccion == 1 and computadorEleccion == 2):
        print("Perdiste")
    else:
        if (computadorEleccion == 0 and eleccion == 2) or (computadorEleccion == 2 and eleccion == 1):
            print("Perdiste")
        elif (computadorEleccion == 0 and eleccion == 1) or (computadorEleccion == 1 and eleccion == 2):
            print("Ganaste")
else:
    print("Empate")