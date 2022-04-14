# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:23:32 2022

@author: Cristobal Van der Meer
"""
from employee import Employee
from customer import Customer

class Rental:
    def __init__(self):
        self.rents = []
        self.people = []
    def add_person(self):
        client_name = input("Ingrese su nombre: ")
        role = "."
        while role !="empleado" and role !="cliente":
            role = input("Ingrese su rol (empleado/cliente): ")
        if role=="empleado":
            client = Customer(client_name)
        else:
            client = Employee(client_name)
        client.checkout()
        self.people.append(client)
    def rent_book(self, inventory):
        if len(self.people)!=0:
            print("En la Biblioteca se encuentran registrados los siguientes personas: ")
            for i in range(len(self.people)):
                print(self.people[i].name)
            person = input("Ingrese su nombre: ")
            valid_person=False
            for i in range(len(self.people)):
                if self.people[i].name==person:
                    valid_person=True
                    pos_i=i
            if valid_person==True:
                print(f"¡Bienvenido devuelta {person}! Porfavor sigue las siguientes instrucciones...")
                n_serie = int(input("Ingrese el numero de serie del libro a arrendar: "))
                rented = False
                can_rent = True
                for i in range(len(self.rents)):
                    if self.rents[i][4]==n_serie and self.rents[i][7]=="Pendiente":
                        can_rent = False
                for i in range(len(inventory.bookscopy)):
                    if inventory.bookscopy[i][4]==n_serie and can_rent==True:
                        print(f"¡El ejemplar del libro {inventory.bookscopy[i][4]} correctamente!")
                        print("Para finalizar el procedimiento, complete los siguientes datos: ")
                        day= int(input("Ingrese el numero de día (Ejemplo: 4): "))
                        self.rents.append([inventory.bookscopy[i][0],inventory.bookscopy[i][1], inventory.bookscopy[i][2],inventory.bookscopy[i][3],n_serie,day,self.people[pos_i].name,"Pendiente"])
                        for j in range(len(inventory.books)):
                            if inventory.books[j][0]==inventory.bookscopy[i][0]:
                                inventory.books[j][5]+=1
                        rented=True
                        print(f"¡Un ejemplar del libro {inventory.bookscopy[i][0]} ha sido arrendado exitosamente!")
                        print(f"Recuerda que el libro tiene un precio diario de ${inventory.bookscopy[i][3]}.")
                        print("Tendras 14 dias maximo para devolver el ejemplar sin atrasos ¡Ojala lo disfrutes!")
                if rented==False:
                    print("[Error] El libro ingresado no se encuentra disponible para arrendar.")
            else:
                print("[Error] El nombre de la persona ingresada no se encuentra registrada en la Biblioteca :(")
        else:
            print("[Error] No se han encontrado personas registradas en la Biblioteca :(")
    def return_book(self, inventory):
        returned=False
        if len(self.people)!=0:
            print("En la Biblioteca se encuentran registrados los siguientes personas: ")
            for i in range(len(self.people)):
                print(self.people[i].name)
            person = input("Ingrese su nombre: ")
            valid_person=False
            for i in range(len(self.people)):
                if self.people[i].name==person:
                    valid_person=True
            if valid_person==True:
                print(f"¡Bienvenido devuelta {person}! Porfavor sigue las siguientes instrucciones...")
                for j in range(len(self.rents)):
                    if person==self.rents[j][6]:
                        print(f"({i}) Libro: {self.rents[i][0]}, Autor: {self.rents[i][1]}, Nº Serie: {self.rents[i][4]}, Dia Arrendado: {self.rents[i][5]}, Estado: {self.rents[i][7]}") 
                n_serie = int(input("Ingrese el numero de serie del libro que desea devolver: "))
                for i in range(len(self.rents)):
                    if self.rents[i][4]==n_serie and self.rents[i][7]=="Pendiente" and self.rents[i][6]==person:
                        dia2= int(input("Ingrese el numero de día devuelto (Ejemplo: 6): "))
                        if self.rents[i][5]<=dia2:
                            payment = (dia2-self.rents[i][5])*self.rents[i][3]
                            self.rents[i][7]=["Devuelto", dia2]
                            print("¡Gracias por devolver el libro a la Biblioteca! :)")
                            if self.people[i].value==0.6:
                                print(f"Has pagado a la Biblioteca ${payment*0.6} por tener el libro {dia2-self.rents[i][5]} dias por ser Empleado.")
                            else:
                                print(f"Has pagado a la Biblioteca ${payment} por tener el libro {dia2-self.rents[i][5]} dias por ser Cliente.")
                            if self.rents[i][5]+14<dia2:
                                self.rents[i][7]=["Devuelto Atrasado", dia2]
                                print("PD: Sin embargo, lo has devuelto con atraso :(")
                            for j in range(len(inventory.books)):
                                if inventory.books[j][0]==self.rents[i][0]:
                                    inventory.books[j][5]-=1
                            returned=True
        if returned==False:
            print("[Error] Ha habido un error al devolver el libro. Compruebe que este disponible, que el dia devuelto ingresado es superior al dia arrendado, que el numero de serie sea valido, etc.")
    def show_rents(self):
        print("A continuacion, se despliega el historial de todos los arriendos: ")
        for i in range(len(self.rents)):
            print(f"({i}) Nombre Arrendatario: {self.rents[i][6]}, Libro: {self.rents[i][0]}, Nº Serie: {self.rents[i][4]}, Dia Arrendado: {self.rents[i][5]}, Estado: {self.rents[i][7]}")  
