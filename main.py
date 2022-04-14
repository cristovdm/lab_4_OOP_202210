# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:24:29 2022

@author: Cristobal Van der Meer
"""
from inventory import Inventory
from rental import Rental

library = Inventory()
lib_rental = Rental()
menu=True
print("¡Bienvenido a la Biblioteca!")
while menu==True:
    print("Seleccione una opción:")
    print("(1) Inventario de la biblioteca.")
    print("(2) Manejar Arriendos.")
    print("(3) Categorizar el Inventario.")
    print("(4) Modificar catalogo.")
    print("(0) Salir")
    option=input("- ")
    print()
    if option=="1":
        library.show_books()
    elif option=="2":
        sub_menu=True
        while sub_menu==True:
            print("[MANEJAR] Seleccione una opción:")
            print("(1) Registrar Usuario en la Biblioteca.")
            print("(2) Arrendar un ejemplar.")
            print("(3) Devolver un ejemplar.")
            print("(4) Historial de arriendo.")
            print("(0) Volver al menu.")
            sub_option=input("- ")
            print()
            if sub_option=="1":
                lib_rental.add_person()
            elif sub_option=="2":
                lib_rental.rent_book(library)
            elif sub_option=="3":
                lib_rental.return_book(library)
            elif sub_option=="4":
                lib_rental.show_rents()
            elif sub_option=="0":
                sub_menu=False
            else:
                print("[Error] Porfavor, seleccione una opcion valida.")
            print()
    elif option=="3":
        sub_menu=True
        while sub_menu==True:
            print("[CATEGORIZAR] Seleccione una opción:")
            print("(1) Buscar libros por GENERO.")
            print("(2) Buscar libros por AUTOR.")
            print("(0) Volver al menu.")
            sub_option=input("- ")
            print()
            if sub_option=="1":
                library.show_books_gender()
            elif sub_option=="2":
                library.show_books_author()
            elif sub_option=="0":
                sub_menu=False
            else:
                print("[Error] Porfavor, seleccione una opcion valida.")
            print()
    elif option=="4":
        sub_menu=True
        while sub_menu==True:
            print("[MODIFICAR] Seleccione una opción:")
            print("(1) Ingresar Nuevo Libro o Ejemplares.")
            print("(2) Eliminar Libros o Ejemplares.")
            print("(0) Volver al menu.")
            sub_option=input("- ")
            print()
            if sub_option=="1":
                library.add_book()
            elif sub_option=="2":
                library.remove_book()
            elif sub_option=="0":
                sub_menu=False
            else:
                print("[Error] Porfavor, seleccione una opcion valida.")
            print()
    elif option=="0":
        print("¡Muchas Gracias por visitar la Biblioteca! ¡Que tenga un muy buen dia! :)")
        menu=False
    else:
        print("[Error] Porfavor, seleccione una opcion valida.")
        print()