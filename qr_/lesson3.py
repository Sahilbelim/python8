import qrcode
from qrcode.image.styledpil import StyledPilImage
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("https://github.com/Sahilbelim/python8/blob/main/qr_/lesson2.py")
qr.make(fit=True)

# img=qr.make_image(fill_color="#190482", back_color="#C2D9FF")

img = qr.make_image(image_factory=StyledPilImage, embeded_image_path="./py8_logo1.png")

type(img)

img.save("color_qr3.png")