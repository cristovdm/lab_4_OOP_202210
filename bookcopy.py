# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:20:21 2022

@author: Cristobal Van der Meer
"""
from numpy import random

class BookCopy:
    def __init__(self, book_name, book_author, book_category, book_value):
        num_serie = random.randint(1,100000)
        self.b_info = [book_name, book_author, book_category, book_value, num_serie]
