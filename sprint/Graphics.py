import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cubic_spline
from scipy import signal
from scipy.signal import find_peaks,savgol_filter

class Graphics():

    def __init__(self):
        self.data = []
        self.umbralized_data = []
        self.y_est_6 = []
        self.plot_graphic = []
        self.low_filter_data = []
        self.segment1 = []
        self.frame = []
        
    def load_file(self, file_path, sheet_name, n_values=-1):
        print("Reading file...")
        file = pd.read_excel(file_path, sheet_name) #May be a EXCEL

        file.columns = ['Frame', 'CoM pos x', 'CoM pos y', 'CoM pos z', 'CoM vel x',
            'CoM vel y', 'CoM vel z', 'CoM acc x', 'CoM acc y', 'CoM acc z',
            'Unnamed: 10', 'Res']

        print("Loading columns...")
        x_value = file['CoM vel x'][:n_values]
        y_value = file['CoM vel y'][:n_values]
        self.frame = file['Frame'][:n_values]
        
        print("Calculating speed...")
        self.data = [np.sqrt(x**2 + y**2) for x,y in list(zip(x_value, y_value))]
        # return self.data

    def umbralize(self, factor=0):
        threshhold = np.mean(self.data)
        sigma = np.std(self.data)
        self.umbralized_data = [1 if x > threshhold + sigma * factor else 0 for x in self.data]

    def show(self):
        t = np.arange(0, len(self.data), 1)
        fig1, ax1 = plt.subplots()
        fig2, ax2 = plt.subplots()
        fig3, ax3 = plt.subplots()
        # plt.figure(1)
        ax2.plot(t, self.data, label='originals')
        # plt.figure(2)
        ax1.plot(np.arange(0,len(self.segment1),1), self.segment1)
        ax3.plot(np.arange(0,len(self.plot_graphic),1), self.plot_graphic)             
        plt.show()
    
    def cubic_spline_smooth(self):
        # The number of knots can be used to control the amount of smoothness
        t = np.arange(0, len(self.data), 1)
        model_6 = cubic_spline.get_natural_cubic_spline_model(t, self.data, minval=min(t), maxval=max(t), n_knots=2000)
        self.y_est_6 = model_6.predict(t)
    
    def salvog_filter(self):
        self.plot_graphic = savgol_filter(self.segment1, 350, 3)
        
    def low_filter(self):
        b,a = signal.butter(4,24/(240/2),'low',analog = False)
        self.low_filter_data = signal.filtfilt(b,a, self.data)
        
    def segment(self):
        n = 15
        umbral = 0.31
        max = [14820]
        aux = []
        frame_aux = []
        for x in max:
            i = x
            while i > 0:
                if self.data[i] > umbral:
                    aux.append(self.data[i])
                    frame_aux.append(self.frame[i])
                else:
                    break
                i-=1

            self.segment1 = np.flip(aux)
            frame_aux = np.flip(frame_aux)

            i = x    
            while i < len(self.data):
                if self.data[i] > umbral:
                    self.segment1 = np.append(self.segment1,self.data[i])
                else:
                    break
                i+=1
        
        return self.segment1
            
if __name__ == "__main__":
    graphic = Graphics()
    graphic.load_file("datos/brutos1.xlsx","Center of Mass",-1)
    #graphic.umbralize(2.0)
    #graphic.cubic_spline_smooth()
    #graphic.low_filter()
    
    print(graphic.segment())
    graphic.salvog_filter()
    graphic.show()
