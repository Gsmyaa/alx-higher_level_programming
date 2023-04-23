#!/usr/bin/python3
"""Defines module that inherit from list"""

class MyList(list):
    """Implement sorted for printing built-in list class"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
    
