#QR Code with image

import qrcode
from PIL import Image

data = 'https://pbs.twimg.com/media/DimbC7oXkAA0TYp.jpg'
qr=qrcode.QRCode(version=1,
                 box_size=10,
                 border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="purple", back_color="white")
img.save('MyQRCode3.jpg') #change that qrcode to an image
img = Image.open('MyQRCode3.jpg')
img.show()