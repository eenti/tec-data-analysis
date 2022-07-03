# packages
import os
from dotenv import load_dotenv
from duneanalytics import *
import json

load_dotenv()

dune_user = os.environ.get("DUNE_USER") or 5000
dune_pwd = os.environ.get("DUNE_PWD") or 5000

# fetch query results from dune as a json
dune = DuneAnalytics(dune_user, dune_pwd)
dune.login()
dune.fetch_auth_token()
result_id = dune.query_result_id(query_id=991461)
data = dune.query_result(result_id)

# conversion of this result into csv