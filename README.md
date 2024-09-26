# Swarnim's OCR & Keyword Search App 📚🔍

Welcome to the Swarnim's OCR (Optical Character Recognition) & Keyword Search App. This application allows you to upload images containing text, extract the text using OCR, perform keyword searches, highlight keywords in the text and image.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the App Locally](#running-the-app-locally)
- [Deployment](#deployment)
  - [Deploying on Streamlit Cloud](#deploying-on-streamlit-cloud)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Multi-language OCR**: Supports OCR in multiple languages including English, Hindi, French, Spanish, and German.
- **Keyword Search**: Search for multiple keywords in the extracted text with options for case sensitivity and whole-word matching.
- **Text Highlighting**: Highlights found keywords in both the extracted text and the uploaded image.
- **Download Options**: Allows downloading the extracted text and the image with highlighted keywords.
- **User-friendly Interface**: Clean and modern UI with customizable options in the sidebar.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.7 or higher

## Installation

Follow these steps to set up the environment and install the necessary dependencies.

### 1. Clone the Repository

```bash
git clone https://github.com/Swarnim913/OCR.git
cd OCR
```

### 2. Create a Virtual Environment (Optional but Recommended)

#### Using `venv`

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**

```txt
streamlit
pytesseract
Pillow
opencv-python-headless
numpy
gTTS
langdetect
```

### 4. Install Tesseract OCR

#### macOS

Install via Homebrew:

```bash
brew install tesseract
brew install tesseract-lang
```

#### Ubuntu/Linux

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
sudo apt-get install tesseract-ocr-eng tesseract-ocr-hin tesseract-ocr-fra tesseract-ocr-spa tesseract-ocr-deu
```

#### Windows

Download the Tesseract installer from the [official repository](https://github.com/UB-Mannheim/tesseract/wiki). Install Tesseract and note the installation path (usually `C:\Program Files\Tesseract-OCR`).

### 5. Configure `pytesseract`

If you're on Windows or if `pytesseract` cannot find the Tesseract executable, specify the path in your code.

#### For Windows Users:

In your Python script (e.g., `app.py`), add:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### For macOS/Linux Users:

Usually, Tesseract is installed in a standard location, and `pytesseract` can find it automatically. If not, specify the path:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
```

## Running the App Locally

### 1. Start the Streamlit App

In your terminal, run:

```bash
streamlit run app.py
```

### 2. Open in Browser

After running the command, Streamlit will provide a local URL (usually `http://localhost:8501`). Open this URL in your web browser to interact with the app.

## Deployment

### Deploying on Streamlit Cloud

You can deploy the app on Streamlit Cloud to make it accessible over the internet.

#### 1. Prepare Your Repository

- Ensure your app script (e.g., `app.py`) is in the root directory.
- Include `requirements.txt` and `packages.txt` in the root directory.

**Contents of `requirements.txt`:**

```txt
streamlit
pytesseract
Pillow
opencv-python-headless
numpy
gTTS
langdetect
```

**Contents of `packages.txt`:**

```txt
tesseract-ocr
tesseract-ocr-eng
tesseract-ocr-hin
tesseract-ocr-fra
tesseract-ocr-spa
tesseract-ocr-deu
libtesseract-dev
```

#### 2. Push to GitHub

Ensure your code is pushed to a GitHub repository.

#### 3. Deploy on Streamlit Cloud

- Go to [Streamlit Cloud](https://share.streamlit.io/).
- Sign in with your GitHub account.
- Click on **"New app"** and select your repository and branch.
- Provide the path to your Python script (e.g., `app.py`).
- Click **"Deploy"**.

#### 4. Monitor Deployment

- Streamlit Cloud will install the dependencies specified in `requirements.txt` and `packages.txt`.
- Monitor the logs for any errors.
- Once deployed, your app will be accessible via a public URL provided by Streamlit.

#### 5. Common Deployment Issues

- **App Hangs on Deployment**: If the app takes too long to deploy or hangs, ensure that `requirements.txt` and `packages.txt` are correct and do not include unnecessary large packages.
- **Tesseract Not Found**: Ensure that `tesseract-ocr` and the required language data packages are specified in `packages.txt`.

## Usage

1. **Upload an Image**: Click on the uploader to select an image file (PNG, JPG, JPEG) containing text.

2. **Select OCR Language(s)**: In the sidebar, select the language(s) present in the image.

3. **Configure Keyword Search Options**:
   - **Case Sensitive Search**: Enable if you want the search to be case-sensitive.
   - **Match Whole Word Only**: Enable to match whole words only.

4. **View Extracted Text**: After uploading, the app will display the extracted text.

5. **Download Options**:
   - **Download Extracted Text**: Click the link to download the text as a `.txt` file.
   - **Download Highlighted Image**: After performing a keyword search, download the image with highlighted keywords.

6. **Perform Keyword Search**:
   - Enter one or more keywords (comma-separated) in the input box.
   - The app will search for these keywords in the extracted text.
   - Found keywords will be highlighted in the text and the image.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.