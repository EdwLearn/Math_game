import random
import math

def jugarConMates():
    print("¡Bienvenido al juego matemático! Te voy a dar una operación y me respondes con el resultado. Si es correcta, ¡Ganaste! Sino, ¡Perdiste!")
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operacion = random.randint(0, 3)

    #suma
    if operacion == 0:
        resultado = a + b
        pregunta = int(input(f'¿Cuánto es {a} + {b}?: '))
        if pregunta == resultado:
          print("¡Sí! ¡Ganaste!")
        else:
          print(f'¡No! ¡Perdiste! Era {resultado}')   

    #división
    elif operacion == 1:
        a = random.randint(1, 100)
        b = random.randint(1, 10)

        resultado = a / b

        while resultado != 1 or resultado != 2 or resultado != 3 or resultado != 4 or resultado != 5 or resultado != 6 or resultado != 7 or resultado != 8 or resultado != 9:
          a = random.randint(1, 100)
          b = random.randint(1, 10)
          resultado = a / b
          if resultado == 1 or resultado == 2 or resultado == 3 or resultado == 4 or resultado == 5 or resultado == 6 or resultado == 7 or resultado == 8 or resultado == 9:
            pregunta = int(input(f'¿Cuánto es {a} / {b}?: '))
            if pregunta == resultado:
                print("¡Sí! ¡Ganaste!")
                break
            else:
                print(f'¡No! ¡Perdiste! Era {resultado}')
                break

    #resta
    elif operacion == 2:
        if a < b:
            a = random.randint(b, 100)
            resultado = a - b
            pregunta = int(input(f'¿Cuánto es {a} - {b}: ')) 
            if pregunta == resultado:
              print("¡Sí! ¡Ganaste!")
            else:
              print(f'¡No! ¡Perdiste! Era {resultado}')        
        else:
            resultado = a - b
            pregunta = int(input(f'¿Cuánto es {a} - {b}?: '))
            if pregunta == resultado:
              print("¡Sí! ¡Ganaste!")
            else:
              print(f'¡No! ¡Perdiste! Era {resultado}')     

    #multiplicación
    elif operacion == 3:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        resultado = a * b
        pregunta = int(input(f'¿Cuánto es {a} * {b}?: '))
        if pregunta == resultado:
          print("¡Sí! ¡Ganaste!")
        else:
          print(f'¡No! ¡Perdiste! Era {resultado}') 

    #potencia
    elif operacion == 4:
      a = random.randint(0, 20)
      b = random.randint(0, 3)
      resultado = a ** b
      pregunta = int(input(f'¿Cuánto es {a} ** {b}?: '))
      if pregunta == resultado:
          print("¡Sí! ¡Ganaste!")
      else:
          print(f'¡No! ¡Perdiste! Era {resultado}')

    #raíz cuadrada
    elif operacion == 5:
      a = random.randint(0, 200)
      resultado = math.sqrt(a)

      #verificar la raíz cuadrada es exacta
      while resultado != 1 or resultado != 2 or resultado != 3 or resultado != 4 or resultado != 5 or resultado != 6 or resultado != 7 or resultado != 8 or resultado != 9 or resultado != 10 or resultado != 11 or resultado != 12 or resultado != 13 or resultado != 14:
        a = random.randint(0, 200)
        resultado = math.sqrt(a)
        if resultado == 1 or resultado == 2 or resultado == 3 or resultado == 4 or resultado == 5 or resultado == 6 or resultado == 7 or resultado == 8 or resultado == 9 or resultado == 10 or resultado == 11 or resultado == 12 or resultado == 13 or resultado == 14:
            pregunta = int(input(f'¿Cuál es la raíz cuadrada de {a}?: '))
            if pregunta == resultado:
                print("¡Sí! ¡Ganaste!")
                break
            else:
                print(f'¡No! ¡Perdiste! Era {resultado}')
                break

jugarConMates()