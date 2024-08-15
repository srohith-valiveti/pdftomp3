PDF to MP3 Converter with Translation
This Streamlit app allows you to upload a PDF or enter text, translate the content into a different language, and convert the translated text into an MP3 file. It's an all-in-one solution for generating audio from written content in various languages.

Features
PDF Upload: Extract text from PDF files.
Text Input: Option to input your own text.
Translation: Translate text into multiple languages.
Text-to-Speech: Convert translated text into an MP3 file.
Downloadable Audio: Download the generated MP3 file directly from the app.
Demo

How to Run the App
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.7 or higher
pip (Python package installer)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/pdf-to-mp3-translator.git
cd pdf-to-mp3-translator
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open the provided URL in your web browser to use the app.

Usage
Choose Input Type: Select either "Upload PDF" or "Write Text" from the radio button options.
Upload PDF / Enter Text: Depending on your choice, upload a PDF or enter text into the provided area.
Settings: Use the sidebar to select the target language and adjust the speech speed.
Translate and Convert: Click the "Translate and Convert to MP3" button. The app will translate the text and generate an MP3 file.
Download: Once the process is complete, you can listen to the audio directly in the app or download it.
Supported Languages
This app supports a wide range of languages for both translation and text-to-speech conversion. The available languages are dynamically retrieved from the supported languages of both the gTTS and Google Translate services.

Troubleshooting
Ensure your PDF files are text-based, as the app may not work well with scanned documents or PDFs without selectable text.
If the app fails to translate or convert text, check your internet connection and ensure the selected language is supported.
Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Streamlit
gTTS
pdfplumber
deep-translator
This README.md provides a comprehensive overview of your app, including installation instructions, usage details, and other relevant information. Modify the sections as needed to suit your project.
