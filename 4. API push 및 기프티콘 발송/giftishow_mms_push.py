from urllib import response
import requests, json
from datetime import timedelta, datetime
import os, pymysql, warnings, jwt, asyncio
import pandas as pd
import numpy as np
from datetime import datetime

############################################## SETTING ##############################################

################################################ API ################################################

now = datetime.now()
now_time = str(now.hour)+str(now.minute)
now_day = str(now.year)+str(now.month)+str(now.day)


api_code = '0204'   # API코드
custom_auth_code = 'REALe175d367815b4d6a8bd160191e8c45f6' # API 인증 키 
custom_auth_token = 'h0kjZn5SyztxvrbGflhmXg==' # API 인증 토큰
dev_yn = 'N' # 테스트여부 설정 값 - yes or no # 운영(N)으로만 설정해서 테스트 해야 합니다.
goods_code = 'G00000750744' # 상품코드
mms_msg = 'test' # MMS 메시지
mms_title = 'title_te' # MMS제목 - mms_title 은 10자가 넘으면 안됩니다.
callbank_no = '15662231' # '-'를 제외한 발신번호 
phone_no = ['01048027350','01077742140'] # '-'를 제외한 수신번호

# tr_id = f'service_20221026_{now_time}' # 거래아이디 (Unique한 ID) 고객사와 기프티쇼비즈간 대사값 (사용자생성 TR_ID)
                                    # TR_ID는 고유값이어야 합니다.
                                    # (필수사항) 자리수 : 25자 이하입니다.
                                    # (권고사항) service_20190814_12345678 형식으로 생성 부탁드립니다.
                                    # 응답결과를 받지 못하는 경우(타임아웃 15초), 동일 TR_ID로 ‘쿠폰취소요청’을 보내주셔야 합니다. 
                                    # 사유는 기프티쇼 비즈 플랫폼에서는 발행이 되어 있을 가능성이 높습니다. (*비즈머니 차감)
                                    # 서비스가 보유한 리워드포인트의 교환 시, 리워드포인트의 차감성공 후 발송요청을 보내주셔야 합니다.
user_id = 'admin@finset.io' # 회원 ID - 고객의 unique id인지, 계정 id인지 
gubun = 'N' # MMS발송 구분자 - Y: 핀번호수신 - N: MMS - I: 바코드이미지수신
# 옵션 파라미터
order_no = '' # 주문번호
rev_info_yn = '' # 예약발송여부 (Y:예약, N:실시간)
rev_info_date = '' # 예약일자 (yyyyMMdd)
rev_info_time = '' # 예약시간 (HHmm)
template_id = '' # 카드 아이디
banner_id = '202006010058067' # 배너 아이디

URL = 'https://bizapi.giftishow.com/bizApi/send'

tr_id = 'service_'+now_day+'_'+now_time

input_data = {
  "api_code": f'{api_code}',
  "custom_auth_code": f'{custom_auth_code}',
  "custom_auth_token": f'{custom_auth_token}',
  "dev_yn": f'{dev_yn}',
  "goods_code": f'{goods_code}',
  "mms_msg": f'{mms_msg}',
  "mms_title": f'{mms_title}',
  "callback_no": f'{callbank_no}',
  "phone_no": phone_no,
  "tr_id": f'{tr_id}',
  "user_id": f'{user_id}',
  "gubun": f'{gubun}'
}
response = requests.post(URL, data=input_data)
print('발송할 고객 전화번호 - ', phone_no)
print('')
print("response: ", response)
print("response.text: ", response.text)

print(tr_id)

# tr_id_lst = []
# for i in range(len(phone_no)):
#   tr_id = 'service_20221026_'+now_time+str(i)

#   input_data = {
#     "api_code": f'{api_code}',
#     "custom_auth_code": f'{custom_auth_code}',
#     "custom_auth_token": f'{custom_auth_token}',
#     "dev_yn": f'{dev_yn}',
#     "goods_code": f'{goods_code}',
#     "mms_msg": f'{mms_msg}',
#     "mms_title": f'{mms_title}',
#     "callback_no": f'{callbank_no}',
#     "phone_no": phone_no[i],
#     "tr_id": f'{tr_id}',
#     "user_id": f'{user_id}',
#     "gubun": f'{gubun}'
#   }
#   response = requests.post(URL, data=input_data)
#   print('발송할 고객 전화번호 - ', phone_no)
#   print('')
#   print("response: ", response)
#   print("response.text: ", response.text)
#   tr_id_lst.append(tr_id)

# print(tr_id_lst)
# 쿠폰이미지와 PIN값은 API를 통해 받아야한다.
# headers = {'Content-Type': 'application/x-www-form-urlencoded'} - 저 값은 자동으로 설정 가능하다고 한다. 

# json.dumps(input_data) - dump를 안하고 진행하였더니 성공!


