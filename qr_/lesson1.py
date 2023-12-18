import qrcode

img=qrcode.make("https://pypi.org/project/qrcode/")

type(img)
img.save("qr4.png")