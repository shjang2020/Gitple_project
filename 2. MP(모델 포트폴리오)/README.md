# 📊 MP(모델 포트폴리오)

투자 포트폴리오 최적화 및 리밸런싱 전략을 구현한 모듈입니다.

## 📋 주요 기능

### 1. 포트폴리오 최적화
- Modern Portfolio Theory 적용
- 효율적 프론티어 계산
- 리스크-수익률 최적화
- 제약조건 설정

### 2. 리밸런싱 전략
- 정기 리밸런싱
- 임계값 기반 리밸런싱
- 비용 최적화
- 거래 시뮬레이션

### 3. 위험 관리 모델
- VaR(Value at Risk) 계산
- 변동성 예측
- 상관관계 분석
- 스트레스 테스트

## 🛠️ 사용 기술
- Python
- NumPy
- Pandas
- Scipy
- CVXOPT
- Matplotlib

## 📊 모델 구조
- 포트폴리오 최적화
  - 평균-분산 최적화
  - 블랙-리터만 모델
  - 리스크 패리티
- 리밸런싱 전략
  - 정적 리밸런싱
  - 동적 리밸런싱
  - 비용 고려 리밸런싱
- 위험 관리
  - VaR 모델
  - 변동성 모델
  - 상관관계 모델

## 💻 코드 구조
```
portfolio/
├── optimization/
│   ├── mpt.py
│   └── black_litterman.py
├── rebalancing/
│   ├── strategy.py
│   └── simulation.py
├── risk/
│   ├── var.py
│   └── volatility.py
└── utils/
    ├── data_processor.py
    └── visualization.py
```
