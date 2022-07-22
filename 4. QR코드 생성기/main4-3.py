import qrcode

file_path = r'/Users/jihoonkim/Desktop/python_40functions/4. QR코드 생성기/qr코드모임.txt'
with open(file_path, 'rt', encoding='UTF8') as f :
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = '4. QR코드 생성기\\' + qr_data + '.png'
        qr_img.save(save_path)