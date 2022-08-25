from ppadb.client import Client

client = Client(host="127.0.0.1", post=5037)
find_devices = client.devices()

if len(find_devices) == 0:
    print('No devices')
    quit()

device = find_devices[0]
print(f'찾은 디바이스 : {device}')

#스마트폰 자동화