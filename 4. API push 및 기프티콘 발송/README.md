# 📱 API push 및 기프티콘 발송

고객 알림 및 기프티콘 발송을 위한 API 모듈입니다.

## 📋 주요 기능

### 1. 푸시 알림
- 실시간 알림 발송
- 맞춤형 메시지 생성
- 알림 설정 관리
- 발송 이력 추적

### 2. 기프티콘 발송
- 기프티콘 생성
- 발송 자동화
- 발송 상태 관리
- 재발송 처리

### 3. API 연동
- 외부 API 연동
- 웹훅 처리
- 인증 관리
- 에러 처리

## 🛠️ 사용 기술
- Python
- REST API
- HTML
- CSS

## 📊 시스템 구조
- 알림 시스템
  - 푸시 알림
  - 이메일 알림
  - SMS 알림
- 기프티콘 시스템
  - 기프티콘 생성
  - 발송 관리
  - 사용 내역

## 💻 코드 구조
```
notification/
├── api/
│   ├── push.py
│   └── gift.py
├── services/
│   ├── notification.py
│   └── giftcard.py
├── tasks/
│   ├── push_task.py
│   └── gift_task.py
└── utils/
    ├── message.py
    └── validator.py
```
