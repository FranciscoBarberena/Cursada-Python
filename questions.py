import random
# Funcionalidad 4 agregada dando opción de jugar de nuevo, soporte para mayúsculas y minúsculas indistintamente, funcion elegirOpcion() removida y puntajeRonda() agregada
def puntajeRonda (intentosRestantes, intentosIniciales):
    return intentosIniciales-(intentosIniciales-intentosRestantes)

categoriasDePalabras = {"tipos_de_datos" : ["cadena","entero","lista"], 
                          "otros":["python","programa","funcion","bucle","variable"]}
puntajeTotal = 0
jugarCategoria = True
while jugarCategoria: 
    opcionElegida = ""
    while (not opcionElegida):
        print("Elegí la categoría de palabras:\n1: Tipos de datos\n2: Otros")
        opcionElegida = int(input())
        match opcionElegida:
            case 1:
                listaDePalabrasEnJuego = categoriasDePalabras["tipos_de_datos"]
            case 2:
                listaDePalabrasEnJuego = categoriasDePalabras["otros"]
            case _:
                print("Opción inválida, intentá de nuevo")
                opcionElegida = ""
    listaDePalabrasEnJuego = random.sample(listaDePalabrasEnJuego,len(listaDePalabrasEnJuego))
    cantidadDePartidas = 0
    jugarRonda = True
    while(jugarRonda):
        adivinado = []
        intentos = 6
        palabra = listaDePalabrasEnJuego[cantidadDePartidas]
        print("¡Bienvenido al Ahorcado!")
        print()
        while intentos > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letra in palabra:
                if letra in adivinado:
                    progress += letra + " "
                else:
                    progress += "_ "
            print(progress)
            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                print("¡Ganaste!")
                break
            print(f"Intentos restantes: {intentos}")
            print(f"Letras usadas: {', '.join(adivinado)}")
            letra = input("Ingresá una letra: ").lower()
            if (len(letra)==1 and letra.isalpha()):
                if letra in adivinado:
                    print("Ya usaste esa letra.")
                elif letra in palabra:
                    adivinado.append(letra)
                    print("¡Bien! Esa letra está en la palabra.")
                else:
                    adivinado.append(letra)
                    intentos -= 1
                    print("Esa letra no está en la palabra.")
            else:
                print("Entrada no válida")
            print()
        else:
            print(f"¡Perdiste! La palabra era: {palabra}")
        puntajeTotal += puntajeRonda(intentos,6)
        print (f"Puntaje de ronda: {puntajeRonda(intentos,6)}")
        otraRonda = ""
        if cantidadDePartidas < len(listaDePalabrasEnJuego)-1:
            while(not otraRonda):
                otraRonda = input("Avanzar a la siguiente palabra de la categoría? (SI/NO)").upper()
                match otraRonda:
                    case "SI":
                        jugarRonda = True
                        cantidadDePartidas += 1
                    case "NO": # Termina el juego
                        jugarRonda = False
                        jugarCategoria = False
                    case _:
                        otraRonda = ""
        else: 
            otraCategoria = ""
            while(not otraCategoria):
                otraCategoria = input("Ya adivinaste todas las palabras de la categoría. Volver al menú de selección de categoría? Tu puntaje se guardará (SI/NO)").upper()
                match otraCategoria:
                    case "SI":
                        jugarCategoria = True
                    case "NO": # Termina el juego
                        jugarCategoria = False
                    case _:
                        otraCategoria = ""
                jugarRonda = False
print(f"Terminó el juego. Puntaje final: {puntajeTotal}")