#Segun una lista quitar los numeros repetidos

def clean_list (n) :
    a = set(n) #set no recibe valores repetidos
    return list(a)
print(clean_list([1, 2, 2, 2, 3, 4, 4, 4]))

#Dada una lista de números, juntar los repetidos 
#y mostrar cuantos hay de cada uno.

from collections import defaultdict

def contar_ocurrencias(numeros):
    # Creamos un diccionario con valores predeterminados de tipo int
    contador = defaultdict(int)
    
    # Contamos las ocurrencias de cada número en la lista
    for num in numeros:
        contador[num] += 1
    
    # Mostramos el resultado
    for num, cantidad in contador.items():
        print(f"El número {num} aparece {cantidad} {'vez' if cantidad == 1 else 'veces'}.")

# Lista de números de ejemplo
numeros = [1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 4, 4]

# Llamamos a la función para contar las ocurrencias
contar_ocurrencias(numeros)



        

