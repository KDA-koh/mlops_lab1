import yaml
import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split

os.makedirs('data/stage4', exist_ok=True)
params = yaml.safe_load(open("params.yaml"))["split"]

p_split_ratio = params["split_ratio"]

scp = pd.read_csv("/home/kda/mlops_lab1/data/stage3/Sport car price.csv")

X = scp.drop(columns=["Price (in USD)", "Torque (lb-ft)"])
y = scp["Price (in USD)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = p_split_ratio, random_state=1)

pd.concat([y_train,X_train],axis=1).to_csv("data/stage4/train.csv",header=None,index=None)
pd.concat([y_test,X_test],axis=1).to_csv("data/stage4/test.csv",header=None,index=None)
