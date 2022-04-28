import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

class Grafico:
    #Constructor
    def __init__(self, dataset, col1, col2):
        self.dataset = dataset
        self.col1 = col1
        self.col2 = col2
    
    def grafico_barras(self, title):
        self.dataset = pd.read_csv("Pokemon.csv")
        self.dataset.groupby(self.col1)[self.col2].sum().plot(kind="bar")
        plt.title(title)
        plt.xlabel(None)
        plt.show()

class Media(Grafico):
    #Constructor
    def __init__(self, dataset, col1, col2):
        super().__init__(dataset, col1, col2)

    def calcular_media(self):
        self.dataset = pd.read_csv("Pokemon.csv")

        def calcular_xini():
            xini = []
            for i in range (len(self.dataset)):
                resultado = self.dataset[self.col1][i]*self.dataset[self.col2][i]
                xini.append(resultado)
            return xini

        self.dataset["XiNi"] = calcular_xini()
        suma_xini = self.dataset["XiNi"].sum()
        suma_ni = self.dataset[self.col2].sum()

        return suma_xini/suma_ni

class Std(Media):
    #Constructor
    def __init__(self, dataset, col1, col2):
        #Heredamos el constructor de la clase Media
        super().__init__(dataset, col1, col2)

    def calcular_std(self):
        self.dataset = pd.read_csv("Pokemon.csv")

        def columna_std():
            columna = []
            media = self.calcular_media()
            for i in range(len(self.dataset)):
                resultado = self.dataset[self.col2][i] * (self.dataset[self.col1][i] - media)*(self.dataset[self.col1][i] - media)
                columna.append(resultado)
            return columna

        self.dataset["Ni*((Xi-media)^2)"] = columna_std()
        suma_columna = self.dataset["Ni*((Xi-media)^2)"].sum()
        suma_ni = self.dataset[self.col2].sum()
        varianza = suma_columna/suma_ni

        return sqrt(varianza)


if __name__ == "__main__":

    #Hacemos el grafico de barras comparando ataque y defensa
    grafico = Grafico("Pokemon.csv","Attack","Defense")
    #grafico.grafico_barras("Grafico Ataque-Defensa")

    #Calculamos la media de ataque y defensa
    media = Media("Pokemon.csv","Attack","Defense")
    print ("La media es: {}".format(media.calcular_media()))

    #Calculamos la desviacion estandar de ataque y defensa
    std = Std("Pokemon.csv","Attack","Defense")
    print ("La desviacion estandar es: {}".format(std.calcular_std()))