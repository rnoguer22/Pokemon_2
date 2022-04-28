import pandas as pd
from main import *

dt = pd.read_csv("Pokemon.csv")

eliminar = ["Type 1","Type 2","Sp. Atk","Sp. Def","Speed","Generation","Legendary","Total"]
for i in eliminar:
    del dt[i]

dt["weapon"] = "kick"

print (dt)

dt.to_csv("Nuevo Dataset.csv")