#AUTOR: Alexis Uriarte
#PROYECTO FINAL DE ITI: APLICACIÓN EN PYTHON

#CREACION DE FUNCIONES:
#funcion muestraMenu, muestra el menu principal
def muestraMenu():
    print("|","="*32,"|")
    print("|          RESTAURANTE S.A         |")
    print("|                MENÚ              |")
    print("|","="*32,"|")
    print("| A | Desayuno                     |")
    print("| B | Almuerzo                     |")
    print("| C | Cena                         |")
    print("| D | ========== SALIR =========== |")
    print("|","="*32,"|")

#funcion muestraSubMenu, muestra las lista de desayuno, almuerzo y cena
#recibe como parámetro la categoria escogida en el menu principal
def muestraSubMenu(categoria):
    #si elije "A" imprime la lista de Desayuno
    if categoria == "A":
        print("|          Desayuno                |")
        print("|","="*32,"|")
        print("| A | Café               | S/.4.50 |")
        print("| B | Chocolate          | S/.5.00 |")
        print("| C | Jugo de Fresas     | S/.9.00 |")
        print("| D | Jugo de Papaya     | S/.8.00 |")
        print("| E | Pan con Pollo      | S/.7.00 |")
        print("| F | Pan con Jamón      | S/.7.00 |")
        print("| G | Pan con Tortilla   | S/.7.00 |")
        print("| J | ========== SALIR =========== |")
        print("|","="*32,"|")
    #si elije "B" imprime la lista de Almuerzo
    elif categoria == "B":
        print("|           Almuerzo               |")
        print("|","="*32,"|")
        print("| A | Café               | S/.4.50 |")
        print("| B | Chocolate          | S/.5.00 |")
        print("| C | Jugo de Fresas     | S/.9.00 |")
        print("| D | Jugo de Papaya     | S/.8.00 |")
        print("| E | Pan con Pollo      | S/.7.00 |")
        print("| F | Pan con Jamón      | S/.7.00 |")
        print("| G | Pan con Tortilla   | S/.7.00 |")
        print("| J | ========== SALIR =========== |")
        print("|","="*32,"|")
    #si elije "B" imprime la lista de Almuerzo
    elif categoria == "C":
        print("|             Cena                 |")
        print("|","="*32,"|")
        print("| A | Pizza Exprés       | S/.9.50 |")
        print("| B | Ensalada Campera   | S/.7.50 |")
        print("| C | Gazpacho           | S/.6.00 |")
        print("| D | Caldo de Gallina   | S/.6.00 |")
        print("| E | Pollo al horno     | S/.5.50 |")
        print("| F | Menestrón          | S/.4.00 |")
        print("| G | ========== SALIR =========== |")
        print("|","="*32,"|")

#PROCESO:
#se realiza todo el algoritmo del trabajo

#EJECUCIÓ DEL PROGRAMA: