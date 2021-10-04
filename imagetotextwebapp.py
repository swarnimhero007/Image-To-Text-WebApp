import pytesseract
from PIL import Image
import streamlit as st
from gtts import gTTS

st.title("Image to Text Web App")
uploaded_image = st.file_uploader('Upload Image', type=['png','jpeg','jpg'])
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
aud=st.checkbox("Want Audio for Extracted Text ?")
extracte=st.button("Extract Text From Image")
output = st.empty()
if not uploaded_image: output.warning('Please upload an image to proceed!')
else:
    if extracte:
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.subheader("Given Image :")
            st.image(image)
            text = str(pytesseract.image_to_string(image))
            text1 = text.replace('', '').replace(' ', '')

            if text1.isspace():
                st.info("No text Extracted.")
            else:
                st.subheader("Extracted Text :")
                st.code(text)
                if aud:
                    st.subheader("Audio:")
                    tts = gTTS(text=text, lang="en-us", tld='co.in')
                    tts.save('textgiven.mp3')
                    audio_file = open(f"textgiven.mp3", "rb")
                    audio_bytes = audio_file.read()
                    st.markdown(f"## Audio of Given Text:")
                    st.audio(audio_bytes, format="audio/mp3", start_time=0)


