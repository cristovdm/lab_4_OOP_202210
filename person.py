# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:16:13 2022

@author: Cristobal Van der Meer
"""
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, first_name):
        self.name = first_name
    @abstractmethod
    def checkout(self):
        pass
