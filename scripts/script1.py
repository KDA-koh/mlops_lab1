import pandas as pd
import sys
import os
import io

os.makedirs('data/stage1', exist_ok=True)

scp = pd.read_csv("/home/kda/mlops_lab1/data/raw/Sport car price.csv")
Engine_Size_map = {"Gas":0, "Electric":1}
Year = {2019:0, 2020:1, 2021:2, 2022:3, 2023:4}

scp["Engine Size (L)"] = scp["Engine Size (L)"].map(Engine_Size_map)
scp["Year"] = scp.Year.map(Year)
scp.to_csv('/home/kda/mlops_lab1/data/stage1/Sport car price.csv')
