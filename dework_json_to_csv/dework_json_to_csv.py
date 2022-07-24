import json
import pandas
import csv
import time
from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://rpc.gnosischain.com'))
web3.isConnected()

input_json = '/home/rxx/Documents/GitHub/tec-data-analysis/dework_json_to_csv/20220724_teacademy_team.json'
team = 'TE Academy T.E.A.M.'

output_csv = "/home/rxx/Documents/GitHub/tec-data-analysis/dework_json_to_csv/"+team.replace('.', '_').replace(' ', '_')+".csv"

df = pandas.read_json(open(input_json, "r", encoding="utf8"), orient='records')

json_dict = list(df["data"])[0]['tasks']

# extract each column in the nested dictionary
csv_list = []

for i in range(0, len(json_dict)):
    column_list = ['id', 'status', 'name', 'doneAt'] # status = completion_status removed description due to CRLF
    row = [team]

    # nice dict
    for j in column_list:
        row.append(json_dict[i][j])
    
    if (i == 0):
        column_list_header = ["team","id","status","name","doneAt","token","amount","username","payment_status","tx_hash","datetime"]
        csv_list.append(column_list_header) 
    
    if row[2] == 'DONE': # strip out in progress cards

        # rewards, nested json
        rewards_json = (json_dict[i]['rewards'])[0] # only 1 reward for now
        
        token = rewards_json['token']['symbol']
        amount = int(rewards_json['amount'])/2e18

        row.append(token); column_list.append('token')
        row.append(amount); column_list.append('amount')

        payments_json = rewards_json.get('payments', None) # only one user for now
        if payments_json != []:
            payments_json = payments_json[0]
            username = (payments_json['user']['username'])
            payments_status = payments_json['payment']['status']
            tx_hash = payments_json['payment']['data'].get('txHash','0xa85934717d0c4459ab2636951bb2f67b9522af6c71d0f318212077c40bbfde1a') 
            # this above is a random early LYXe tx hash. its over one year before tec, so easy to clean later on, rather than error handling in web3py

            row.append(username); column_list.append('username')
            row.append(payments_status); column_list.append('payment_status')
            row.append(tx_hash); column_list.append('tx_hash')

            # append datetime from hash
            block = web3.eth.get_transaction(tx_hash)
            block_seconds = (web3.eth.get_block(block['blockNumber'])['timestamp'])
            block_datetime = time.strftime('%Y-%m-%d', time.localtime(block_seconds))

            if (block_datetime=='2021-04-23'): 
                block_datetime='processing'
            row.append(block_datetime); column_list.append('datetime')

            # add all to csv
            csv_list.append(row)
     

# write to a csv
with open(output_csv, "w+") as f:
    writer = csv.writer(f)
    writer.writerows(csv_list)

