# 📝 Textractor

**Textractor** is a Python application that converts non-searchable PDFs
into searchable PDFs using Optical Character Recognition (OCR) with
support for both **German** and **English** text. It integrates
spell-checking for extracted text using dictionaries and allows batch
processing of PDF files through a user-friendly graphical interface
(GUI).

## 🎯 Purpose

Have you ever needed to:

- Copy Text from a PDF File?
- Search for PDF files containing specific words?
- Organize you document by their content?
- Prepare a folder structure before migrating files?

**Textractor** solves these problems by scanning you PDF files in s specific PATh, extract the texts and spell check them before storing new searchable versions of the PDF files. Don't worry, PDF files with selectable texts will be ignored!

## 💡 Features

- 📄 Converts non-searchable PDFs into searchable ones.

- 🔍 Integrates **OCR** to extract text from PDF images.

- 📝 Spell-checks the extracted text using **German** and **English**
  dictionaries.

- 🖼️ Supports batch processing of PDFs within folders.

- 🔧 Easy-to-use GUI for folder selection and processing.

- 📂 Allows selecting custom output directories for processed files.

- 🗃️ Respects your folder structure by mirroring the original folder structure from the source folder.

## 🛠️ Installation

**1. Install Tesseract OCR**

_A- For Windows:_ - Download and install the least release of **Tesseract OCR Windows installer** from [UB Mannheim](https://github.com/UB-Mannheim)
[here](https://github.com/UB-Mannheim/tesseract).

_B- For MacOS:_
If you have Homebrew installed, you can install Poppler by running the following command

```bash
brew brew install tesseract

```

_C- For Linux (Ubuntu/Debian):_
Install Tesseract via APT

```bash
sudo apt-get install tesseract-ocr
```

- For installation on other os refer to the
  [original download page of **Tesseract OCR**](https://github.com/tesseract-ocr/tessdoc/blob/main/Downloads.md)

- During installation, note the installation path. You will need to
  update the path in the code.

_*Verify Installation*_ by running `tesseract -v`

**2. Update the Path in Code**

In the Textractor code, update the following line with the correct path
to the Tesseract-OCR executable (make sure the path is correct):

```python
pytesseract.pytesseract.tesseract_cmd = r\'C:\Path\To\Tesseract-OCR\tesseract.exe\'
```

On other OS (Not Windows)

```python
pytesseract.pytesseract.tesseract_cmd = 'Path/To/Tesseract-OCR/executable/'
```

**3. Download and Install Poppler**

_A- For Windows:_

Download Poppler binaries from [**Owen Schwartz**](https://github.com/oschwartz10612)
[here](https://github.com/oschwartz10612/poppler-windows/releases).

Add PATH variables for Poppler to accordingly to `poppler\bin`

_B- For MacOS:_

If you have Homebrew installed, you can install Poppler by running the following command

```bash
brew install poppler
```

_C- For Linux (Ubuntu/Debian):_

```bash
sudo apt-get install poppler-utils
```

_*Verify Installation*_ by running `pdftoppm -v`

**4. Install Required Python Packages**

Run the following command to install all necessary dependencies:

```bash
pip install pdf2image pytesseract tkinter pyenchant
```

**5. Hunspell Dictionaries Setup**

To ensure the spell-check functionality works:

A. **Install Hunspell Dictionaries**:
Download and install **Hunspell**
dictionaries for **German** (de_DE) and **English** (en_US)
languages. You can find the dictionaries
[here](https://github.com/wooorm/dictionaries).

    B. **Update the Dictionary Path** in the code: Update the path to the
      dictionaries in the following line:

      ```python
      enchant.set_param(\"enchant.myspell.dictionary.path\", r\'C:\Path\To\Hunspell\Dictionaries\')
      ```

**6. Update Environment PATH Variables**

Ensure that **Tesseract OCR**, **Hunspell**, and **Poppler** paths are included
in your system's **PATH** environment variables to allow the software to
locate them during execution.

## 🚀 How to Use

**1. Launch the Application**

Simply run the Python script using the following command:

```bash
python Textractor.py
```

**2. Select Input and Output Folders**

    - A GUI will appear where you can select the folder containing the **PDFfiles** to process.

    - Use the **\"Browse\"** button to select both **Input** and **Output**
    folders:

    - **Input Folder**: Contains the non-searchable PDF files.

    - **Output Folder**: Where the processed searchable PDFs will be saved.

**3. Start the PDF Conversion**

    - Once folders are selected, click the **\"Start Conversion\"** button.

    - The app will process each PDF in the input folder, check if it's
    non-searchable, and convert it to a searchable PDF if needed.

**4. Review the Conversion Log**

- After the conversion process is complete, a **conversion log** will be
  generated in the output folder (conversion_log.txt), containing
  details of the processing results, such as errors or successfully
  processed files.

## 🛠️ Dependencies

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

- [pdf2image](https://github.com/Belval/pdf2image)

- [pytesseract](https://pypi.org/project/pytesseract/)

- [tkinter](https://docs.python.org/3/library/tkinter.html)

- [pyenchant](https://pyenchant.github.io/pyenchant/)

- [Hunspell Dictionaries](https://github.com/wooorm/dictionaries)

## 📝 Additional Notes

- Ensure that **Tesseract OCR** and **Hunspell** dictionaries are
  correctly installed and their paths are configured in the code and
  system PATH.

  - The app currently supports OCR for both **German** and **English**
    languages. To add support for additional languages, update the OCR
    command in the code:

  ```python
  raw_text = pytesseract.image_to_string(image, lang=\"deu+eng\")
  ```

- For optimal performance, ensure your PDF files have a high-resolution
  image for accurate OCR.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for
details.

Enjoy using **Textractor** to make your PDF files searchable and
error-free with integrated spell-checking

## 🙏 Acknowledgments

- Thanks to [UB Mannheim](https://github.com/UB-Mannheim) for making **Tesseract OCR** [Windows installer](https://github.com/UB-Mannheim/tesseract)
