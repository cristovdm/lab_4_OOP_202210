# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:19:28 2022

@author: Cristobal Van der Meer
"""
from book import Book
from bookcopy import BookCopy

class Inventory:
    def __init__(self):
        self.books = []
        self.bookscopy = []
    def add_book(self):
        book_name=input("Ingrese el nombre del Libro: ")
        book_exists=False
        for i in range(len(self.books)):
            if self.books[i][0]==book_name:
                book_exists = True
                print(f"El libro ingresado ya existe, y tiene un total de {self.books[i][4]} ejemplares.")
                n_bookcopys = int(input("Seleccione el numero de ejemplares a agregar: "))
                for j in range(n_bookcopys):
                    book_copy = BookCopy(self.books[i][0],self.books[i][1],self.books[i][2],self.books[i][3])
                    for i in range(len(self.books)):
                        if book_copy.b_info[0]==self.books[i][0]:
                            self.books[i][4]+=1
                    self.bookscopy.append(book_copy.b_info)
                print(f"{n_bookcopys} Ejemplares agregados correctamente.")
        if book_exists==False:
            print("Puesto que es un libro nuevo, rellene los siguientes datos: ")
            author=input("Ingrese el autor del Libro: ")
            gender=input("Ingrese el genero del Libro: ")
            price=float(input("Ingrese el precio por dia de arriendo del Libro: "))
            book = Book(book_name,author,gender,price)
            book_copy = BookCopy(book_name,author,gender,price)
            self.books.append(book.b_info)
            self.bookscopy.append(book_copy.b_info)
    def remove_book(self):
        book_name=input("Ingrese el nombre del Libro o Ejemplar a eliminar: ")
        book_exists=False
        for i in range(len(self.books)):
            if self.books[i][0]==book_name:
                book_exists = True
                print(f"El libro tiene un total de {self.books[i][3]} ejemplares.")
                print("[Advertencia] Si elimina todos los ejemplares de un libro, el libro se eliminara")
                n_bookscopy = int(input("Seleccione el numero de ejemplares a eliminar: "))
                if self.books[i][4]-n_bookscopy>=0:
                    self.books[i][4]-= n_bookscopy
                    cb_removed= 0
                    i2=0
                    removing=True
                    while removing==True:
                        if self.bookscopy[i2][0]==book_name:
                            self.bookscopy.pop(i2)
                            cb_removed+=1
                            i2=0
                        else:
                            i2+=1
                        if cb_removed==n_bookscopy:
                            removing=False
                    print(f"{n_bookscopy} Ejemplares eliminados correctamente.")
                else:
                    print("[Error] El numero de ejemplares ingresado es superior al numero de ejemplares disponibles.")
                if self.books[i][3]==0:
                    self.books.pop(i)
                    print("El Libro se ha eliminado.")
                break
        if book_exists==False:
            print("[Error] El nombre del libro escogido no existe en la Biblioteca.")
    def show_books(self):
        print("El inventario de la Biblioteca es el siguiente: ")
        print()
        for i in range(len(self.books)):
            print(f"Nombre: {self.books[i][0]}, Autor: {self.books[i][1]}, Categoria: {self.books[i][2]}, Costo/dia: {self.books[i][3]}, Ejemplares: {self.books[i][4]}, Arrendados: {self.books[i][5]}")
            o=1
            for i2 in range(len(self.bookscopy)):
                if self.books[i][0]==self.bookscopy[i2][0]:
                    print(f"[Ejemplar Nº{o} del libro {self.bookscopy[i][0]}] Numero de Serie: {self.bookscopy[i2][4]}")
                    o+=1
            print()
        if len(self.books)==0:
            print("No hay ningun libro en la Biblioteca, lo lamento :(")
            print()
    def show_books_gender(self):
        gender=input("Ingrese el genero: ")
        for i in range(len(self.books)):
            if self.books[i][2]==gender:
                print(f"Nombre: {self.books[i][0]}, Autor: {self.books[i][1]}, Categoria: {self.books[i][2]}, Costo/dia: {self.books[i][3]}, Ejemplares: {self.books[i][4]}, Arrendados: {self.books[i][5]}")
                o=1
                print()
                for i2 in range(len(self.bookscopy)):
                    if self.books[i][0]==self.bookscopy[i2][0]:
                        print(f"[Ejemplar Nº{o} del libro {self.bookscopy[i2][0]}] Numero de Serie: {self.bookscopy[i2][4]}")
                        o+=1
                print()
        if len(self.books)==0:
            print("No hay ningun libro en la Biblioteca con ese genero, lo lamento :(")
            print()
    def show_books_author(self):
        author=input("Ingrese el autor: ")
        for i in range(len(self.books)):
            if self.books[i][1]==author:
                print(f"Nombre: {self.books[i][0]}, Autor: {self.books[i][1]}, Categoria: {self.books[i][2]}, Costo/dia: {self.books[i][3]}, Ejemplares: {self.books[i][4]}, Arrendados: {self.books[i][5]}")
                o=1
                print()
                for i2 in range(len(self.bookscopy)):
                    if self.books[i][0]==self.bookscopy[i2][0]:
                        print(f"[Ejemplar Nº{o} del libro {self.bookscopy[i2][0]}] Numero de Serie: {self.bookscopy[i2][4]}")
                        o+=1
                print()
        if len(self.books)==0:
            print("No hay ningun libro en la Biblioteca con ese autor, lo lamento :(")
            print()
