import streamlit as st
from gtts import gTTS, lang
import pdfplumber
from io import BytesIO

# Set page configuration
st.set_page_config(page_title='PDF to MP3 Converter', layout='wide')

# Custom styling
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.markdown('<h1 style="color: #5a4d41; text-align: center;">Advanced PDF to MP3 Converter 📄➡️🔊</h1>', unsafe_allow_html=True)
st.markdown('<div class="big-font">Upload your PDF file or write your own text and convert it into an audio file!</div>', unsafe_allow_html=True)

# Sidebar for TTS Options
st.sidebar.header('Settings')
language_options = list(lang.tts_langs().keys())  # Dynamically fetch language codes
selected_language = st.sidebar.selectbox('Language', options=language_options, index=language_options.index('en'))
speech_speed = st.sidebar.slider('Speech Speed', 0.5, 2.0, 1.0)  # Min, Max, Default

# Main content
conversion_type = st.radio("Choose your input type:", ('Upload PDF', 'Write Text'))

if conversion_type == 'Upload PDF':
    uploaded_file = st.file_uploader("", type="pdf")
    if uploaded_file is not None:
        extracted_text = ''
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                extracted_text += ' ' + (page.extract_text() or '')
        edited_text = st.text_area("Edit the text before conversion:", value=extracted_text, height=200)
else:
    edited_text = st.text_area("Write your text here:", height=200)

# Convert edited text to MP3
if st.button('Convert to MP3'):
    if edited_text.strip() != "":
        with st.spinner('Converting text to MP3...'):
            tts = gTTS(edited_text, lang=selected_language, slow=speech_speed < 1)
            audio_file = BytesIO()
            tts.write_to_fp(audio_file)
            audio_file.seek(0)
            st.success('Conversion completed! Here is your audio:')
            st.audio(audio_file, format='audio/mp3')
            st.download_button(label="Download MP3", data=audio_file, file_name="converted_audio.mp3", mime="audio/mp3")
    else:
        st.error("Please upload a PDF or enter text to convert.")

# Footer
st.markdown('---')
st.markdown('<p style="color: #5a4d41; text-align: center;">Made with ❤️ and Streamlit</p>', unsafe_allow_html=True)
