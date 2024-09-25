import streamlit as st
from PIL import Image, ImageDraw
import pytesseract
import re
import cv2
import numpy as np

# Apply custom CSS to style the UI
st.markdown("""
    <style>
        /* Modern font for the app */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');
        
        html, body, [class*="css"]  {
            font-family: 'Roboto', sans-serif;
        }

        /* Title customization */
        .css-h2j5ae {
            color: #008080;
            font-weight: 700;
            margin-bottom: 20px;
        }

        /* Button customization */
        .stButton>button {
            background-color: #008080;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 500;
        }

        /* Handle text area color for light and dark modes */
        body[data-theme="light"] .stTextArea textarea {
            background-color: #f9f9f9;
            color: black;
            border-radius: 8px;
            border: 1px solid #ddd;
            padding: 15px;
        }

        body[data-theme="dark"] .stTextArea textarea {
            background-color: black;
            color: white;
            border-radius: 8px;
            border: 1px solid #ddd;
            padding: 15px;
        }

        /* Highlighted keyword box customization */
        body[data-theme="light"] div[role="textbox"] {
            background-color: white;
            border-radius: 10px;
            padding: 15px;
        }
        
        body[data-theme="dark"] div[role="textbox"] {
            background-color: black;
            border-radius: 10px;
            padding: 15px;
            color: white;
        }
        
        /* Customizing the upload section */
        .stFileUploader>label {
            color: #008080;
        }

    </style>
""", unsafe_allow_html=True)

# Title of the web app
st.title("Swarnim's OCR App 📚")

# Slim container to organize layout
with st.container():
    st.write("Upload an image file for text extraction and keyword search.")

# Upload an image file
uploaded_image = st.file_uploader("📤 Upload an Image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Open the uploaded image
    image = Image.open(uploaded_image)
    
    # Display the image in a centered, modern look
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)
    
    # Perform OCR on the image
    with st.spinner("Extracting text from the image... ⏳"):
        extracted_text = pytesseract.image_to_string(image, lang='eng+hin')

    # Clean up the extracted text
    cleaned_text = extracted_text.strip()  # Remove leading/trailing whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple spaces/newlines with single spaces

    # Display the cleaned extracted text
    st.text_area("📄 Extracted Text", cleaned_text, height=300, placeholder="Extracted text will appear here...")

    # Keyword search functionality
    search_query = st.text_input("🔍 Enter a keyword to search")

    if search_query:
        if re.search(re.escape(search_query), cleaned_text, re.IGNORECASE):
            st.success(f"✅ Keyword '{search_query}' found in the extracted text.")

            # Highlight the keyword in the extracted text
            highlighted_text = re.sub(
                f"(?i)({re.escape(search_query)})",  # case-insensitive search
                r"<mark style='background-color: yellow; color: black;'>\1</mark>",  # lighter background with readable text
                cleaned_text
            )
            
            # Display the highlighted text with modern UI
            st.markdown(
                f"<div style='background-color: white; color: black; padding: 10px; line-height: 1.5; border-radius: 10px;'>{highlighted_text}</div>", 
                unsafe_allow_html=True
            )

            # Now highlight the keyword in the original image
            img_cv = np.array(image)  # Convert PIL image to OpenCV format
            img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR for OpenCV

            # Get bounding box info for each character
            data = pytesseract.image_to_data(image, lang='eng+hin', output_type=pytesseract.Output.DICT)

            # Draw rectangles around searched keyword
            n_boxes = len(data['text'])
            for i in range(n_boxes):
                if search_query.lower() in data['text'][i].lower():
                    (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
                    img_cv = cv2.rectangle(img_cv, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle

            # Convert the image back to RGB (PIL format) and display it
            img_with_highlight = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
            img_with_highlight_pil = Image.fromarray(img_with_highlight)

            st.image(img_with_highlight_pil, caption='🔍 Image with highlighted keyword', use_column_width=True)

        else:
            st.error(f"❌ Keyword '{search_query}' not found.")

# Modules to add: streamlit, opencv-python, Pillow, pytesseract, numpy