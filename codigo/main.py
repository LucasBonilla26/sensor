#from scipy import integrate
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
    file = pd.read_csv('datos/acceleration.csv'); #May be a EXCEL
    return file

def getIntegration(packet_counter, dataToIntegrate):
    """
    packet_counter is not needed i guess
    """
    acceleration = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 2]
    update_rate = 10 #60
    time_between_samples = 1/update_rate
    dataIntegrated = [sum(acceleration[:i]) * time_between_samples for i in range(len(acceleration))]
    return dataIntegrated

def getIntegrationV2():
    acceleration = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 2, 0]
    velocity = [0]
    time = 0.1
    for acc in acceleration:
        velocity.append(velocity[-1] + acc * time)
    del velocity[0]
    
    return velocity

def cumtrapz_example(x):
    dtime = 0.1
    dtVel = x * dtime;
    return np.cumsum([dtVel])

file = read_data()
print(file)
file.columns = ['packetCounter','AccX','AccY','AccZ']
#print(file['Acc_X'].to_list())
# print(file['AccX'])
# # print(file['AccX'])
# # velocity_x = getIntegration(file['packetCounter'],file['AccX'])
# # position = getIntegration(file['packetCounter'],velocity_x)
# # print(position)
# #print(getIntegrationV2())
# #print(getIntegration(file['packetCounter'],file['AccX']))
# #acceleration = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 5.0, 2.0, 0.0, -1.0, -3.5, -3.5, -3.5, -2.1, -1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0])
acceleration = file['AccX']
print(acceleration)
velocity = cumtrapz_example(acceleration)
position = cumtrapz_example(velocity)
# result = cumtrapz_example(acceleration)
plt.plot(acceleration)
plt.plot(velocity)
# plt.plot(velocity[74:106])
plt.plot(position)
# print(position[len(position)-1]-position[0])
# print(position[-1])
plt.ylabel('some numbers')
plt.show()



# Rotation Matrix
# cos(x) -sin(x)
# sin(x) cos(x)