import json
import pandas
import csv
import time
from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://rpc.gnosischain.com'))
web3.isConnected()

input_json = '20220724_twitter_team.json'
team = 'Twitter T.E.A.M.'

output_csv = team.replace('.', '_') + '.csv'

df = pandas.read_json(input_json, orient='records')
json_dict = list(df["data"])[0]['tasks']

# extract each column in the nested dictionary
csv_list = []

for i in range(0, len(json_dict)):
    column_list = ['id', 'status', 'name', 'doneAt'] # status = completion_status removed description due to CRLF
    row = [team]

    # nice dict
    for j in column_list:
        row.append(json_dict[i][j])

    # rewards, nested json
    rewards_json = (json_dict[i]['rewards'])[0] # only 1 reward for now
    
    token = rewards_json['token']['symbol']
    amount = int(rewards_json['amount'])/2e18

    row.append(token); column_list.append('token')
    row.append(amount); column_list.append('amount')

    payments_json = rewards_json['payments'][0] # only one user for now

    username = (payments_json['user']['username'])
    payments_status = payments_json['payment']['status']
    tx_hash = payments_json['payment']['data'].get('txHash','0xa85934717d0c4459ab2636951bb2f67b9522af6c71d0f318212077c40bbfde1a')

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
    if (i == 0):
        column_list.insert(0, 'team')
        csv_list.append(column_list) 
    csv_list.append(row)
     

# write to a csv
with open(output_csv, "w+") as f:
    writer = csv.writer(f)
    writer.writerows(csv_list)

