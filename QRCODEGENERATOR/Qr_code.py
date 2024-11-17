import qrcode as qr
img = qr.make("    ") # link can be inserted between "" for generation of qrcode
img.save("cha.png")