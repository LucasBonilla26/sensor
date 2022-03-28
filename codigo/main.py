from asyncio import read
from scipy import integrate
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

def getPosition(packet_counter, acceleration):
    
    update_rate = 60
    time = []

    #Change for
    #for i in packet_counter:
        #time[] = i/60

        #speed = integrate(acceleration,time) #(funcion, variable)
        #print(speed)
        #return speed


file = read_data()
#print(file)
file.columns = ['1','2','3','4']
print(file['1'])
getPosition(file['1'],file['2'])