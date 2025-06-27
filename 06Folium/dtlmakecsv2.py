import requests
import xmltodict
import json
import csv
import time

url = 'http://api.nongsaro.go.kr/service/garden/gardenDtl'
api_key = '20250626K8HCI4KNPYS4XFEDFUBXVA'

with open('plant_ids.txt', 'r') as f:
    plant_ids = [line.strip() for line in f.readlines() if line.strip()]

# 저장할 필드 리스트 (header)
fields = [
    'cntntsNo', 'plntbneNm', 'plntzrNm', 'distbNm', 'fmlNm', 'fmlCodeNm', 'orgplceInfo',
    'adviseInfo', 'imageEvlLinkCours', 'growthHgInfo', 'growthAraInfo', 'lefStleInfo',
    'smellCode', 'smellCodeNm', 'toxctyInfo', 'prpgtEraInfo', 'etcEraInfo', 'managelevelCode',
    'managelevelCodeNm', 'grwtveCode', 'grwtveCodeNm', 'grwhTpCode', 'grwhTpCodeNm','winterLwetTpCode',
    'winterLwetTpCodeNm', 'hdCode', 'hdCodeNm', 'frtlzrInfo', 'soilInfo', 'watercycleSprngCode',
    'watercycleSprngCodeNm', 'watercycleSummerCode', 'watercycleSummerCodeNm', 'watercycleAutumnCode',
    'watercycleAutumnCodeNm', 'watercycleWinterCode', 'watercycleWinterCodeNm', 'dlthtsManageInfo',
    'speclmanageInfo', 'fncltyInfo', 'flpodmtBigInfo', 'flpodmtMddlInfo', 'flpodmtSmallInfo',
    'WIDTH_BIG_INFO', 'widthMddlInfo', 'widthSmallInfo', 'vrticlBigInfo', 'vrticlMddlInfo', 'vrticlSmallInfo',
    'hgBigInfo','hgMddlInfo','hgSmallInfo','volmeBigInfo','volmeMddlInfo','volmeSmallInfo','pcBigInfo',
    'pcMddlInfo','pcSmallInfo','managedemanddoCode','managedemanddoCodeNm','clCode','clCodeNm','grwhstleCode',
    'grwhstleCodeNm','indoorpsncpacompositionCode','indoorpsncpacompositionCodeNm','eclgyCode','eclgyCodeNm',
    'lefmrkCode', 'lefmrkCodeNm','lefcolrCode','lefcolrCodeNm','ignSeasonCode','ignSeasonCodeNm','flclrCode',
    'flclrCodeNm', 'fmldeSeasonCode','fmldeSeasonCodeNm','fmldecolrCode','fmldecolrCodeNm', 'prpgtmthCode',
    'prpgtmthCodeNm','lighttdemanddoCode','lighttdemanddoCodeNm','postngplaceCode','postngplaceCodeNm',
    'dlthtsCode','dlthtsCodeNm'
]

with open('plants.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    for cntntsNo in plant_ids:
        params = {'apiKey': api_key, 'cntntsNo': cntntsNo}
        response = requests.get(url, params=params)
        data_dict = xmltodict.parse(response.content)
        data_json = json.loads(json.dumps(data_dict, ensure_ascii=False))
        body = data_json.get('response', {}).get('body', {})
        item = body.get('item', {})

        # CSV에 저장할 딕셔너리 생성 (fields 기준으로)
        row = {field: item.get(field, '') for field in fields}

        writer.writerow(row)
        print(f"저장 완료: {cntntsNo} - {row.get('plntbneNm', '')}")

        time.sleep(0.3)  # API 과도 요청 방지
