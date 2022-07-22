import qrcode
from io import open

file_path = r'/Users/jihoonkim/Desktop/python_40functions/4. QR코드 생성기/qr코드모임.txt'
with open(file_path, 'rt', encoding='UTF8') as f :
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

#여러 개의 QR코드를 한 번에 생성하는 코드 만들고 실행