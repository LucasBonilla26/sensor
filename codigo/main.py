from asyncore import read
import pandas as pd
import numpy as np

"""
Main code of the program
"""

def read_data():
    """
    Este es el docstring de la función
    """
    file = pd.read_csv('datos/datos.csv'); #May be a EXCEL
    return file

file = read_data()
#print(file)
file.columns = ['1','2','3','4']
print(file['1'])