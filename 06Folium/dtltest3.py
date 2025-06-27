import requests
import xmltodict
import json
import csv
import time

# API 기본 설정
url = 'http://api.nongsaro.go.kr/service/garden/gardenDtl'
api_key = '20250626K8HCI4KNPYS4XFEDFUBXVA'

with open('plant_ids.txt', 'r') as f:
    plant_ids = [line.strip() for line in f.readlines() if line.strip()]

# 예시: 식물 ID 리스트
# plant_ids = ['12971', '12937', '12932', '12956', '12920', '12919', '12901']

# 각 식물 상세 정보 조회
for cntntsNo in plant_ids:
    params = {
        'apiKey': api_key,
        'cntntsNo': cntntsNo
    }

    response = requests.get(url, params=params)
    data_dict = xmltodict.parse(response.content)
    data_json = json.loads(json.dumps(data_dict, ensure_ascii=False))
    body = data_json.get('response', {}).get('body', {})

    # 전체 항목을 key-value 형식으로 출력
    print(f"✅ 전체 응답 데이터 (cntntsNo={cntntsNo})")
    for key, value in body.items():
        print(f"{key}: {value}")# 전체 항목을 key-value 형식으로 출력