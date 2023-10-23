import pandas as pd
import numpy as np
import sys
import os
import io

os.makedirs('data/stage1', exist_ok=True)

scp = pd.read_csv("/home/kda/mlops_lab1/data/raw/Sport car price.csv")

scp["Engine Size (L)"] = np.where((scp["Car Make"] == "Rimac") | (scp["Car Make"] == "Tesla"), "Electric","Gas") 
print(scp["Engine Size (L)"].value_counts())

print(scp.isna().sum())

print(scp[scp["Torque (lb-ft)"].isna()])

scp["Horsepower"] = scp["Horsepower"].str.replace("\+", "",regex=True).str.replace("\,", "",regex=True)

scp["Torque (lb-ft)"] = scp["Torque (lb-ft)"].str.replace('\-', lambda x: np.nan,regex=True).str.replace("\+","",regex=True).str.replace("\,", "",regex=True)
scp.loc[scp['Torque (lb-ft)'] == "0", 'Torque (lb-ft)'] = scp.loc[scp['Torque (lb-ft)'] == "0", 'Horsepower']
scp['Torque (lb-ft)'].fillna(scp['Horsepower'], inplace=True)
scp["Torque (lb-ft)"] = scp["Torque (lb-ft)"].astype(int)

scp["0-60 MPH Time (seconds)"] = scp["0-60 MPH Time (seconds)"].str.replace("\<","",regex=True).astype(float)

scp["Price (in USD)"] = scp["Price (in USD)"].str.replace(",","",regex=True).astype(int)

Engine_Size_map = {"Gas":0, "Electric":1}
Year = {2019:0, 2020:1, 2021:2, 2022:3, 2023:4}

scp["Engine Size (L)"] = scp["Engine Size (L)"].map(Engine_Size_map)
scp["Year"] = scp.Year.map(Year)

print(scp.isna().sum())

scp["Year"].fillna(1,inplace=True)

print(scp.isna().sum())

scp.to_csv('/home/kda/mlops_lab1/data/stage1/Sport car price.csv')
