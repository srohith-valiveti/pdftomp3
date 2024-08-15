import streamlit as st
from gtts import gTTS, lang
import pdfplumber
from io import BytesIO
from deep_translator import GoogleTranslator

# Set page configuration
st.set_page_config(page_title='PDF to MP3 Converter with Translation', layout='wide')

# Custom styling
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.markdown(
    '<h1 style="color: #5a4d41; text-align: center;">Advanced PDF to MP3 Converter with Translation 📄🌐➡️🔊</h1>',
    unsafe_allow_html=True)
st.markdown(
    '<div class="big-font">Upload your PDF file or write your own text, translate it, and convert it into an audio file!</div>',
    unsafe_allow_html=True)


# Function to get supported languages
def get_supported_languages():
    tts_langs = set(lang.tts_langs().keys())
    translator_langs = set(GoogleTranslator().get_supported_languages(as_dict=True).values())
    supported_langs = tts_langs.intersection(translator_langs)
    return {code: lang.tts_langs()[code] for code in supported_langs}


# Get supported languages
supported_languages = get_supported_languages()

# Sidebar for TTS Options
st.sidebar.header('Settings')
language_options = list(supported_languages.values())
selected_language_name = st.sidebar.selectbox('Target Language', options=language_options,
                                              index=language_options.index('English'))
selected_language_code = [code for code, name in supported_languages.items() if name == selected_language_name][0]
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
        edited_text = st.text_area("Edit the text before translation and conversion:", value=extracted_text, height=200)
else:
    edited_text = st.text_area("Write your text here:", height=200)

# Translate and convert edited text to MP3
if st.button('Translate and Convert to MP3'):
    if edited_text.strip() != "":
        with st.spinner('Translating and converting text to MP3...'):
            try:
                # Translate the text
                translator = GoogleTranslator(source='auto', target=selected_language_code)
                translated_text = translator.translate(edited_text)

                st.subheader("Translated Text:")
                st.write(translated_text)

                # Convert to speech
                tts = gTTS(translated_text, lang=selected_language_code, slow=speech_speed < 1)
                audio_file = BytesIO()
                tts.write_to_fp(audio_file)
                audio_file.seek(0)
                st.success('Translation and conversion completed! Here is your audio:')
                st.audio(audio_file, format='audio/mp3')
                st.download_button(label="Download MP3", data=audio_file, file_name="translated_audio.mp3",
                                   mime="audio/mp3")
            except Exception as e:
                st.error(f"An error occurred during translation or conversion: {str(e)}")
    else:
        st.error("Please upload a PDF or enter text to translate and convert.")

# Footer
st.markdown('---')
st.markdown('<p style="color: #5a4d41; text-align: center;">Made with ❤️ and Streamlit</p>', unsafe_allow_html=True)
