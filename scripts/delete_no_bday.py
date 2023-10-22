import pandas as pd
import sys
import os
import io

os.makedirs('data/stage1', exist_ok=True)
adv_stats = pd.read_csv('/home/kda/mlops_lab1/data/raw/Advanced.csv')


adv_stats = adv_stats.dropna(subset=['birth_year'])

adv_stats.to_csv('/home/kda/mlops_lab1/data/stage1/Advanced.csv')
