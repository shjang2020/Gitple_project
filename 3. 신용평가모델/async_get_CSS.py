## DB연결 이후 고객 리스트를 뽑고 여러 자산 연결 수를 파악하는 프로시저를 실행하는 코드

import pandas as pd
import time
import asyncio
import aiomysql
from aiomysql.sa import create_engine
import paramiko
from sshtunnel import SSHTunnelForwarder


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
                #print(f"""SELECT {j}({i});""")
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
    final_df = pd.read_csv('cust_list_v7.csv', index_col=0)

    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(pani(final_df))

    final_df.to_csv('1102_pani_v7.csv')
    print(time.time()-start)
    print(final_df)
