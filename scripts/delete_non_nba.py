import pandas as pd
import sys
import os
import io

os.makedirs('data/stage2', exist_ok=True)

adv_stats = pd.read_csv('/home/kda/mlops_lab1/data/stage1/Advanced.csv')

adv_stats = adv_stats[adv_stats['lg'] == 'NBA']

adv_stats.to_csv('/home/kda/mlops_lab1/data/stage2/Advanced.csv')
