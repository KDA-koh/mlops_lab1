import pandas as pd
import sys
import os
import io

os.makedirs('data/stage3', exist_ok=True)

scp = pd.read_csv("/home/kda/mlops_lab1/data/stage2/Sport car price.csv")
Car_Model = pd.get_dummies(scp["Car Model"], drop_first=True)
scp = scp.drop("Car Model", axis = 1)
scp = pd.concat([scp, Car_Model], axis = 1)

scp.to_csv('/home/kda/mlops_lab1/data/stage3/Sport car price.csv')
