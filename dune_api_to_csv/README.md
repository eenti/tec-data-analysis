# extract a csv given a Dune Analytics Query

Made this project alongside @anak.
Goal is to extract dune queries for our multisig wallets given dune queries -> .csv for further analysis; though this code should be extendable to anybody wanting to download data from dune without access to their API.

## requirements
python3 
python-dotenv
os
duneanalytics
pandas

download them with the requirements file, or manually

## how to use
* download a copy of this repository,
* add a .env file to this folder with two variables:
  * DUNE_USER="your_dune_username"
  * DUNE_PWD="your_dune_password
* edit the two variables to your needs:
  * output_file (your csv location. Uses relative path given this folder)
  * your_query_id (taken as the webpage ID from Dune's query editor)
* run! you'll get your csv soon

that's all! :)