Se agreg� un poco de dificultad al eliminar la posici�n 3 del ahorcado en la opci�n de 
dificultad "E".
Se agregaron el color "gray" y la fruta "mango" al diccionario words.
Se agrego un cartel de advertencia ante la selecci�n de una letra err�nea y se detalla en el mismo mensaje la cantidad de intentos restantes que el jugador tiene.
Se agrego una función que a partir de la clave aleatoria secretSet, busca en un diccionario de claves que contienen listas con algunas pistas para el competidor, de 
esta forma por cada fallo recibirá una pista en caso de que no esté ni siquiera cerca de la clase de palabra que debe acertar.

El programa trabaja con datos varios tipos de objeto, con diccionarios para las palabras, con una lista para definir el ahorcado, conteniendo elementos del tipo str.
La función split permite convertir el dato string de gran cantidad de información en una lista de str a partir de la cual puedo aplicar
 otra función, en nuestro caso la getRandomWord, que me permite seleccionar aleatoriamente la clave, y a partir de ella un dato aleatorio dentro de la misma, para obtener la 
 palabra secreta a encontrar por el jugador. Esto se logra utilizando las funciones random.randint() y random.choice(list(())).
 La función displayBoard, es la que actualiza el ahorcado, mostrandome el muñeco con un paso más al haber errado en la opción de la letra, y va mostrandome las letras en las que 
 se ha fallado y las que han sido acertadas en la variable blanks.
 La función getGuess() logra el ingreso de una letra válida en instancia de ejecución, es decir la transforma en minúscula, y rechaza la opción si ya fue ingresada anteriormente, o si no es una 
 letra.
 La función playAgain() evita la salida del while manteniendo la variable gameIsDone en False, y reseteando la palabra secreta para comenzar nuevamente el proceso si el jugador elige la opción yes.
 
 La PEP8 no es respetada, se ve a simple vista con la variable secretSet, debería definirse como secret_Set
 