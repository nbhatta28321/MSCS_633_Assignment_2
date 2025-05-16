

import qrcode

def generate_qr(url):
    """
    Generates a QR code from the given URL and saves it as an image.
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        filename = "biox_qr_code.png"
        img.save(filename)
        print(f"QR Code successfully generated and saved as '{filename}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_url = input("Enter the URL to generate QR Code: ")
    generate_qr(input_url)
