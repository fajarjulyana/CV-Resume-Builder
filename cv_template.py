CV_HTML_TEMPLATE = {
    'Modern Professional': """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {
                size: A4;
                margin: 0;
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: '{{ style.font_main }}', sans-serif;
            }

            body {
                background: white;
                color: {{ style.color_secondary }};
                line-height: 1.6;
                width: 210mm;
                min-height: 297mm;
                margin: 0 auto;
            }

            .cv-container {
                width: 210mm;
                min-height: 297mm;
                margin: 0;
                padding: 15mm;
                display: grid;
                grid-template-columns: 70mm 1fr;
                gap: 15mm;
                background: white;
            }

            .sidebar {
                background: {{ style.color_primary }};
                color: white;
                padding: 15mm 10mm;
                border-radius: 4mm;
                height: 267mm;
            }

            .main-content {
                padding: 0;
                height: 267mm;
                overflow: hidden;
            }

            .header {
                text-align: center;
                margin-bottom: 8mm;
            }

            .photo {
                width: 40mm;
                height: 40mm;
                border-radius: 50%;
                margin: 0 auto 5mm;
                display: block;
                object-fit: cover;
                border: 0.75mm solid white;
            }

            h1 {
                font-family: '{{ style.font_header }}', sans-serif;
                color: {{ style.color_primary }};
                font-size: 9mm;
                margin-bottom: 3mm;
            }

            .section {
                margin-bottom: {{ style.sections_spacing }}px;
            }

            .section-title {
                font-family: '{{ style.font_header }}', sans-serif;
                color: {{ style.color_primary }};
                font-size: 6mm;
                margin-bottom: 4mm;
                border-bottom: 0.5mm solid {{ style.border_color }};
                padding-bottom: 1mm;
            }

            .contact-info {
                margin-bottom: 8mm;
            }

            .contact-item {
                margin-bottom: 2mm;
                font-size: 3.5mm;
            }

            .education-item, .experience-item {
                margin-bottom: 5mm;
            }

            .education-item h3, .experience-item h3 {
                color: {{ style.color_primary }};
                margin-bottom: 1mm;
                font-size: 4mm;
            }

            .skills-list {
                display: flex;
                flex-wrap: wrap;
                gap: 2mm;
            }

            .skill-item {
                background: rgba(255, 255, 255, 0.1);
                padding: 1mm 3mm;
                border-radius: 2mm;
                font-size: 3.5mm;
            }

            .about-me {
                margin-bottom: 8mm;
                line-height: 1.8;
                text-align: justify;
                font-size: 3.5mm;
            }

            p {
                font-size: 3.5mm;
            }

            .social-links {
                margin-top: 4mm;
            }

            .social-link {
                color: white;
                text-decoration: none;
                display: block;
                margin-bottom: 2mm;
                font-size: 3.5mm;
            }

            .social-link:hover {
                text-decoration: underline;
            }
            .qr-code {
                width: 30mm;
                height: 30mm;
                margin: 5mm auto;
            }

            .qr-code img {
                width: 100%;
                height: 100%;
                object-fit: contain;
            }

            .qr-label {
                text-align: center;
                color: white;
                font-size: 3mm;
                margin-top: 2mm;
            }
        </style>
    </head>
    <body>
        <div class="cv-container">
            <div class="sidebar">
                {% if photo %}
                <img src="{{ photo }}" alt="Profile Photo" class="photo">
                {% endif %}

                <div class="contact-info">
                    <h2 class="section-title" style="color: white; border-color: rgba(255,255,255,0.3);">Contact</h2>
                    <div class="contact-item">{{ email }}</div>
                    <div class="contact-item">{{ phone }}</div>
                    {% if linkedin or github %}
                    <div class="social-links">
                        {% if linkedin %}
                        <a href="{{ linkedin }}" class="social-link" target="_blank">LinkedIn</a>
                        {% endif %}
                        {% if github %}
                        <a href="{{ github }}" class="social-link" target="_blank">GitHub</a>
                        {% endif %}
                    </div>
                    {% endif %}

                    {% if contact_qr %}
                    <div class="qr-code">
                        <img src="{{ contact_qr }}" alt="Contact QR Code">
                        <div class="qr-label">Scan untuk menyimpan kontak</div>
                    </div>
                    {% endif %}
                </div>

                <div class="section">
                    <h2 class="section-title" style="color: white; border-color: rgba(255,255,255,0.3);">Skills</h2>
                    <div class="skills-list">
                        {% for skill in skills.split(',') %}
                        <div class="skill-item">{{ skill.strip() }}</div>
                        {% endfor %}
                    </div>
                </div>
            </div>

            <div class="main-content">
                <div class="header">
                    <h1>{{ full_name }}</h1>
                </div>

                {% if about_me %}
                <div class="section">
                    <h2 class="section-title">Tentang Saya</h2>
                    <div class="about-me">
                        {{ about_me }}
                    </div>
                </div>
                {% endif %}

                <div class="section">
                    <h2 class="section-title">Education</h2>
                    {% for edu in education %}
                    <div class="education-item">
                        <h3>{{ edu.degree }}</h3>
                        <div>{{ edu.school }}</div>
                        <div>{{ edu.year }}</div>
                    </div>
                    {% endfor %}
                </div>

                <div class="section">
                    <h2 class="section-title">Experience</h2>
                    {% for exp in experience %}
                    <div class="experience-item">
                        <h3>{{ exp.title }}</h3>
                        <div><strong>{{ exp.company }}</strong> - {{ exp.duration }}</div>
                        <p>{{ exp.description }}</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </body>
    </html>
    """,
    'Creative Minimal': """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {
                size: A4;
                margin: 0;
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: '{{ style.font_main }}', sans-serif;
            }

            body {
                background: white;
                color: {{ style.color_secondary }};
                line-height: 1.6;
                width: 210mm;
                min-height: 297mm;
                margin: 0 auto;
            }

            .cv-container {
                width: 210mm;
                min-height: 297mm;
                padding: 20mm;
                background: white;
            }

            .header {
                display: flex;
                align-items: center;
                margin-bottom: 15mm;
                gap: 10mm;
            }

            .photo {
                width: 50mm;
                height: 50mm;
                border-radius: 4mm;
                object-fit: cover;
            }

            .header-content {
                flex: 1;
            }

            h1 {
                font-family: '{{ style.font_header }}', sans-serif;
                color: {{ style.color_primary }};
                font-size: 12mm;
                margin-bottom: 4mm;
            }

            .contact-info {
                display: flex;
                gap: 5mm;
                font-size: 3.5mm;
                color: {{ style.color_secondary }};
            }

            .main-grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 10mm;
            }

            .section {
                margin-bottom: {{ style.sections_spacing }}px;
            }

            .section-title {
                font-family: '{{ style.font_header }}', sans-serif;
                color: {{ style.color_primary }};
                font-size: 6mm;
                margin-bottom: 4mm;
                position: relative;
                padding-bottom: 2mm;
            }

            .section-title::after {
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                width: 15mm;
                height: 0.5mm;
                background: {{ style.color_primary }};
            }

            .about-me {
                grid-column: span 2;
                font-size: 3.5mm;
                line-height: 1.8;
                color: {{ style.color_secondary }};
                margin-bottom: 8mm;
            }

            .skills-list {
                display: flex;
                flex-wrap: wrap;
                gap: 2mm;
            }

            .skill-item {
                background: {{ style.color_primary }};
                color: white;
                padding: 1mm 3mm;
                border-radius: 2mm;
                font-size: 3.5mm;
            }

            .education-item, .experience-item {
                margin-bottom: 5mm;
                padding: 4mm;
                border-left: 0.5mm solid {{ style.color_primary }};
            }

            .education-item h3, .experience-item h3 {
                color: {{ style.color_primary }};
                font-size: 4mm;
                margin-bottom: 1mm;
            }

            .social-links {
                display: flex;
                gap: 4mm;
                margin-top: 2mm;
            }

            .social-link {
                color: {{ style.color_secondary }};
                text-decoration: none;
                font-size: 3.5mm;
                padding: 1mm 3mm;
                border: 0.5mm solid {{ style.color_primary }};
                border-radius: 2mm;
            }

            .social-link:hover {
                background: {{ style.color_primary }};
                color: white;
            }
        </style>
    </head>
    <body>
        <div class="cv-container">
            <div class="header">
                {% if photo %}
                <img src="{{ photo }}" alt="Profile Photo" class="photo">
                {% endif %}
                <div class="header-content">
                    <h1>{{ full_name }}</h1>
                    <div class="contact-info">
                        <div>{{ email }}</div>
                        <div>|</div>
                        <div>{{ phone }}</div>
                    </div>
                    {% if linkedin or github %}
                    <div class="social-links">
                        {% if linkedin %}
                        <a href="{{ linkedin }}" class="social-link" target="_blank">LinkedIn</a>
                        {% endif %}
                        {% if github %}
                        <a href="{{ github }}" class="social-link" target="_blank">GitHub</a>
                        {% endif %}
                    </div>
                    {% endif %}
                </div>
            </div>

            <div class="main-grid">
                {% if about_me %}
                <div class="about-me">
                    <h2 class="section-title">Tentang Saya</h2>
                    <div class="about-me-content">
                        {{ about_me }}
                    </div>
                </div>
                {% endif %}

                <div class="section">
                    <h2 class="section-title">Education</h2>
                    {% for edu in education %}
                    <div class="education-item">
                        <h3>{{ edu.degree }}</h3>
                        <div>{{ edu.school }}</div>
                        <div>{{ edu.year }}</div>
                    </div>
                    {% endfor %}
                </div>

                <div class="section">
                    <h2 class="section-title">Skills</h2>
                    <div class="skills-list">
                        {% for skill in skills.split(',') %}
                        <div class="skill-item">{{ skill.strip() }}</div>
                        {% endfor %}
                    </div>
                </div>

                <div class="section" style="grid-column: span 2;">
                    <h2 class="section-title">Experience</h2>
                    {% for exp in experience %}
                    <div class="experience-item">
                        <h3>{{ exp.title }}</h3>
                        <div><strong>{{ exp.company }}</strong> - {{ exp.duration }}</div>
                        <p>{{ exp.description }}</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </body>
    </html>
    """,
    'Executive Plus': """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: '{{ style.font_main }}', serif;
            }
            
            body {
                background: white;
                color: {{ style.color_secondary }};
                line-height: 1.6;
            }
            
            .cv-container {
                max-width: 210mm;
                margin: 0 auto;
                padding: 20mm;
            }
            
            .header {
                text-align: center;
                margin-bottom: 40px;
                border-bottom: 3px double {{ style.color_primary }};
                padding-bottom: 20px;
            }
            
            .photo {
                width: 120px;
                height: 120px;
                border-radius: 50%;
                margin: 0 auto 20px;
                display: block;
                object-fit: cover;
                border: 2px solid {{ style.color_primary }};
            }
            
            h1 {
                font-family: '{{ style.font_header }}', serif;
                color: {{ style.color_primary }};
                font-size: 42px;
                margin-bottom: 10px;
            }
            
            .contact-info {
                display: flex;
                justify-content: center;
                gap: 30px;
                margin-top: 20px;
            }
            
            .section {
                margin-bottom: {{ style.sections_spacing }}px;
            }
            
            .section-title {
                font-family: '{{ style.font_header }}', serif;
                color: {{ style.color_primary }};
                font-size: 28px;
                margin-bottom: 20px;
                text-align: center;
                position: relative;
            }
            
            .section-title::after {
                content: '';
                display: block;
                width: 100px;
                height: 2px;
                background: {{ style.color_primary }};
                margin: 10px auto;
            }
            
            .education-item, .experience-item {
                margin-bottom: 25px;
                padding: 20px;
                border: 1px solid {{ style.border_color }};
            }
            
            .education-item h3, .experience-item h3 {
                color: {{ style.color_primary }};
                margin-bottom: 10px;
                font-size: 20px;
            }
            
            .skills-list {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                gap: 15px;
                padding: 20px;
            }
            
            .skill-item {
                background: white;
                padding: 10px 20px;
                border: 1px solid {{ style.border_color }};
                text-align: center;
                font-style: italic;
            }
            
            .social-links {
                display: flex;
                justify-content: center;
                gap: 5mm;
                margin-top: 3mm;
            }
            
            .social-link {
                color: {{ style.color_primary }};
                text-decoration: none;
                font-style: italic;
                font-size: 3.5mm;
            }
            
            .social-link:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="cv-container">
            <div class="header">
                {% if photo %}
                <img src="{{ photo }}" alt="Profile Photo" class="photo">
                {% endif %}
                <h1>{{ full_name }}</h1>
                <div class="contact-info">
                    <div>{{ email }}</div>
                    <div>{{ phone }}</div>
                </div>
                {% if linkedin or github %}
                <div class="social-links">
                    {% if linkedin %}
                    <a href="{{ linkedin }}" class="social-link" target="_blank">LinkedIn</a>
                    {% endif %}
                    {% if github %}
                    <a href="{{ github }}" class="social-link" target="_blank">GitHub</a>
                    {% endif %}
                </div>
                {% endif %}
            </div>
            
            <div class="section">
                <h2 class="section-title">Education</h2>
                {% for edu in education %}
                <div class="education-item">
                    <h3>{{ edu.degree }}</h3>
                    <div>{{ edu.school }}</div>
                    <div>{{ edu.year }}</div>
                </div>
                {% endfor %}
            </div>
            
            <div class="section">
                <h2 class="section-title">Professional Experience</h2>
                {% for exp in experience %}
                <div class="experience-item">
                    <h3>{{ exp.title }}</h3>
                    <div><strong>{{ exp.company }}</strong> - {{ exp.duration }}</div>
                    <p>{{ exp.description }}</p>
                </div>
                {% endfor %}
            </div>
            
            <div class="section">
                <h2 class="section-title">Areas of Expertise</h2>
                <div class="skills-list">
                    {% for skill in skills.split(',') %}
                    <div class="skill-item">{{ skill.strip() }}</div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </body>
    </html>
    """,
    'Corporate Elite': """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {
                size: A4;
                margin: 0;
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: '{{ style.font_main }}', sans-serif;
            }

            body {
                background: white;
                color: {{ style.color_secondary }};
                line-height: 1.6;
                width: 210mm;
                min-height: 297mm;
                margin: 0 auto;
            }

            .cv-container {
                width: 210mm;
                min-height: 297mm;
                padding: 20mm;
                background: white;
                display: grid;
                grid-template-columns: 1fr;
                gap: 10mm;
            }

            .header {
                border-bottom: 2mm solid {{ style.color_primary }};
                padding-bottom: 10mm;
                display: grid;
                grid-template-columns: auto 1fr;
                gap: 10mm;
                align-items: center;
            }

            .photo {
                width: 45mm;
                height: 45mm;
                border-radius: 50%;
                object-fit: cover;
                border: 1mm solid {{ style.color_primary }};
            }

            .header-content {
                display: flex;
                flex-direction: column;
                gap: 3mm;
            }

            h1 {
                font-family: '{{ style.font_header }}', sans-serif;
                color: {{ style.color_primary }};
                font-size: 12mm;
                line-height: 1.2;
            }

            .contact-info {
                display: flex;
                gap: 5mm;
                font-size: 3.5mm;
                flex-wrap: wrap;
            }

            .contact-item {
                background: {{ style.color_primary }};
                color: white;
                padding: 1mm 3mm;
                border-radius: 1mm;
            }

            .main-content {
                display: grid;
                grid-template-columns: 2fr 1fr;
                gap: 10mm;
            }

            .left-column {
                border-right: 0.5mm solid {{ style.border_color }};
                padding-right: 10mm;
            }

            .section {
                margin-bottom: {{ style.sections_spacing }}px;
            }

            .section-title {
                font-family: '{{ style.font_header }}', sans-serif;
                color: {{ style.color_primary }};
                font-size: 6mm;
                margin-bottom: 5mm;
                display: flex;
                align-items: center;
                gap: 3mm;
            }

            .section-title::before {
                content: '';
                display: block;
                width: 8mm;
                height: 0.5mm;
                background: {{ style.color_primary }};
            }

            .about-me {
                font-size: 3.5mm;
                line-height: 1.8;
                color: {{ style.color_secondary }};
                margin-bottom: 8mm;
                text-align: justify;
            }

            .experience-item {
                margin-bottom: 8mm;
                position: relative;
                padding-left: 5mm;
            }

            .experience-item::before {
                content: '';
                position: absolute;
                left: 0;
                top: 0;
                bottom: 0;
                width: 0.5mm;
                background: {{ style.color_primary }};
            }

            .experience-item h3 {
                color: {{ style.color_primary }};
                font-size: 4.5mm;
                margin-bottom: 2mm;
            }

            .education-item {
                margin-bottom: 6mm;
                padding: 4mm;
                background: rgba({{ style.color_primary }}, 0.05);
                border-radius: 2mm;
            }

            .education-item h3 {
                color: {{ style.color_primary }};
                font-size: 4mm;
                margin-bottom: 1mm;
            }

            .skills-list {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 3mm;
            }

            .skill-item {
                background: white;
                padding: 2mm 3mm;
                border-radius: 1mm;
                font-size: 3.5mm;
                border: 0.3mm solid {{ style.color_primary }};
                color: {{ style.color_primary }};
                text-align: center;
            }

            .social-links {
                display: flex;
                gap: 3mm;
                margin-top: 3mm;
            }

            .social-link {
                background: {{ style.color_primary }};
                color: white;
                padding: 1mm 3mm;
                border-radius: 1mm;
                text-decoration: none;
                font-size: 3.5mm;
                display: inline-block;
            }

            .social-link:hover {
                opacity: 0.9;
            }
        </style>
    </head>
    <body>
        <div class="cv-container">
            <div class="header">
                {% if photo %}
                <img src="{{ photo }}" alt="Profile Photo" class="photo">
                {% endif %}
                <div class="header-content">
                    <h1>{{ full_name }}</h1>
                    <div class="contact-info">
                        <div class="contact-item">{{ email }}</div>
                        <div class="contact-item">{{ phone }}</div>
                    </div>
                    {% if linkedin or github %}
                    <div class="social-links">
                        {% if linkedin %}
                        <a href="{{ linkedin }}" class="social-link" target="_blank">LinkedIn</a>
                        {% endif %}
                        {% if github %}
                        <a href="{{ github }}" class="social-link" target="_blank">GitHub</a>
                        {% endif %}
                    </div>
                    {% endif %}
                </div>
            </div>

            <div class="main-content">
                <div class="left-column">
                    {% if about_me %}
                    <div class="section">
                        <h2 class="section-title">Tentang Saya</h2>
                        <div class="about-me">
                            {{ about_me }}
                        </div>
                    </div>
                    {% endif %}

                    <div class="section">
                        <h2 class="section-title">Experience</h2>
                        {% for exp in experience %}
                        <div class="experience-item">
                            <h3>{{ exp.title }}</h3>
                            <div><strong>{{ exp.company }}</strong> - {{ exp.duration }}</div>
                            <p>{{ exp.description }}</p>
                        </div>
                        {% endfor %}
                    </div>
                </div>

                <div class="right-column">
                    <div class="section">
                        <h2 class="section-title">Education</h2>
                        {% for edu in education %}
                        <div class="education-item">
                            <h3>{{ edu.degree }}</h3>
                            <div>{{ edu.school }}</div>
                            <div>{{ edu.year }}</div>
                        </div>
                        {% endfor %}
                    </div>

                    <div class="section">
                        <h2 class="section-title">Skills</h2>
                        <div class="skills-list">
                            {% for skill in skills.split(',') %}
                            <div class="skill-item">{{ skill.strip() }}</div>
                            {% endfor %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
}