import pandas as pd
import sys
import os
import io

os.makedirs('data/stage2', exist_ok=True)

scp = pd.read_csv("/home/kda/mlops_lab1/data/stage1/Sport car price.csv")
Car_Make = pd.get_dummies(scp["Car Make"], drop_first=True)
scp = scp.drop("Car Make", axis = 1)
scp = pd.concat([scp, Car_Make], axis = 1)

scp.to_csv('/home/kda/mlops_lab1/data/stage2/Sport car price.csv')
