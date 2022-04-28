import pandas as pd

dt = pd.read_csv("Pokemon.csv")

eliminar = ["Type 2","Sp. Atk","Sp. Def","Speed","Generation","Legendary"]
for i in eliminar:
    del dt[i]

dt["Type2"] = "Water"

dt.to_csv("Nuevo Dataset.csv")