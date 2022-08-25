from ppadb.client   import Client
import time

def adb_connect():
    client = Client(host="127.0.0.1", port=5037)
    find_devices = client.devices()

    if len(find_devices) == 0:
        print('No devicess')
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스 : {device}')

    return device, client

device, client = adb_connect()

device.shell('input keyevent 64')
time.sleep(2.0)

xyPosition = "423 136"
device.shell(f'input tap {xyPosition}')
time.sleep(2.0)

url = "www.naver.com"
device.shell(f'input text {url}')
time.sleep(2.0)

device.shell('input keyevent 66')
time.sleep(2.0)

result = device.screencap()
with open(r"18. 스마트자동화\screen.png", "wb") as fp:
    fp.write(result)

#웹 브라우저 화면 캡처 후 저장하는 코드 만들기