from flask import Flask, request, send_file
from flask_restful import Resource, Api
import qrcode
import cv2
import numpy as np
import random


app = Flask(__name__)
api = Api(app)

class CreateUser(Resource):
    def post(self):
        return {'status': 'success'}

api.add_resource(CreateUser, '/user')

@app.route("/", methods=["POST"])
def home():
    #img = Image.open(request.files['file'])
    value = request.files['file']
    return value


def get_2d_barcodeT(barcode_string):
    pouch = cv2.imread("Input.png", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("./"+barcode_string, pouch)
    return barcode_string

def get_2d_barcode(barcode_string):
    pouch = cv2.imread("Input.png", cv2.IMREAD_GRAYSCALE)

    img = qrcode.make(barcode_string)

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
    pouch[pos_y:pos_y + height, pos_x:pos_x + width] = resize_barcode90

    outputFileName = "output.png"
    cv2.imwrite("./" + outputFileName, pouch)
    return outputFileName



@app.route('/get_image')
def get_image():
    barcode_string = request.args.get('text')
    barcode_image_filename = get_2d_barcode(barcode_string)
    print(barcode_string)

    return send_file(barcode_image_filename, mimetype='image/png')

# @app.route("/")

# def hello():
#    return "Hello from FastCGI via IIS!123"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


