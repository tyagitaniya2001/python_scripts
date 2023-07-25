from logging import getLogger

from datetime import timedelta
from requests import HTTPError
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PrivateFormat
from cryptography.hazmat.primitives.serialization import NoEncryption
import time
import datetime
import os
import logging


import snowflake.connector as sf

print("snowflake")

sf_object=sf.connect(user='TANIYATYAGI28',
                     password='Hexaview@2001',
                     account='hxasgtu-dy54546',
                     role='ACCOUNTADMIN',
                     warehouse='TEST_WH',
                     database='TEST_DB_3',
                     schema='SCHEMA_TEST')


sqlSnowflake = sf_object.cursor()

result=sqlSnowflake.execute("LIST @my_csv_stage PATTERN='.*Customer.*';")

print(result)
filelist=[]
for row in result:
    print(row)
    filename = row[0]
    filelist.append(filename.split('/', 1)[-1])
   
print(filelist)


#logging.basicConfig(
#        filename='/tmp/ingest.log',
 #       level=logging.DEBUG)
#logger = getLogger(__name__)

#PRIVATE_KEY_PASSPHRASE='Hexaview@2001'

with open("C:/Users/taniya.tyagi/rsa_key.p8", 'rb') as pem_in:
  pemlines = pem_in.read()
  private_key_obj = load_pem_private_key(pemlines,
  password='Hexaview@2001'.encode(), backend=default_backend())

private_key_text = private_key_obj.private_bytes(
  Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()).decode('utf-8')
print("step 1")

from snowflake.ingest import SimpleIngestManager
from snowflake.ingest import StagedFile
from snowflake.ingest.utils.uris import DEFAULT_SCHEME

ingest_manager = SimpleIngestManager(account='hxasgtu-dy54546',
                                     host='hxasgtu-dy54546.snowflakecomputing.com',
                                     user='TANIYATYAGI28',
                                     pipe='test_db_3.schema_test.cust_pipe',
                                     private_key=private_key_text)

print("CONNECTED")

#file_list=['Customer_03.csv','Customer_04.csv','Customer_05.csv']



file_list=['*.csv']
staged_file_list = []
for file_name in filelist:
    staged_file_list.append(StagedFile(file_name, None))
    
print(staged_file_list)

try:
    resp = ingest_manager.ingest_files(staged_file_list)
except HTTPError as e:
    #logger.error(e)
    exit(1)

print("Section: Assert")
assert(resp['responseCode'] == 'SUCCESS')

while True:
    history_resp = ingest_manager.get_history()

    if len(history_resp['files']) > 0:
        print('Ingest Report:\n')
        print(history_resp)
        break
    else:
        # wait for 20 seconds
        time.sleep(20)

    hour = timedelta(hours=1)
    date = datetime.datetime.utcnow() - hour
    history_range_resp = ingest_manager.get_history_range(date.isoformat() + 'Z')
