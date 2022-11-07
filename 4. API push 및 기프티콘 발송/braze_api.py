from urllib import response
import requests, json
from datetime import timedelta, datetime
import os, pymysql, warnings, jwt, asyncio
import pandas as pd
import numpy as np

############################################## SETTING ##############################################

DB_ENV = {
    # DB_HOST: local DB, DB_HOST_READ_ONLY: read only DB
    'HOST': '127.0.0.1',
    'USER': 'mysql',
    'PASSWORD': 'password',
    'DB': 'betterday_db'
}

conn = pymysql.connect(        
        host = DB_ENV['HOST'],
        user = DB_ENV['USER'],
        password = DB_ENV['PASSWORD'],
        db = DB_ENV['DB'],
        charset = 'utf8'
        )

################## 연금 보험 가입자 ##################
sql_1 = '''
SELECT mut.BDAY_CUST_ID FROM MD_INSU_INSURANCES mii , MD_USER_TOKEN mut 
WHERE mii.INSU_TYPE = 09
AND mii.INSU_STATUS = 02
AND mii.IS_CONSENT =1
AND mii.TOKEN_ID = mut.ID
GROUP BY mut.BDAY_CUST_ID;
'''
################# 개인연금펀드 손실 발생자 ##################
sql_2 = '''
SELECT mut.BDAY_CUST_ID  FROM MD_INVEST_ACCOUNTS_PRODUCTS miap , MD_INVEST_ACCOUNTS mia , MD_USER_TOKEN mut 
WHERE miap.INVEST_ACCOUNTS_ID =  mia.ID 
AND mia.TOKEN_ID = mut.ID 
AND mia.IS_CONSENT=1
AND miap.PROD_TYPE IN (413, 414, 415)
AND miap.PURCHASE_AMT - miap.EVAL_AMT>0
GROUP BY mut.BDAY_CUST_ID;
'''

cur = conn.cursor()
cur.execute(sql_1)

user_id = cur.fetchall()
user_id = list(pd.DataFrame(user_id)[0])
print('id result: ',user_id)

cur.close()

################################################ API ################################################

api_key = '45501b94-0803-419e-9313-38be738b2110'
instance_url = 'rest.iad-05.braze.com'
# user_id = 2107
campaign_id = '3644bac3-4841-a34b-940a-69d40d6813a2'

URL = 'https://'+f'{instance_url}'+'/campaigns/trigger/send'
data = {
  "campaign_id": f'{campaign_id}',
  "recipients": [
    {
      "external_user_id": f'{user_id}',
      #"trigger_properties": f'{trigger_properties}',
      #"example_integer_property": 1
    }
  ]
}

headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '+f'{api_key}'}

response = requests.post(URL, data=json.dumps(data) ,headers=headers)

print("response: ", response)
print("response.text: ", response.text)


# push messege 설정