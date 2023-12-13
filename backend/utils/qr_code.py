import qrcode
import os  

class QRCode:
    @staticmethod
    def create(text: str):
        """ This method is used to create a QR code from a text.

        Args:
            text (str): The text to be converted to a QR code.
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        
        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code image
        img.save("static/qrcode.png")
    
    @staticmethod
    def remove():
        """ 
            This method is used to remove the QR code.
        """
        os.remove("static/qrcode.png")