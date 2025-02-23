import streamlit as st
from PIL import Image
import io
from templates import CV_TEMPLATES, SAMPLE_IMAGES
from pdf_generator import generate_pdf
from styles import apply_styles
from utils import load_profile_pics

def main():
    apply_styles()

    st.title("Professional CV Builder")
    st.markdown("""
        <div style='text-align: center; color: #666; margin-bottom: 2rem;'>
        Buat CV profesional Anda dengan template yang menarik
        </div>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'current_template' not in st.session_state:
        st.session_state.current_template = 0
    if 'cv_data' not in st.session_state:
        st.session_state.cv_data = {}
    if 'custom_colors' not in st.session_state:
        st.session_state.custom_colors = {}
        # Initialize custom colors for all templates
        for idx, template in enumerate(CV_TEMPLATES):
            st.session_state.custom_colors[idx] = {
                'primary': template['style']['color_primary'],
                'secondary': template['style']['color_secondary'],
                'border': template['style']['border_color']
            }

    # Sidebar for template selection and customization
    with st.sidebar:
        st.header("Pilih Template")
        st.markdown("<div class='template-selection'>", unsafe_allow_html=True)

        for idx, template in enumerate(CV_TEMPLATES):
            st.markdown(f"""
                <div class='template-preview'>
                    <h4 style='color: {template['style']['color_primary']};'>{template['name']}</h4>
                </div>
            """, unsafe_allow_html=True)

            if st.button("Gunakan Template", key=f"template_{idx}"):
                st.session_state.current_template = idx

            # Color customization for each template
            if idx == st.session_state.current_template:
                st.markdown("### Kustomisasi Warna")
                # Ensure the index exists in custom_colors
                if idx not in st.session_state.custom_colors:
                    st.session_state.custom_colors[idx] = {
                        'primary': template['style']['color_primary'],
                        'secondary': template['style']['color_secondary'],
                        'border': template['style']['border_color']
                    }

                custom_primary = st.color_picker(
                    "Warna Utama",
                    st.session_state.custom_colors[idx]['primary'],
                    key=f"primary_{idx}"
                )
                custom_secondary = st.color_picker(
                    "Warna Sekunder",
                    st.session_state.custom_colors[idx]['secondary'],
                    key=f"secondary_{idx}"
                )
                custom_border = st.color_picker(
                    "Warna Border",
                    st.session_state.custom_colors[idx]['border'],
                    key=f"border_{idx}"
                )

                # Update custom colors in session state
                st.session_state.custom_colors[idx].update({
                    'primary': custom_primary,
                    'secondary': custom_secondary,
                    'border': custom_border
                })

                # Update template style with custom colors
                CV_TEMPLATES[idx]['style'].update({
                    'color_primary': custom_primary,
                    'color_secondary': custom_secondary,
                    'border_color': custom_border
                })

            st.image(template['preview_url'], use_container_width=True)
            st.markdown("<hr>", unsafe_allow_html=True)

    # Main content
    tabs = st.tabs(["📋 Informasi Pribadi", "🎓 Pendidikan", "💼 Pengalaman", "🔧 Keahlian", "👀 Preview"])

    with tabs[0]:
        st.subheader("Informasi Pribadi")
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.cv_data['full_name'] = st.text_input("Nama Lengkap", key="name")
            st.session_state.cv_data['email'] = st.text_input("Email", key="email")
            st.session_state.cv_data['phone'] = st.text_input("Nomor Telepon", key="phone")
            st.session_state.cv_data['linkedin'] = st.text_input("LinkedIn URL", key="linkedin", 
                help="Contoh: https://linkedin.com/in/username")
            st.session_state.cv_data['github'] = st.text_input("GitHub URL", key="github",
                help="Contoh: https://github.com/username")
            st.session_state.cv_data['about_me'] = st.text_area(
                "Tentang Saya",
                help="Deskripsikan diri Anda secara singkat dan profesional",
                height=150,
                key="about_me",
                value=st.session_state.cv_data.get('about_me', '')
            )

        with col2:
            st.markdown("<div class='profile-container'>", unsafe_allow_html=True)
            profile_pics = load_profile_pics()
            selected_pic = st.selectbox("Pilih Foto Profil", ["Upload Sendiri"] + list(profile_pics.keys()))

            if selected_pic == "Upload Sendiri":
                uploaded_file = st.file_uploader("Upload foto Anda", type=['jpg', 'png', 'jpeg'])
                if uploaded_file:
                    st.session_state.cv_data['photo'] = uploaded_file
                    st.image(uploaded_file, width=150)
            else:
                st.session_state.cv_data['photo'] = profile_pics[selected_pic]
                st.image(profile_pics[selected_pic], width=150)
            st.markdown("</div>", unsafe_allow_html=True)

    with tabs[1]:
        st.subheader("Pendidikan")
        if 'education' not in st.session_state.cv_data:
            st.session_state.cv_data['education'] = []

        for i in range(len(st.session_state.cv_data['education']) + 1):
            st.markdown(f"### Pendidikan {i+1}")
            col1, col2, col3 = st.columns(3)

            # Inisialisasi entri baru jika diperlukan
            if i >= len(st.session_state.cv_data['education']):
                st.session_state.cv_data['education'].append({"degree": "", "school": "", "year": ""})

            with col1:
                st.session_state.cv_data['education'][i]['degree'] = st.text_input(
                    "Gelar",
                    value=st.session_state.cv_data['education'][i]['degree'],
                    key=f"degree_{i}"
                )
            with col2:
                st.session_state.cv_data['education'][i]['school'] = st.text_input(
                    "Institusi",
                    value=st.session_state.cv_data['education'][i]['school'],
                    key=f"school_{i}"
                )
            with col3:
                st.session_state.cv_data['education'][i]['year'] = st.text_input(
                    "Tahun",
                    value=st.session_state.cv_data['education'][i]['year'],
                    key=f"year_{i}"
                )

            if i > 0:  # Tombol hapus untuk entri selain yang pertama
                if st.button("🗑️ Hapus", key=f"del_edu_{i}"):
                    st.session_state.cv_data['education'].pop(i)
                    st.rerun()

        if st.button("➕ Tambah Pendidikan Lain"):
            st.session_state.cv_data['education'].append({"degree": "", "school": "", "year": ""})
            st.rerun()

    with tabs[2]:
        st.subheader("Pengalaman Kerja")
        if 'experience' not in st.session_state.cv_data:
            st.session_state.cv_data['experience'] = []

        for i in range(len(st.session_state.cv_data['experience']) + 1):
            st.markdown(f"### Pengalaman {i+1}")

            # Inisialisasi entri baru jika diperlukan
            if i >= len(st.session_state.cv_data['experience']):
                st.session_state.cv_data['experience'].append({
                    "title": "",
                    "company": "",
                    "duration": "",
                    "description": ""
                })

            col1, col2, col3 = st.columns(3)
            with col1:
                st.session_state.cv_data['experience'][i]['title'] = st.text_input(
                    "Posisi",
                    value=st.session_state.cv_data['experience'][i]['title'],
                    key=f"title_{i}"
                )
            with col2:
                st.session_state.cv_data['experience'][i]['company'] = st.text_input(
                    "Perusahaan",
                    value=st.session_state.cv_data['experience'][i]['company'],
                    key=f"company_{i}"
                )
            with col3:
                st.session_state.cv_data['experience'][i]['duration'] = st.text_input(
                    "Durasi",
                    value=st.session_state.cv_data['experience'][i]['duration'],
                    key=f"duration_{i}"
                )

            st.session_state.cv_data['experience'][i]['description'] = st.text_area(
                "Deskripsi Pekerjaan",
                value=st.session_state.cv_data['experience'][i]['description'],
                key=f"description_{i}"
            )

            if i > 0:  # Tombol hapus untuk entri selain yang pertama
                if st.button("🗑️ Hapus", key=f"del_exp_{i}"):
                    st.session_state.cv_data['experience'].pop(i)
                    st.rerun()

            st.markdown("---")

        if st.button("➕ Tambah Pengalaman Lain"):
            st.session_state.cv_data['experience'].append({
                "title": "",
                "company": "",
                "duration": "",
                "description": ""
            })
            st.rerun()

    with tabs[3]:
        st.subheader("Keahlian")
        if 'skills' not in st.session_state.cv_data:
            st.session_state.cv_data['skills'] = ""
        st.session_state.cv_data['skills'] = st.text_area(
            "Keahlian (pisahkan dengan koma)", 
            value=st.session_state.cv_data.get('skills', ""),
            help="Contoh: Microsoft Office, Adobe Photoshop, Public Speaking"
        )

    with tabs[4]:
        st.subheader("Preview dan Unduh")
        if st.button("🔄 Generate PDF", type="primary"):
            try:
                with st.spinner('Membuat CV...'):
                    # Get current template with custom colors
                    current_template = CV_TEMPLATES[st.session_state.current_template].copy()
                    current_template['style'].update(st.session_state.custom_colors[st.session_state.current_template])

                    pdf_bytes = generate_pdf(
                        st.session_state.cv_data,
                        current_template
                    )
                    st.success("CV berhasil dibuat!")
                    st.download_button(
                        label="📥 Unduh CV",
                        data=pdf_bytes,
                        file_name="cv.pdf",
                        mime="application/pdf"
                    )
            except Exception as e:
                st.error(f"Error saat membuat PDF: {str(e)}")

if __name__ == "__main__":
    main()