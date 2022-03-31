Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
numero_aleatorio = random.randrange(5)
gane = False
print("Tenés 5 intentos para adivinar un entre 0 y 99")
intento = 1
while intento < 6 and not gane:
    numero_Ingresado = int(input('Ingresa tu número: '))
    if numero_Ingresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
        intento += 1
if not gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))