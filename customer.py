# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:18:38 2022

@author: Cristobal Van der Meer
"""
from person import Person

class Customer(Person):
    def checkout(self):
        self.value = 1
        return self.value
