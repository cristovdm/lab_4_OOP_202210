# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:19:14 2022

@author: Cristobal Van der Meer
"""
class Book:
    def __init__(self, book_name, book_author, book_category, book_value):
        self.b_info = [book_name, book_author, book_category, book_value, 1, 0]