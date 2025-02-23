import requests
from io import BytesIO
from PIL import Image
import qrcode
import base64

def load_profile_pics():
    sample_pics = {
        'Professional 1': 'https://images.unsplash.com/photo-1576558656222-ba66febe3dec',
        'Professional 2': 'https://images.unsplash.com/photo-1554774853-b415df9eeb92',
        'Professional 3': 'https://images.unsplash.com/photo-1554774853-6a56f62c6451'
    }

    return sample_pics

def validate_image(image_file):
    try:
        img = Image.open(image_file)
        return True
    except:
        return False

def resize_image(image, max_size=(800, 800)):
    img = Image.open(image)
    img.thumbnail(max_size)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()

def generate_contact_qr(cv_data):
    """Generate QR code with vCard format for contact information"""
    # Create vCard format string
    vcard = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"FN:{cv_data.get('full_name', '')}",
        f"EMAIL:{cv_data.get('email', '')}",
        f"TEL:{cv_data.get('phone', '')}"
    ]

    # Add social media if available
    if cv_data.get('linkedin'):
        vcard.append(f"URL;type=LINKEDIN:{cv_data['linkedin']}")
    if cv_data.get('github'):
        vcard.append(f"URL;type=GITHUB:{cv_data['github']}")

    vcard.append("END:VCARD")
    vcard_text = "\n".join(vcard)

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_text)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert to base64 for HTML embedding
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}"