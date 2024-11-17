import qrcode
from PIL import Image  

# Initialize the QRCode object with settings
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add data to the QR code
qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white") 
img.save("QRCODE.png")
