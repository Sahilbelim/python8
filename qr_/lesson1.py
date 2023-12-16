import qrcode

img=qrcode.make("https://www.google.com/")

type(img)
img.save("qr2.png")