import qrcode
import pyshorteners
import tkinter as tk
from PIL import Image
from datetime import datetime

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
SquareModuleDrawer,
RoundedModuleDrawer,
CircleModuleDrawer,
)
from qrcode.image.styles.colormasks import RadialGradiantColorMask

print("=" * 60)
print("ADVANCED QR CODE GENERATOR")
print("=" * 60)

url = input("\nEnter URL: ").strip()

final_url = url

shorten = input("Shorten URL? (y/n): ").lower()

if shorten == "y":
  try:
     shortener = pyshorteners.Shortener()
     final_url = shortener.tinyurl.short(url)
     print("Short URL:", final_url)
  except:
     print("Shortening failed. Using original URL.")
     final_url = url
  else:
     final_url = url

print("\nChoose QR Design")
print("1. Square")
print("2. Rounded")
print("3. Circle")

choice = input("Enter choice (1-3): ").strip()

if choice == "1":
  drawer = SquareModuleDrawer()
elif choice == "2":
  drawer = RoundedModuleDrawer()
elif choice == "3":
  drawer = CircleModuleDrawer()
else:
  drawer = RoundedModuleDrawer()

fill_color = input(
"\nQR Color (black, blue, red, green etc): "
).strip() or "black"

back_color = input(
"Background Color: "
).strip() or "white"

qr = qrcode.QRCode(
version=None,
error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size=12,
border=4,
)

qr.add_data(final_url)
qr.make(fit=True)

img = qr.make_image(
image_factory=StyledPilImage,
module_drawer=drawer,
color_mask=RadialGradiantColorMask()
)

img = img.convert("RGBA")

logo_path = input(
"\nLogo path (press Enter to skip): "
).strip()

if logo_path:
  try:
     logo = Image.open(logo_path).convert("RGBA")

     qr_width, qr_height = img.size

     logo_size = qr_width // 6

     logo = logo.resize(
        (logo_size, logo_size),
        Image.LANCZOS
    )

     position = (
        (qr_width - logo_size) // 2,
        (qr_height - logo_size) // 2
    )

     img.paste(
        logo,
        position,
        mask=logo
    )

     print("Logo added successfully.")

  except Exception as e:
     print("Logo error:", e)

timestamp = datetime.now().strftime(
"%Y%m%d_%H%M%S"
)

filename = f"Premium_QR_{timestamp}.png"

img.save(filename)

print("\n" + "=" * 60)
print("QR GENERATED SUCCESSFULLY")
print("=" * 60)

print("Saved as:", filename)
print("Encoded URL:", final_url)

img.show()
