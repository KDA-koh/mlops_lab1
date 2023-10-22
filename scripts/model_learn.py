import sys
import os
import yaml
import pickle

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


os.makedirs("data/models",exist_ok=True)
params = yaml.safe_load(open("params.yaml"))["train"]
p_seed = params["seed"]
p_max_depth = params["max_depth"]

scp = pd.read_csv("data/stage4/train.csv")
X = scp.drop(columns=["Price (in USD)", "Torque (lb-ft)"])
y = scp["Price (in USD)"]

clf = DecisionTreeClassifier(max_depth=p_max_depth, random_state=p_seed)
clf.fit(X,y)

with open("data/models","wb") as fd:
    pickle.dump(clf,fd)