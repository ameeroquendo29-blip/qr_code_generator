import qrcode

url = input("Enter the URL here: ").strip()
file_path = "C:\\Users\\Ameer\\Downloads\\PUP\\Python\\qr_code_generator_ni_pogi\\qr_code_generator.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated")