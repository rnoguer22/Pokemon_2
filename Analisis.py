import pandas as pd
import matplotlib.pyplot as plt

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

if __name__ == "__main__":

    grafico = Grafico("Pokemon.csv","Attack","Defense")
    grafico.grafico_barras("Grafico Ataque-Defensa")