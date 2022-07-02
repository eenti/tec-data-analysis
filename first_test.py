# packages
from duneanalytics import *
import pandas as pd
import json

# your user and password. doing this so i can gitignore my user/pwd and so keep the repo public 
from dune_user_password import dune_username, dune_password

# fetch query results from dune as a json
dune = DuneAnalytics(dune_username, dune_password)
dune.login()
dune.fetch_auth_token()
result_id = dune.query_result_id(query_id=991461)
data = dune.query_result(result_id)

df = pd.DataFrame.from_dict(data)
print(df["data"])

#with open('data.json', 'w+') as f:
#    json.dump(data, f)