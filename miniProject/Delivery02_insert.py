import requests, json
import cx_Oracle as cx
import time

host_name='localhost'
oracle_port=1521
service_name='xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

url='https://openapi.gg.go.kr/GGEXPSDLV'
page=1
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
            # print(SIGUN_NM, STR_NM, BIZREGNO, INDUTYPE_NM, REFINE_LOTNO_ADDR, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)

            sql = """insert into delivery_apps (idx, sigun, str_nm, bizregno, indutype_nm, addr, latitude, longitude)
                values (myboard_seq.nextval, :sigun, :str_nm, :bizregno, :indutype_nm, :addr, :latitude, :longitude)"""

            try:
                cursor.execute(sql, sigun=SIGUN_NM, str_nm=STR_NM, bizregno=BIZREGNO,
                               indutype_nm=INDUTYPE_NM, addr=REFINE_LOTNO_ADDR,
                               latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
                conn.commit()
                print('1개의 레코드 입력')
            except Exception as e:
                conn.rollback()
                print('insert 실행시 오류발생', e)
        page += 1
        time.sleep(0.5)
    except (KeyError, IndexError):
        print(f'{page} 에서 더이상 데이터가 없음')
        break
conn.close()