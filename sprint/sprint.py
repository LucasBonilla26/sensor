from ctypes import sizeof
from scipy import signal
from scipy import integrate
from webbrowser import get
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from scipy.signal import argrelextrema
import math
from Graphic import Graphic

def derivative(amplitude,time,frequency):
    i=1
    diffLocalMaxim=[]
    while i < len(amplitude)-1:
        diffV = (amplitude[i+1] - amplitude[i-1])/2*frequency
        plot.scatter(time[i],diffV, color='yellow', s=15)
        diffLocalMaxim.append(diffV)
        i+=1
    return diffLocalMaxim

def showLocalMaxMin(vector,time):
    #Minimums and local maximums 
    localMaximums = argrelextrema(np.array(vector), np.greater)
    localMinimums = argrelextrema(np.array(vector), np.less)
    #Show minimums and local maximums 
    i=0
    while i < len(amplitude[localMaximums]):
        plot.scatter(time[localMaximums][i],amplitude[localMaximums][i], color='purple', s=15)
        plot.scatter(time[localMinimums][i],amplitude[localMinimums][i], color='red', s=15)
        i+=1

# Get x values of the sine wave
time = np.arange(0, 200, 0.2);
# Amplitude of the sine wave is sine of a variable like time
amplitude = np.sin(time)
# print(amplitude)
# Plot a sine wave using time and amplitude obtained for the sine wave
plot.plot(time, amplitude, color="lightblue")
# Give a title for the sine wave plot
plot.title('Sine wave')
# Give x axis label for the sine wave plot
plot.xlabel('Time')
# Give y axis label for the sine wave plot
plot.ylabel('Amplitude = sin(time)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
# Display the sine wave

graphic = Graphic()

file = pd.read_excel('datos/brutos1.xlsx',sheet_name = 'Center of Mass'); #May be a EXCEL

print(file.columns)
file.columns = ['Frame', 'CoM pos x', 'CoM pos y', 'CoM pos z', 'CoM vel x',
       'CoM vel y', 'CoM vel z', 'CoM acc x', 'CoM acc y', 'CoM acc z',
       'Unnamed: 10', 'Res']

x_value = file['CoM vel x']
y_value = file['CoM vel y']
res_value = file['Res']
print(len(x_value))

i=0
while i < len(x_value):
    graphic.res.append(np.sqrt(x_value[i]**2+y_value[i]**2))
    if (graphic.res[i] - res_value[i]) != 0:
        print("pene")
    i+=1
    
#print(graphic.res)

# while i < len():
#     x = file['Com pos x'][i]
#     y = file['Com pos y'][i]
#     np.sqrt(x**+y**)
   
#graphic.res.append()
#print(file['frame'])

# showLocalMaxMin(amplitude,time)

# # print(amplitude[localMaximums])
# # print(time[localMaximums])
# # print(amplitude[localMinimums])

# diffLocalMaxim = derivative(amplitude, time, 0.5)
# print(diffLocalMaxim);

# #Maximums and minimums local values for the derivative
# localMaximumsDiff = argrelextrema(np.array(diffLocalMaxim), np.greater)
# localMinimumsDiff = argrelextrema(np.array(diffLocalMaxim), np.less)

# print(localMaximumsDiff[0])
# print(localMinimumsDiff[0])

# #print(diffLocalMaxim[localMaximumsDiff[0]])
# localMaximumsDiff = np.array(localMaximumsDiff[0])
# localMinimumsDiff = np.array(localMinimumsDiff[0])

# i=0
# while i < len(localMaximumsDiff):
#     plot.scatter(time[localMaximumsDiff[i]],diffLocalMaxim[localMaximumsDiff[i]], color='green', s=15)
#     plot.scatter(time[localMinimumsDiff[i]],diffLocalMaxim[localMinimumsDiff[i]], color='black', s=15)
#     i+=1
    
# plot.show()