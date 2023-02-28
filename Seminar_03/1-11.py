import os
import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=owNJ5PYj7s4")

img.save("qr.png","PNG")
os.system("qr.png")
