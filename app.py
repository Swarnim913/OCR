import streamlit as st
from PIL import Image
import pytesseract
import re
import cv2
import numpy as np
from io import BytesIO
import base64
from gtts import gTTS
import os
from langdetect import detect

# Specify Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Apply custom CSS to style the UI (keep your existing styles)
st.markdown("""
    <style>
        /* Your custom CSS styles */
    </style>
""", unsafe_allow_html=True)

# Custom header
st.markdown("<div class='header'><h1>Swarnim's OCR & Keyword Search App 📚🔍</h1></div>", unsafe_allow_html=True)

# Sidebar for additional features
st.sidebar.header("🔧 Options")

# Language selection
lang_options = {
    "English": "eng",
    "Hindi": "hin",
    "French": "fra",
    "Spanish": "spa",
    "German": "deu"
}
lang_selection = st.sidebar.multiselect("Select OCR Language(s)", options=list(lang_options.keys()), default=["English"])
ocr_lang = '+'.join([lang_options[lang] for lang in lang_selection])

# Keyword search options
st.sidebar.subheader("🔍 Keyword Search Options")
case_sensitive = st.sidebar.checkbox("Case Sensitive Search", value=False)
whole_word = st.sidebar.checkbox("Match Whole Word Only", value=False)




# Upload an image file
uploaded_image = st.file_uploader("📤 Upload an Image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Open the uploaded image
    image = Image.open(uploaded_image)
    
    # Display the image in a centered, modern look
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)
    
    # Specify custom config for Tesseract
    custom_config = r'--oem 3 --psm 6'
    
    # Perform OCR on the image
    with st.spinner("Extracting text from the image... ⏳"):
        extracted_text = pytesseract.image_to_string(image, lang=ocr_lang, config=custom_config)
    
    # Clean up the extracted text
    cleaned_text = extracted_text.strip()  # Remove leading/trailing whitespace
    # Optionally, replace multiple blank lines with a single line
    cleaned_text = re.sub(r'\n\s*\n', '\n', cleaned_text)
    
    # Language detection
    detected_lang = detect(cleaned_text)
    st.markdown(f"**Detected Language:** {detected_lang.upper()}")
    
    # Display the cleaned extracted text
    st.text_area("📄 Extracted Text", cleaned_text, height=300, placeholder="Extracted text will appear here...")
    
    # Download extracted text
    def get_text_download_link(text, filename):
        b64 = base64.b64encode(text.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">📥 Download Extracted Text</a>'
        return href
    
    st.markdown(get_text_download_link(cleaned_text, "extracted_text.txt"), unsafe_allow_html=True)
    
    # Mapping detected languages to gTTS language codes
    language_mapping = {
        'en': 'en',
        'hi': 'hi',
        'fr': 'fr',
        'es': 'es',
        'de': 'de',
        # Add more mappings as needed
    }
    
    # Map detected language to gTTS language code
    tts_lang = language_mapping.get(detected_lang, 'en')  # Default to English if not found
    
    
    


    
    # Keyword search functionality
    search_query = st.text_input("🔍 Enter keyword(s) to search (comma-separated)")
    
    if search_query:
        keywords = [kw.strip() for kw in search_query.split(',')]
        matches = {}
        for kw in keywords:
            flags = 0 if case_sensitive else re.IGNORECASE
            pattern = r'\b{}\b'.format(re.escape(kw)) if whole_word else re.escape(kw)
            if re.search(pattern, cleaned_text, flags):
                matches[kw] = True
            else:
                matches[kw] = False
    
        # Display search results
        for kw, found in matches.items():
            if found:
                st.success(f"✅ Keyword '{kw}' found in the extracted text.")
            else:
                st.error(f"❌ Keyword '{kw}' not found.")
    
        # Highlight keywords in text
        highlighted_text = cleaned_text
        for kw in keywords:
            flags = re.MULTILINE
            if not case_sensitive:
                flags |= re.IGNORECASE
            pattern = r'\b({})\b'.format(re.escape(kw)) if whole_word else f"({re.escape(kw)})"
            highlighted_text = re.sub(
                pattern,
                r"<mark style='background-color: yellow; color: black;'>\1</mark>",
                highlighted_text,
                flags=flags
            )
    
        # Display the highlighted text
        st.markdown(
            f"<div style='background-color: #fff; color: #000; padding: 10px; line-height: 1.5; border-radius: 10px;'>{highlighted_text}</div>", 
            unsafe_allow_html=True
        )
    
        # Now highlight the keyword in the original image
        img_cv = np.array(image.convert('RGB'))  # Ensure image is in RGB
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR for OpenCV
    
        # Get bounding box info for each word
        data = pytesseract.image_to_data(image, lang=ocr_lang, config=custom_config, output_type=pytesseract.Output.DICT)
    
        # Draw rectangles around searched keywords
        n_boxes = len(data['text'])
        for i in range(n_boxes):
            word = data['text'][i]
            for kw in keywords:
                flags = 0 if case_sensitive else re.IGNORECASE
                pattern = r'^{}$'.format(re.escape(kw)) if whole_word else re.escape(kw)
                if re.match(pattern, word, flags):
                    (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
                    img_cv = cv2.rectangle(img_cv, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle
    
        # Convert the image back to RGB (PIL format) and display it
        img_with_highlight = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        img_with_highlight_pil = Image.fromarray(img_with_highlight)
    
        st.image(img_with_highlight_pil, caption='🔍 Image with highlighted keyword(s)', use_column_width=True)
    
        # Option to download the highlighted image
        buffered = BytesIO()
        img_with_highlight_pil.save(buffered, format="PNG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode()
        href = f'<a href="data:file/png;base64,{img_b64}" download="highlighted_image.png">📥 Download Highlighted Image</a>'
        st.markdown(href, unsafe_allow_html=True)
    
# Custom footer
st.markdown("""
    <div class="footer">
        <p>Swarnim's OCR & Keyword Search App</p>
    </div>
""", unsafe_allow_html=True)