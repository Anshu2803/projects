#importing qrcode module
import qrcode
#qr code functions for adjusting the size of qr code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.linkedin.com/in/anshul-agrawal-a25061228')
qr.make(fit=True)

#make function for the qr code color 
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_linkdin.png")