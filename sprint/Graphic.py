from scipy import signal
from scipy import integrate
from webbrowser import get
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Graphic:
    """Graphic Class"""

    frequency = 0
    __xAcceleration = []
    __xAcceleration = []
    res = []
    data = []
    
    def __init__(self):
        """Method's construsctor"""
        print(" created")
    
    def read_data():
        """
        Este es el docstring de la función
        """
        file = pd.read_excel('datos/brutos1.xlsx'); #May be a EXCEL
        return file
        
    def truncate(self,number, digits) -> float:
        """
        Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
        """
        nbDecimals = len(str(number).split('.')[1]) 
        if nbDecimals <= digits:
            return number
        stepper = 10.0 ** digits
        return math.trunc(stepper * number) / stepper
    

