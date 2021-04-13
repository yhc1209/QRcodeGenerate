import qrcode

def generateQR(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    with open(filename+'.png', 'wb') as f:
        img.save(f)

if __name__ == "__main__":
    for x in range(10):
        for y in range(10):
            name = f'x{x:0>4}y{y:0>4}'
            generateQR(name, name)