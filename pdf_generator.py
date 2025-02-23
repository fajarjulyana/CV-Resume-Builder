import os
from weasyprint import HTML, CSS
from jinja2 import Template
import base64
from PIL import Image
import io
from cv_template import CV_HTML_TEMPLATE
import requests
from utils import generate_contact_qr

def generate_pdf(cv_data, template_config):
    # Process photo if exists
    if 'photo' in cv_data:
        try:
            if isinstance(cv_data['photo'], str) and cv_data['photo'].startswith('http'):
                # Handle URL image
                response = requests.get(cv_data['photo'])
                img_data = response.content
            else:
                # Handle uploaded file
                img = Image.open(cv_data['photo'])
                img_buffer = io.BytesIO()
                img.save(img_buffer, format='PNG')
                img_data = img_buffer.getvalue()

            # Convert to base64 for HTML embedding
            cv_data['photo'] = f"data:image/png;base64,{base64.b64encode(img_data).decode()}"
        except Exception as e:
            print(f"Error processing photo: {str(e)}")
            cv_data['photo'] = None

    # Generate QR code for contact information
    cv_data['contact_qr'] = generate_contact_qr(cv_data)

    # Get template HTML based on style
    html_template = CV_HTML_TEMPLATE.get(template_config['name'], CV_HTML_TEMPLATE['Modern Professional'])

    # Create template context with style from template_config
    template_context = {
        'style': template_config['style'],
        **cv_data
    }

    # Render template with CV data
    template = Template(html_template)
    html_content = template.render(**template_context)

    # Create PDF from HTML
    pdf_buffer = io.BytesIO()
    HTML(string=html_content).write_pdf(
        pdf_buffer,
        stylesheets=[],
        optimize_size=('fonts', 'images')
    )

    pdf_buffer.seek(0)
    return pdf_buffer.getvalue()