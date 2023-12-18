import qrcode
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("Add Data heare ...")
qr.make(fit=True)

img=qr.make_image(fill_color="#265073", back_color="#ECF4D6")

type(img)

img.save("color_qr1.png")