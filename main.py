import qrcode
import cv2
import numpy as np
import random

pouch = cv2.imread("d:\\barcode\\Input.png", cv2.IMREAD_GRAYSCALE)

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#data = "Python QR 코드를 생성하는 qrcode 라이브러리 알아보기오늘은 Python으로 QR 코드를 생성하는 라이브러리인 qrcode를 사용해보려 합니다."


for i in range(0, 10):
    data = ""
    for j in range(0, 100):
        data = data + random.choice(ascii_letters)

    fileName = f"d:\\barcode\\qr{i}.jpg"
    img = qrcode.make(data)
    # img.save(fileName)

    # PIL to Cv2 image
    qr_barcode_image = np.asarray(img.convert('L'))
    # qr_barcode_image = np.asarray(img)[:,:,::-1].copy()

    # PIL to Cv2 image
    # qr_barcode_image = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2GRAY)
    # qr_barcode_image = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

    # resize barcode
    resize_barcode = cv2.resize(qr_barcode_image, (150, 150), interpolation=cv2.INTER_CUBIC)

    # rotate 270
    resize_barcode90 = cv2.transpose(resize_barcode)
    resize_barcode90 = cv2.flip(resize_barcode, 1)

    # copy to pouch image
    height, width = resize_barcode90.shape
    pos_x, pos_y = 150, 400
    pouch[pos_y:pos_y+height, pos_x:pos_x+width] = resize_barcode90

    pouchFileName = f"d:\\barcode\\output{i}.jpg"
    cv2.imwrite(pouchFileName, pouch)

