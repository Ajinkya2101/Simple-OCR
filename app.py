import streamlit as st
from PIL import Image
import pytesseract
import os

# Configure Tesseract for Hindi and English
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
languages = 'eng+hin'  # for English and Hindi OCR

def extract_text(image):
    text = pytesseract.image_to_string(image, lang=languages)
    return text

def keyword_search(extracted_text, keyword):
    if keyword.lower() in extracted_text.lower():
        return True
    return False

# Streamlit app
st.title("OCR Web Application for Hindi and English")

# File uploader for image
uploaded_image = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

if uploaded_image:
    image = Image.open(uploaded_image)
    
    # Display the uploaded image
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Extract text using OCR
    extracted_text = extract_text(image)
    st.subheader("Extracted Text:")
    st.text(extracted_text)

    # Keyword search functionality
    keyword = st.text_input("Enter keyword to search in extracted text:")

    if keyword:
        if keyword_search(extracted_text, keyword):
            st.success(f"The keyword '{keyword}' was found in the text!")
        else:
            st.error(f"The keyword '{keyword}' was not found in the text.")

