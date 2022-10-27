from turtle import back
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, 
box_size=15, border=2)

qr.add_data("https://www.wscubetech.com/")
qr.make(fit=True)

img = qr.make_image(fill_color = "black", back_color = "cyan")

img.save("WS CUBE website.png")