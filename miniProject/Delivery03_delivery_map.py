import folium
import time
import requests,json
from openpyxl.chart.marker import Marker

url='https://openapi.gg.go.kr/GGEXPSDLV'
page=1
user_sigun = input('시군명을 입력하세요(ex: 수원시):')
delivery_apps = folium.Map(location=[37.5502, 126.982])

while True:
    params = dict(
        Type='json',
        pSize='1000',
        pIndex=page,
        KEY='d8060de8bc004ff1953902908cc425d9'
    )

    raw_data = requests.get(url=url, params=params)
    binary_data = raw_data.content
    json_data = json.loads(binary_data)
    try:
        for jd in json_data['GGEXPSDLV'][1]['row'] :
            SIGUN_NM = jd['SIGUN_NM']
            STR_NM = jd['STR_NM']
            BIZREGNO = jd['BIZREGNO']
            INDUTYPE_NM = jd['INDUTYPE_NM']
            REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR']
            REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']
            REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT']
            if SIGUN_NM==user_sigun:
                folium.Marker([REFINE_WGS84_LAT, REFINE_WGS84_LOGT], popup=STR_NM).add_to(delivery_apps)
                print(SIGUN_NM, STR_NM, BIZREGNO, INDUTYPE_NM, REFINE_LOTNO_ADDR, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)
        page += 1
        time.sleep(0.5)
    except (KeyError, IndexError):
        print(f'{page} 에서 더이상 데이터가 없음')
        break
delivery_apps.save('../saveFiles/delivery_map_'+user_sigun+'.html')