from ppadb.client import Client
import time

def adb_connect():
    client = Client(host="127.0.0.1", port=5037)
    find_devices = client.devices()

    if len(find_devices) == 0:
        print('No devices')
        quit()

    return device, client

device, client = adb_connect()
time.sleep(3.0)

#스마트폰 자동화_ 스마트폰의 웹 브라우저를 여는 명령어로 웹페이지를 여는 기능