#Importacion biblotecas
from collections import namedtuple
import operator
from datetime import datetime
import random

#Declaracion de variables y creacion de listas asi como los ciclos a usar 
ciclo = True
ciclo_venta = True
lista_venta = []
Venta = namedtuple("Venta", ("desc_art", "cant_art", "costo"))
lista_precio = []
lista_cantidad = []
folio = [2, 3, 5]

#Se inicia el ciclo del menu principal para el programa
while ciclo:
    print("\n---MENU PRINCIPAL (Departamento Ventas)---\nFecha:",datetime.today().strftime("%d-%m-%Y"))

    print("1.Registro de venta")
    print("2.Consulta de venta")
    print("3.Salir")
    print("-"*30)
    op_menu = int(input())

    if op_menu == 1:
        #Se inicia el ciclo de registro de venta con opcion a registro multiples de articulos
        while ciclo_venta:
            print("\n***Venta***\n","Folio:",id(folio),     "Fecha:" ,datetime.today().strftime("%d-%m-%Y"))
            desc_art = input("Ingresa descripción del articulo: ")
            cant_art = int(input("Ingresa cantidad del articulo a vender: "))
            costo = int(input("Ingresa el precio del articulo: "))
            lista_precio.append(costo)
            lista_cantidad.append(cant_art)
            venta_registrada = Venta(desc_art,cant_art, costo)
            lista_venta.append(venta_registrada)
            agregar = input (f"¿Agregar articulo?\nsi. 1\nno. 2\n")
            
            #Despliegue de detalles de precio al final del registro de venta 
            if agregar == "2":
                print(lista_precio, lista_cantidad)
                multListas = list(map(operator.mul, lista_precio, lista_cantidad))
                sumaListas = sum(multListas)
                iva = sumaListas * .16
                sumaTotal = sumaListas + iva
                print("El precio final con el 16% de IVA agregado sería de: $",(sumaTotal))
                break
            

    #Opcion de detalles de venta
    elif op_menu == 2:
        print("\n***Mostar detalles de venta***\n",id(folio))
        for lista in lista_venta:
            print(f"Descripción del Articulo: {lista.desc_art}\nCantidad de el articulo: {lista.cant_art}\nprecio: {lista.costo}\n")
            print(sumaTotal)
        print("-"*30)

    #Opcion 3 para salir del programa
    elif op_menu == 3:
        break

    else:
        print("\nEsa opción no es válida")
