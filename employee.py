# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:17:56 2022

@author: Cristobal Van der Meer
"""
from person import Person

class Employee(Person):
    def checkout(self):
        self.value = 0.6
        return self.value