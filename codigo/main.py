from scipy import signal
from scipy import integrate
from webbrowser import get
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Main code of the program
"""

def read_data():
    """
    Este es el docstring de la función
    """
    file = pd.read_csv('datos/pablodepie30_noparada.csv'); #May be a EXCEL
    return file

def getIntegration(acceleration):
    """
    packet_counter is not needed i guess
    """
    update_rate = 100 #60
    time_between_samples = 1/update_rate
    dataIntegrated = [sum(acceleration[:i]) * time_between_samples for i in range(len(acceleration))]
    return dataIntegrated

def getIntegrationV2(vector):
    vector[-1] = 0
    velocity = [0]
    time = 0.06
    for acc in acceleration:
        velocity.append(velocity[-1] + acc * time)
    
    del velocity[0]
    return velocity

def cumtrapz_example(x):
    dtime = 0.06
    dtVel = x * dtime;
    return np.cumsum([dtVel])

file = read_data()
#print(file)
file.columns = ['packetCounter','AccX','AccY','AccZ']
acceleration = np.array(file['AccX'])

#plt.plot(acceleration)

b,a = signal.butter(4,10/(100/2),'low',analog = False)
y = signal.filtfilt(b,a, acceleration)
y -= 9.8

i=0
while i < len(y):
    if -0.6 < y[i] < 0.6:
        y[i] = 0.0
    i+=1

plt.plot(y)
# velocity = cumtrapz_example(y)
# position = cumtrapz_example(velocity)
velocity = integrate.cumtrapz(y,dx=1/60,initial=0);

i=0
while i < len(velocity):
    if -0.3 < velocity[i] < 0.3:
        velocity[i] = 0.0
    i+=1

position = integrate.cumtrapz(velocity,dx=1/60,initial=0);
position *= 100
# velocity = getIntegration(acceleration)
# position = getIntegration(velocity)

# velocity = getIntegrationV2(acceleration)
# position = getIntegrationV2(velocity)

#print(max(velocity))
#print(min(velocity))

#print(max(acceleration))
#print(min(acceleration))
# # print(position)
# print(position[65])
# print(position[-1])

#plt.figure(1)
#plt.plot(y)
plt.plot(velocity)
#plt.plot(y)
# plt.figure(2)
plt.plot(position)
plt.ylabel('Sensor')
plt.show()





# Rotation Matrix
# cos(x) -sin(x)
# sin(x) cos(x)