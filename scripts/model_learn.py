import sys
import os
import yaml
import pickle

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

dir_path = "data/models"
os.makedirs(dir_path,exist_ok=True)
params = yaml.safe_load(open("params.yaml"))["train"]
p_seed = params["seed"]
p_max_depth = params["max_depth"]

scp = pd.read_csv("data/stage4/train.csv")
scp.info()

X = scp.drop(columns=["Price (in USD)"])
y = scp["Price (in USD)"]

clf = DecisionTreeClassifier(max_depth=p_max_depth, random_state=p_seed)
clf.fit(X,y)

model = "model.pkl"
full_model_path = os.path.join(dir_path,model)
with open(full_model_path,"wb") as fd:
    pickle.dump(clf,fd)
