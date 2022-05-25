from ctypes import sizeof
from scipy import signal
from scipy import integrate
from scipy.signal import find_peaks
from webbrowser import get
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from scipy.signal import argrelextrema
import math
from Graphic import Graphic

graphic = Graphic()

file = pd.read_excel('datos/brutos1.xlsx',sheet_name = 'Center of Mass') #May be a EXCEL

print(file.columns)
file.columns = ['Frame', 'CoM pos x', 'CoM pos y', 'CoM pos z', 'CoM vel x',
       'CoM vel y', 'CoM vel z', 'CoM acc x', 'CoM acc y', 'CoM acc z',
       'Unnamed: 10', 'Res']

x_value = file['CoM vel x']
y_value = file['CoM vel y']
res_value = file['Res']
print(len(x_value))

i=0
c=0
while i < len(x_value):
    graphic.res.append(np.sqrt(x_value[i]**2+y_value[i]**2))
    if (graphic.res[i] - res_value[i]) != 0:
        c+=1
    i+=1



# Get x values of the sine wave
graphic.time = np.arange(0, len(graphic.res), 1)
# graphic.time = np.arange(0, 100, 0.1)
# graphic.res = np.sin(graphic.time)
# Plot a sine wave using time and amplitude obtained for the sine wave
plot.plot(graphic.time, graphic.res, color="lightblue")
# Give a title for the sine wave plot
plot.title('Graphic res')
# Give x axis label for the sine wave plot
plot.xlabel('Time')
# Give y axis label for the sine wave plot
plot.ylabel('Res = sqrt(velx^2+vely^2)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')

graphic.show_local_max_min()
peaks, _ = find_peaks(graphic.res,height=0)
print(peaks)
i=0
c=0
while i<len(peaks):
    if graphic.res[peaks[i]] != graphic.localMaxs[i]:
        #print("distintos")
        c+=1
    i+=1
print(c)
#plot.plot(peaks,graphic.res[np.array(peaks)],"x")
# i=0
# print("for")
# while i < len(graphic.localMaxs):
#     plot.scatter(graphic.time[graphic.indexMax[i]],graphic.localMaxs[i], color='purple', s=15)
#     i+=1

plot.show()
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