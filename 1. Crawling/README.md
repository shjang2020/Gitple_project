# 🔍 Crawling

증권사 API를 활용한 데이터 수집 및 처리 모듈입니다.

## 📋 주요 기능

### 1. 증권사 API 연동
- 한국투자증권 API 연동
- 실시간 시장 데이터 수집
- REST API 구현
- WebSocket 실시간 데이터 처리

### 2. 실시간 시장 데이터 수집
- 주가 데이터 수집
- 거래량 데이터 수집
- 호가 데이터 수집
- 실시간 시장 지표 수집

### 3. 기업 재무정보 수집
- 재무제표 데이터 수집
- 기업 실적 데이터 수집
- 시장 데이터 정규화
- 데이터 저장 및 관리

## 🛠️ 사용 기술
- Python
- Requests
- WebSocket
- Pandas
- SQLAlchemy
- REST API

## 📊 데이터 구조
- 시장 데이터
  - 주가 정보
  - 거래량 정보
  - 호가 정보
- 기업 데이터
  - 재무제표
  - 실적 정보
  - 시장 지표

## 💻 코드 구조
```
crawling/
├── api/
│   ├── korea_investment.py
│   └── websocket_client.py
├── data/
│   ├── market_data.py
│   └── company_data.py
├── utils/
│   ├── data_processor.py
│   └── db_manager.py
└── config/
    └── settings.py
```
