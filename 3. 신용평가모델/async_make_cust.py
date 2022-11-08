## DB연결 이후 고객 리스트를 뽑고 여러 자산 연결 수를 파악하는 프로시저를 실행하는 코드 

import pandas as pd
import time
import asyncio
import aiomysql
from aiomysql.sa import create_engine
import paramiko
from sshtunnel import SSHTunnelForwarder
import pymysql


class AsyncIterator:
    def __init__(self, seq):
        self.iter = iter(seq)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.iter)
        except StopIteration:
            raise StopAsyncIteration

async def pani(df):
    with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=mypkey,
        remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = await aiomysql.connect(host='127.0.0.1', user=sql_username,
                password=sql_password, db=sql_main_database,
                port=tunnel.local_bind_port)

        async for i in AsyncIterator(df.index):
            async for j in AsyncIterator(df.iloc[:,:].columns):
                cur = await conn.cursor()
                await cur.execute(f"""SELECT {j}({i});""")
                r = await cur.fetchall()
                df.loc[i,j] = r[0][0]
                await cur.close()
            print(f'{i} is done')
        conn.close()

pkeyfilepath = '/Users/nagyeonghun/Desktop/ssh_key.pem' ######################### ssh_key.pem 파일 경로 입력
password = 'gitple5293'
mypkey = paramiko.RSAKey.from_private_key_file(pkeyfilepath, password=password)
sql_hostname = 'nlb-db-prd-11861507-d8b0b3f2c76e.kr-fin.lb.naverncp.com'
sql_username = 'rudgnsdl06'            ######################### sql_username 입력
sql_password = 'Z2st8puvos&39ipaSibu'            ######################### sql_password 입력
sql_main_database = 'betterday_db'
sql_main_database = 'betterday_db'
sql_port = 3306
ssh_host = '10.0.1.14'
ssh_user = 'rudgnsdl06'                ######################### ssh_user 입력
ssh_port = 22

if __name__ == '__main__':

    with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=mypkey,
        remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        con = pymysql.connect(host='127.0.0.1', user=sql_username,
            passwd=sql_password, db=sql_main_database,
            port=tunnel.local_bind_port)
        sql = f"""SELECT ID FROM BDAY_CUST ORDER BY ID ;"""
        temp = pd.read_sql(sql, con)
    print('select all id in db')

    all_cust = temp['ID'].to_list()

    df_col = ['ID', 'ISCONSENT_BANK_1', 'ISCONSENT_CARD_1', 'ISCONSENT_INV_1', 'ISCONSENT_INS_1']
    cust_df = pd.DataFrame(columns= df_col)
    cust_df['ID'] = all_cust
    cust_df=cust_df.set_index('ID')

    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(pani(cust_df))
    cust_df.to_csv('is_cons_v7.csv')

    cust_list = cust_df[((cust_df>=1).sum(axis=1)>=2)].index
    print('num of cust:', len(cust_list))
    df_col = ['ID']
    for i in range(1, 8):
        df_col.append(f'CSS_IRP_{i}')
    for i in range(8,139):
        df_col.append(f'CSS_BANK_{i}')
    for i in range(1, 67):
        df_col.append(f'CSS_CARD_{i}')
    for i in range(104, 112):
        df_col.append(f'CSS_CARD_{i}')
    for i in range(1, 46):
        df_col.append(f'CSS_INV_{i}')
    for i in range(1, 34):
        df_col.append(f'CSS_INS_{i}')

    final_df = pd.DataFrame(columns= df_col)
    final_df['ID'] = cust_list
    final_df=final_df.set_index('ID')
    final_df.to_csv('cust_list_v7.csv')
    print(time.time()-start)
    print(final_df)
