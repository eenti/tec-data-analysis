#!/usr/bin/env python3

import pandas as pd
import os
from pathlib import Path

# config variable here
data_file = "data.json" # put data file you want here
output_file = "data-7-2-2022.csv"

data_dir = os.getcwd()
output_dir = "output"

data_path = str(Path(data_dir)/data_file)

x = pd.read_json(data_path)

keys = pd.DataFrame(x["data"]["get_result_by_result_id"])["data"][0].keys()
y = dict()

for i in  pd.DataFrame(x["data"]["get_result_by_result_id"])["data"]:
    for k in keys:
         y.setdefault(k,[]).append(i[k])

pd.DataFrame(y).to_csv(Path(output_dir)/output_file)
