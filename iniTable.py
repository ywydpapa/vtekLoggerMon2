from influxdb import InfluxDBClient

host = 'localhost'  # InfluxDB 호스트 주소
port = 8086         # InfluxDB 포트
database = 'logger'  # 사용할 데이터베이스 이름
username = 'root'  # InfluxDB 사용자 이름
password = 'root'  # InfluxDB 비밀번호

client = InfluxDBClient(host, port, username, password, database)

# 데이터 포인트 생성
measurement = 'inoutT'  # 측정값의 이름
tags = {'stamp': 'Initial'}  # 태그 (선택 사항)
fields = {'d001':'-','d002':'-','d003':'-','d004':'-','d005':'-','d006':'-','d007':'-','d008':'-','d009':'-','d010':'-',
'd011':'-','d012':'-','d013':'-','d014':'-','d015':'-','d016':'-','d017':'-','d018':'-','d019':'-','d020':'-',
'd021':'-','d022':'-','d023':'-','d024':'-','d025':'-','d026':'-','d027':'-','d028':'-','d029':'-','d030':'-',
'd031':'-','d032':'-','d033':'-','d034':'-','d035':'-','d036':'-','d037':'-','d038':'-','d039':'-','d040':'-',
'd041':'-','d042':'-','d043':'-','d044':'-','d045':'-','d046':'-','d047':'-','d048':'-','d049':'-','d050':'-',
'd051':'-','d052':'-','d053':'-','d054':'-','d055':'-','d056':'-','d057':'-','d058':'-','d059':'-','d060':'-',
'd061':'-','d062':'-','d063':'-','d064':'-','d065':'-','d066':'-','d067':'-','d068':'-','d069':'-','d070':'-',
'd071':'-','d072':'-','d073':'-','d074':'-','d075':'-','d076':'-','d077':'-','d078':'-','d079':'-','d080':'-',
'd081':'-','d082':'-','d083':'-','d084':'-','d085':'-','d086':'-','d087':'-','d088':'-','d089':'-','d090':'-',
'd091':'-','d092':'-','d093':'-','d094':'-','d095':'-','d096':'-','d097':'-','d098':'-','d099':'-','d100':'-',
'd101':'-','d102':'-','d103':'-','d104':'-','d105':'-','d106':'-','d107':'-','d108':'-','d109':'-','d110':'-',
'd111':'-','d112':'-','d113':'-','d114':'-','d115':'-','d116':'-','d117':'-','d118':'-','d119':'-','d120':'-',
'd121':'-','d122':'-','d123':'-','d124':'-','d125':'-','d126':'-','d127':'-','d128':'-','d129':'-','d130':'-'}  # 필드

data = [
    {
        'measurement': measurement,
        'tags': tags,
        'fields': fields
    }
]
client.write_points(data)
client.close()
