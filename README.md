# Swarnim's OCR & Keyword Search App 📚🔍

This is a Streamlit-based web application that performs Optical Character Recognition (OCR) on uploaded images, detects text, and allows users to search for keywords within the extracted text. Additionally, the app supports multiple languages for OCR, provides text highlighting, and offers options to download both the extracted text and an image with highlighted keywords.

## Features

- **Multilingual OCR**: Supports multiple languages (English, Hindi, French, Spanish, German) for text extraction.
- **Keyword Search**: Search for specific keywords in the extracted text, with options for case-sensitive search and matching whole words only.
- **Text Highlighting**: Highlights keywords in both the extracted text and the original image.
- **Downloadable Outputs**: Users can download the extracted text as a `.txt` file and the highlighted image as a `.png` file.
- **Detected Language**: Automatically detects the language of the extracted text.
- **Customizable Options**: Users can configure OCR languages and search options via a sidebar.

## Deployment on Streamlit Cloud

Follow these steps to deploy the app on **Streamlit Cloud**:

### Step 1: Prepare Your Repository

Ensure that your project includes the following files:

1. `app.py` – The main Python file containing the Streamlit app.
2. `requirements.txt` – A file listing all Python dependencies required for the app.
3. `packages.txt` – A file listing the system-level dependencies (for example, Tesseract).

### Step 2: Create `requirements.txt`

Add the following to `requirements.txt` to ensure all necessary Python libraries are installed:

```txt
streamlit
opencv-python-headless
Pillow
pytesseract
numpy
gTTS
langdetect
```

> **Note**: Use `opencv-python-headless` instead of `opencv-python` as it’s better suited for deployment in headless environments like Streamlit Cloud.

### Step 3: Create `packages.txt`

The `packages.txt` file is required to install system-level dependencies. Add the following to `packages.txt` to ensure that Tesseract and other required libraries are installed:

```txt
tesseract-ocr
tesseract-ocr-eng
tesseract-ocr-hin
tesseract-ocr-fra
tesseract-ocr-spa
tesseract-ocr-deu
libtesseract-dev

```

This will ensure that Tesseract is available on your Streamlit Cloud instance.

### Step 4: Deploy to Streamlit Cloud

1. Push the project to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in.
3. Click on **New app** and connect your GitHub repository.
4. Select the branch and the app file (e.g., `app.py`).
5. Click **Deploy**.

Streamlit Cloud will automatically install the dependencies listed in `requirements.txt` and `packages.txt`.

## App Structure

### Sidebar Options
- **OCR Languages**: Select one or more languages for the OCR process (default is English).
- **Keyword Search Options**:
  - **Case Sensitive**: Toggle to enable case-sensitive keyword search.
  - **Whole Word Only**: Toggle to search for whole words only.

### Main UI
- **Image Upload**: Upload an image (PNG, JPG, JPEG) for text extraction.
- **Extracted Text Display**: View the extracted text in a scrollable text box.
- **Detected Language**: Automatically detects the language of the extracted text.
- **Keyword Search**: Enter keywords (comma-separated) to search for them in the extracted text.
- **Keyword Highlighting**: Keywords are highlighted in both the extracted text and the image.

### Downloadable Outputs
- **Download Extracted Text**: Download the extracted text as a `.txt` file.
- **Download Highlighted Image**: Download the image with highlighted keywords as a `.png` file.

## Additional Information

- **Custom Tesseract Configuration**: The app uses Tesseract’s `--oem 3` and `--psm 6` configuration for better accuracy in text extraction.
- **Highlighting in Images**: The app draws green rectangles around the keywords found in the image using OpenCV.

## Modules Used

- `streamlit`: For building the web application interface.
- `Pillow`: For handling image operations.
- `pytesseract`: For performing Optical Character Recognition (OCR).
- `opencv-python`: For processing and highlighting text in the uploaded image.
- `numpy`: For image manipulation with OpenCV.
- `gTTS`: (Optional) For converting the extracted text to speech.
- `langdetect`: For detecting the language of the extracted text.
- `re`: For regular expressions used in keyword search and text highlighting.
- `base64`: For encoding images and text for downloading.

## Future Improvements

- Support for more OCR languages.
- Integration with cloud services for large-scale OCR processing.
- Advanced text analytics such as sentiment analysis on the extracted text.


