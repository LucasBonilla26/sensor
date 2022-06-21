from Graphics import Graphics

if __name__ == "__main__":
    graphic = Graphics()
    #graphic.load_file(r"C:\Users\BioEr\Desktop\FutbolBase\Sara_SportExtremadura.xlsx","Center of Mass") No poner nada para coger la gráfica entera
    #graphic.load_file(graphic.load_file,"Center of Mass", graphic.limit) 
    #graphic.segment()
    
    #Graficas manuel
    data = graphic.load_file2(r"C:\Users\BioEr\Desktop\sensor\sprint\CURVE_Dch.xlsx",r"Hoja1")
    data.columns = ['G1','G2','G3','G4','G5']
    graphic_data = data['G1']
    print(graphic_data)
    graphic.segment_manu(data['G5'])
    
    print("He terminado!")
    #graphic.salvog_filter()
    #graphic.show()
