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

def getIntegration(packet_counter, dataToIntegrate):
    """
    packet_counter is not needed i guess
    """
    update_rate = 60
    time_between_samples = 1/update_rate
    dataIntegrated = [sum(dataToIntegrate[:i]) * time_between_samples for i in range(len(dataToIntegrate))]
    return dataIntegrated


file = read_data()
#print(file)
file.columns = ['packetCounter','AccX','AccY','AccZ']
print(file['AccX'])
velocity_x = getIntegration(file['packetCounter'],file['AccX'])
position = getIntegration(file['packetCounter'],velocity_x)
print(position)


# Rotation Matrix
# cos(x) -sin(x)
# sin(x) cos(x)