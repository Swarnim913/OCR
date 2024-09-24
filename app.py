import streamlit as st
from PIL import Image, ImageDraw
import pytesseract
import re
import cv2
import numpy as np

# If Tesseract is installed in a non-default location
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Title of the web app
st.title("OCR and Document Search Web Application")

# Upload an image file
uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Open the uploaded image
    image = Image.open(uploaded_image)
    
    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Perform OCR on the image
    st.write("Extracting text from the image...")
    extracted_text = pytesseract.image_to_string(image, lang='eng+hin')

    # Clean up the extracted text
    cleaned_text = extracted_text.strip()  # Remove leading/trailing whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple spaces/newlines with single spaces

    # Display the cleaned extracted text
    st.text_area("Extracted Text", cleaned_text, height=300)

    # Keyword search functionality
    search_query = st.text_input("Enter a keyword to search")

    if search_query:
        if re.search(re.escape(search_query), cleaned_text, re.IGNORECASE):
            st.write(f"Keyword '{search_query}' found in the extracted text.")
            
            # Highlight the keyword in the extracted text
            highlighted_text = re.sub(
                f"(?i)({re.escape(search_query)})",  # case-insensitive search
                r"<mark style='background-color: yellow; color: black;'>\1</mark>",  # lighter background with readable text
                cleaned_text
            )
            
            # Display the highlighted text
            st.markdown(f"<div style='background-color: white; color: black; padding: 10px; line-height: 1.5;'>{highlighted_text}</div>", unsafe_allow_html=True)

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

            st.image(img_with_highlight_pil, caption='Image with highlighted keyword', use_column_width=True)

        else:
            st.write(f"Keyword '{search_query}' not found.")
