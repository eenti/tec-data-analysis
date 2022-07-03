# packages
from dotenv import load_dotenv
import os
from duneanalytics import *
import pandas as pd

load_dotenv() # bring forth the environment vars

# params
output_file = "data-7-2-2022.csv"
your_query_id = 991461

dune_user = os.environ.get("DUNE_USER") or 5000
dune_pwd = os.environ.get("DUNE_PWD") or 5000

# fetch query results from dune as a dict of jsons
dune = DuneAnalytics(dune_user, dune_pwd)
dune.login()
dune.fetch_auth_token()
result_id = dune.query_result_id(query_id=your_query_id)
data = dune.query_result(result_id)

# conversion of this dict into standard csv for import in gSheets
x = pd.DataFrame.from_dict(data)

keys = pd.DataFrame(x["data"]["get_result_by_result_id"])["data"][0].keys()

y = dict()

for i in pd.DataFrame(x["data"]["get_result_by_result_id"])["data"]:
    for k in keys:
         y.setdefault(k,[]).append(i[k])

pd.DataFrame(y).to_csv(output_file, index=False)
