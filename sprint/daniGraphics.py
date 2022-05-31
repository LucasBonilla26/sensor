import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class daniGraphics():

    def __init__(self):
        self.data = []
        self.umbralized_data = []
    
    def load_file(self, file_path, sheet_name, n_values=-1):
        print("Reading file...")
        file = pd.read_excel(file_path, sheet_name) #May be a EXCEL

        file.columns = ['Frame', 'CoM pos x', 'CoM pos y', 'CoM pos z', 'CoM vel x',
            'CoM vel y', 'CoM vel z', 'CoM acc x', 'CoM acc y', 'CoM acc z',
            'Unnamed: 10', 'Res']

        print("Loading columns...")
        x_value = file['CoM vel x'][:n_values]
        y_value = file['CoM vel y'][:n_values]
        
        print("Calculating speed...")
        self.data = [np.sqrt(x**2 + y**2) for x,y in list(zip(x_value, y_value))]
        # return self.data

    def umbralize(self, factor=0):
        threshhold = np.mean(self.data)
        sigma = np.std(self.data)
        self.umbralized_data = [1 if x > threshhold + sigma * factor else 0 for x in self.data]

    def show(self):
        t = np.arange(0, len(self.data), 1)
        plt.figure()
        plt.plot(t, self.data)
        plt.plot(t, self.umbralized_data, 'ro')     
        plt.show()

         
if __name__ == "__main__":
    graphic = daniGraphics()
    graphic.load_file("brutos1.xlsx","Center of Mass", 30000)
    graphic.umbralize(2.0)
    graphic.show()
