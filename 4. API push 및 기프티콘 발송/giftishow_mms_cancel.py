from urllib import response
import requests, json
from datetime import timedelta, datetime
import os, pymysql, warnings, jwt, asyncio
import pandas as pd
import numpy as np

############################################## SETTING ##############################################

################################################ API ################################################

api_code = '0202'   # API코드
custom_auth_code = 'REALe175d367815b4d6a8bd160191e8c45f6' # API 인증 키 
custom_auth_token = 'h0kjZn5SyztxvrbGflhmXg==' # API 인증 토큰
dev_yn = 'N' # 테스트여부 설정 값 - yes or no # 운영(N)으로만 설정해서 테스트 해야 합니다.
tr_id = 'service_2022111_15431' # 거래아이디 (Unique한 ID) 고객사와 기프티쇼비즈간 대사값 (사용자생성 TR_ID)
                                    # TR_ID는 고유값이어야 합니다.
                                    # (필수사항) 자리수 : 25자 이하입니다.
                                    # (권고사항) service_20190814_12345678 형식으로 생성 부탁드립니다.
                                    # 응답결과를 받지 못하는 경우(타임아웃 15초), 동일 TR_ID로 ‘쿠폰취소요청’을 보내주셔야 합니다. 
                                    # 사유는 기프티쇼 비즈 플랫폼에서는 발행이 되어 있을 가능성이 높습니다. (*비즈머니 차감)
                                    # 서비스가 보유한 리워드포인트의 교환 시, 리워드포인트의 차감성공 후 발송요청을 보내주셔야 합니다.
user_id = 'admin@finset.io' # 회원 ID - 고객의 unique id인지, 계정 id인지 

URL = 'https://bizapi.giftishow.com/bizApi/cancel'

input_data = {
  "api_code": f'{api_code}',
  "custom_auth_code": f'{custom_auth_code}',
  "custom_auth_token": f'{custom_auth_token}',
  "dev_yn": f'{dev_yn}',
  "tr_id": f'{tr_id}',
  "user_id": f'{user_id}',
}

response = requests.post(URL, data=input_data)

print("response: ", response)
print("response.text: ", response.text)