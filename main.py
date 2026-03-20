import qrcode as qr
from PIL import Image

data = input("Enter Text or URL:").strip()
if data.startswith("http"):
    print("🌐 Detected: URL")
elif "@" in data:
    print("📧 Detected: Email")
else:
    print("📝 Detected: Text")
if not data:
    print("❌ Data cannot be empty!")
    exit()


name = input("Enter file name: ").strip()
if not name.endswith(".png"):
    name = name + ".png"


valid_colors = ["black", "white", "red", "blue", "green", "yellow"]

front = input("Enter QR color (e.g., black, red, blue): ").lower()
back = input("Enter background color (e.g., white, yellow): ").lower()

if front not in valid_colors or back not in valid_colors:
    print("⚠️ Invalid color! Using default (black & white)")
    front = "black"
    back = "white"

if front == back:
    print("⚠️ Same colors not allowed! Using default (black & white)")
    front = "black"
    back = "white"



qr_=qr.QRCode(version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4)
qr_.add_data(data)
qr_.make(fit=True)
img= qr_.make_image(fill_color=front,back_color=back)



use_logo = input("Do you want to add a logo? (y/n): ").lower()

if use_logo == "y":
    try:
        logo_path = input("Enter logo file path (e.g., logo.png): ").strip()
        logo = Image.open(logo_path)

        # Resize logo (IMPORTANT)
        logo_size = (img.size[0] // 4, img.size[1] // 4)
        logo = logo.resize(logo_size)

        # Calculate center position
        pos = ((img.size[0] - logo.size[0]) // 2,
               (img.size[1] - logo.size[1]) // 2)

        img.paste(logo, pos)

        print("✅ Logo added successfully!")

    except Exception as e:
        print("Error Found Check Your Input!!...")

#img.save(f"{name}.png")

import os
file_path = os.path.abspath(f"{name}.png")

img.save(file_path)

print("Saved at:", file_path)

os.startfile(file_path)

# if platform.system()=="Windows":
#     os.startfile(f"{name}.png")
# elif platform.system()=="Darwin":
#     os.system(f"open {name}.png")
# else:
#     os.system(f"xdg-open {name}.png")

print("QR code generated Succesfully!!")
