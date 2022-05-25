from threading import local
from scipy import signal
from scipy import integrate
from webbrowser import get
from scipy.signal import argrelextrema
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

class Graphic:
    """Graphic Class"""

    def __init__(self):
        """Method's construsctor"""
        print("created")
        self.frequency = 1
        self.derivative = []
        self.res = []
        self.data = []
        self.time = []
        self.localMaxs = []
        self.localMins = []
        self.indexMax = []
        self.indexMin = []
    
    def read_data(self):
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

    def show_local_max_min(self):
        """
        Show local maximums and minimums of the vector
        """
        #Minimums and local maximums 
        localMaximums = argrelextrema(np.array(self.res), np.greater)
        localMinimums = argrelextrema(np.array(self.res), np.less)
        #Show minimums and local maximums
        print(localMaximums)
        print(len(localMaximums[0]))
        i=0
        while i < len(localMaximums[0]):
            self.indexMax.append(localMaximums[0][i])
            self.indexMin.append(localMinimums[0][i])
            self.localMaxs.append(self.res[self.indexMax[i]])
            self.localMins.append(self.res[self.indexMin[i]])
            # print("res=" + str(self.res[indexMax]))
            # plot.scatter(self.res[indexMax],self.res[indexMax], color='purple', s=15)
            # plot.scatter(self.res[indexMin],self.res[indexMin], color='red', s=15)
            i+=1
        return 0

    def derivative_cal(self):
        """
        Obtain the derivative of vector
        """
        i=1
        while i < len(self.data)-1:
            diffV = (self.data[i+1] - self.data[i-1])/2*self.frequency
            self.derivative.append(diffV)
            i+=1
        return self.derivative

    

