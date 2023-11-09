import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

intentos = 0

print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100. ¡Adivina!")

while True:
    try:
        intento = int(input("Tu suposición: "))
        intentos += 1

        if intento < numero_secreto:
            print("Más alto. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Más bajo. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break
    except ValueError:
        print("Ingresa un número válido.")

print(f"El número secreto era {numero_secreto}. ¡Gracias por jugar!")
