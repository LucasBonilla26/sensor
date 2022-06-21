import numpy as np
from openpyxl import Workbook
import pandas as pd
import matplotlib.pyplot as plt
import cubic_spline
import xlsxwriter
from scipy import signal
from scipy.signal import find_peaks,savgol_filter
import datetime as dt

class Graphics():

    def __init__(self):
        self.data = []
        self.umbralized_data = []
        self.y_est_6 = []
        self.plot_graphic = []
        self.low_filter_data = []
        self.first_sheet = "General Information"
        self.start_time = 0
        self.frame = []
        
        ########################################################## DATOS MODIFICABLES ##############################################################################
        #Path donde se crea el excel con los datos segmentados
        #Ejemplo de ruta -> r'L:\.shortcut-targets-by-id\1Hs9L2qhd3LpjsVWp9cF_HjklAV_TVHBE\02_INVESTIGACIONES\Futbol\Territorio Gaming-Sta Teresa\04_Registros\Base\Sujeto1_EmmaRipalda\Comparación tecnologías\GestosEmma.xlsx'
        self.excel_file = r"C:\Users\BioEr\Desktop\futbol\Emma.xlsx"
        #Path al excel con los datos a segmentar
        self.load_filename = r"C:\Users\BioEr\Desktop\futbol\Emma_SportExtremadura.xlsx"
        #Máximos de la gráfica
        #Ejemplo de máximos -> [2733,14822,37474,43953,51529,55242,64208,69019,81255,85009,105422,135371,140114,144357,147569] EMMA [10214,23654,41955,52604,57964,61194,84129,88865,108930,113703,132883,157709,161259,165429,170570]
        self.max =  [250,1500,3000,4200,5400,6700]
        #Valor en X hasta cual se desea cargar los datos
        #NO PONER COMILLAS
        self.limit = -1
  
    def load_file(self, file_path, sheet_name, n_values=-1):
        print("Reading file...")
        
        file = pd.read_excel(file_path, sheet_name) #Excel
        
        self.take_start_time(file_path)

        file.columns = ['Frame', 'CoM pos x', 'CoM pos y', 'CoM pos z', 'CoM vel x',
            'CoM vel y', 'CoM vel z', 'CoM acc x', 'CoM acc y', 'CoM acc z']


        print("Loading columns...")
        x_value = file['CoM vel x'][:n_values]
        y_value = file['CoM vel y'][:n_values]
        self.frame = file['Frame'][:n_values]
        
        print("Calculating speed...")
        self.data = [np.sqrt(x**2 + y**2) for x,y in list(zip(x_value, y_value))]
        # return self.data

    def load_file2(self,file_path,sheet_name):
        file = pd.read_excel(file_path, sheet_name) #Excel
        return file

    def take_start_time(self,file_path):
        generalsheet = pd.read_excel(file_path, self.first_sheet)
        self.start_time = generalsheet.iat[2,1]
        print(self.start_time)
        print(type(self.start_time.hour))
        self.start_time = dt.time(self.start_time.hour,self.start_time.minute,self.start_time.second)

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
        #ax1.plot(np.arange(0,len(self.segment1),1), self.segment1)
        #ax3.plot(np.arange(0,len(self.plot_graphic),1), self.plot_graphic)             
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
        workbook = xlsxwriter.Workbook(self.excel_file)
        umbral = 0.31
                
        for x in self.max:
            aux = []
            frame_aux = []
            i = x
            while i > 0:
                if self.data[i] > umbral:
                    aux.append(self.data[i])
                    frame_aux = np.append(frame_aux,self.frame[i])
                else:
                    break
                i-=1

            
            self.segment1 = np.flip(aux)
            frame_aux = np.flip(frame_aux)

            i = x
            i+=1 
            while i < len(self.data):
                if self.data[i] > umbral:
                    self.segment1 = np.append(self.segment1,self.data[i])
                    frame_aux = np.append(frame_aux,self.frame[i])
                else:
                    break
                i+=1
        
            # print(len(self.segment1))
            # print(len(frame_aux))
            
            row=0
            worksheet = workbook.add_worksheet()
            
            for x in range(len(self.segment1)):
                worksheet.write(row,2,self.segment1[x])
                worksheet.write(row,0,frame_aux[x])
                seconds = dt.timedelta(seconds=frame_aux[x]/240/24/60/60*100000)
                frame_time = (dt.datetime.combine(dt.date(1,1,1),self.start_time) + seconds).time()
                print(frame_time)
                worksheet.write(row,1,frame_time.strftime("%H:%M:%S.%f"))
                row+=1

        workbook.close()

        return self.segment1

    def segment_manu(self,column):
        workbook = xlsxwriter.Workbook(r"C:\Users\BioEr\Desktop\GraficasManu\Gráfica5.xlsx")
        umbral = 0.0
        frame = np.arange(0,len(column),1)
        worksheet = workbook.add_worksheet()
                
        for x in self.max:
            aux = []
            frame_aux = []
            i = x
            while i > 0:
                if column[i] > umbral:
                    aux.append(column[i])
                    frame_aux = np.append(frame_aux,frame[i])
                else:
                    break
                i-=1

            values = np.flip(aux)
            frame_aux = np.flip(frame_aux)

            i = x
            i+=1 
            while i < len(column):
                if column[i] > umbral:
                    values = np.append(values,column[i])
                    frame_aux = np.append(frame_aux,frame[i])
                else:
                    break
                i+=1
        
            # print(len(self.segment1))
            # print(len(frame_aux))
            
            row=0
            #worksheet = workbook.add_worksheet()
            index = self.max.index(x)
            for x in range(len(values)):
                worksheet.write(row,index,values[x])
                #worksheet.write(row,0,frame_aux[x])
                # seconds = dt.timedelta(seconds=frame_aux[x]/240/24/60/60*100000)
                # frame_time = (dt.datetime.combine(dt.date(1,1,1),self.start_time) + seconds).time()
                # print(frame_time)
                # worksheet.write(row,1,frame_time.strftime("%H:%M:%S.%f"))
                row+=1

        workbook.close()

        return values
            
if __name__ == "__main__":
    graphic = Graphics()
    #graphic.load_file(r"C:\Users\BioEr\Desktop\FutbolBase\Sara_SportExtremadura.xlsx","Center of Mass") No poner nada para coger la gráfica entera
    graphic.load_file(graphic.load_filename,"Center of Mass", graphic.limit) 
    graphic.segment()
    
    #Graficas manuel
    # data = graphic.load_file2(r"C:\Users\BioEr\Desktop\sensor\sprint\CURVE_Dch.xlsx",r"Hoja1")
    # data.columns = ['G1','G2','G3','G4','G5']
    # graphic_data = data['G1']
    # print(graphic_data)
    # graphic.segment_manu(data['G1'])
    
    print("He terminado!")
    #graphic.salvog_filter()
    #graphic.show()
