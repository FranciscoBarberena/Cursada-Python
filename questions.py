import random

def elegirOpcion():
    opcionElegida = ""
    while (not opcionElegida):
        print("Elegí la categoría de palabras:\n1: Tipos de datos\n2: Otros")
        opcionElegida = int(input())
        match opcionElegida:
            case 1:
                palabrasEnJuego = categoriasDePalabras["tipos_de_datos"]
            case 2:
                palabrasEnJuego = categoriasDePalabras["otros"]
            case _:
                print("Opción inválida, intentá de nuevo")
                opcionElegida = ""
    return palabrasEnJuego
            
categoriasDePalabras = {"tipos_de_datos" : ["cadena","entero","lista"], 
                          "otros":["python","programa","funcion","bucle","variable"]}
palabra = random.choice(elegirOpcion())
adivinadas = []
intentos = 6
print("¡Bienvenido al Ahorcado!")
print()
while intentos > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letra in palabra:
        if letra in adivinadas:
            progress += letra + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        break
    print(f"Intentos restantes: {intentos}")
    print(f"Letras usadas: {', '.join(adivinadas)}")
    letra = input("Ingresá una letra: ")
    if (len(letra)==1 and letra.isalpha()):
        if letra in adivinadas:
            print("Ya usaste esa letra.")
        elif letra in palabra:
            adivinadas.append(letra)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            adivinadas.append(letra)
            intentos -= 1
            print("Esa letra no está en la palabra.")
    else:
        print("Entrada no válida")
    print()
else:
    print(f"¡Perdiste! La palabra era: {palabra}")
print (f"Puntaje final: {6-(6-intentos)}")