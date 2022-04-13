
import string
letra = input("Ingrese la letra")

texto = "Hemos estado todo el fin de semana trabajando en python"
letra = letra.lower()
if letra in string.ascii_letters:
    texto = texto.split()   #Como quiero recorre todas las palabras neceisto la lista 
    for elem in texto:
        if elem.lower().startswith(letra):
            print(elem)
else:
    print("Usted no ha ingresado una letra.")
        

