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

**Textractor** solves these problems by scanning you PDF file in s specific PATh, exact the texts and spell check them before storing new searchable versions of the PDF files. Don't worry, PDF files with selectable texts will be ignored

## 💡 Features

- 📄 Converts non-searchable PDFs into searchable ones.

- 🔍 Integrates **OCR** to extract text from PDF images.

- 📝 Spell-checks the extracted text using **German** and **English**
  dictionaries.

- 🖼️ Supports batch processing of PDFs within folders.

- 🔧 Easy-to-use GUI for folder selection and processing.

- 📂 Allows selecting custom output directories for processed files.

- 🗃️ Respects your folder structure by mirorring the original folder structure from the source folder.

## 🛠️ Installation

**1. Install Tesseract OCR**

- Download and install **Tesseract OCR** from
  [here](https://github.com/tesseract-ocr/tesseract).

- During installation, note the installation path. You will need to
  update the path in the code.

**2. Update the Path in Code**

In the Textractor code, update the following line with the correct path
to the Tesseract-OCR executable (make sure the path is correct):

```python
pytesseract.pytesseract.tesseract_cmd = r\'C:\Path\To\Tesseract-OCR\tesseract.exe\'
```

**3. Install Required Python Packages**

Run the following command to install all necessary dependencies:

```bash
pip install pdf2image pytesseract tkinter pyenchan
```

t

**4. Hunspell Dictionaries Setup**

To ensure the spell-check functionality works:

A. **Install Hunspell Dictionaries**: Download and install **Hunspell**
dictionaries for **German** (de_DE) and **English** (en_US)
languages. You can find the dictionaries
[here](https://github.com/wooorm/dictionaries).

B. **Update the Dictionary Path** in the code: Update the path to the
dictionaries in the following line:

```python
enchant.set_param(\"enchant.myspell.dictionary.path\", r\'C:\Path\To\Hunspell\Dictionaries\')
```

**5. Update Environment PATH Variables**

Ensure that both **Tesseract OCR** and **Hunspell** paths are included
in your system's PATH environment variables to allow the software to
locate them during execution.

## 🚀 How to Use

**1. Launch the Application**

Simply run the Python script using the following command:

```bash
python Textractor.py
```

**2. Select Input and Output Folders**

- A GUI will appear where you can select the folder containing the **PDF
  files** to process.

- Use the **\"Browse\"** button to select both **Input** and **Output**
  folders:

  - **Input Folder**: Contains the non-searchable PDF files.

  - **Output Folder**: Where the processed searchable PDFs will be
    saved.

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

  ````python
  raw_text = pytesseract.image_to_string(image, lang=\"deu+eng\")   ```

  ````

- For optimal performance, ensure your PDF files have a high-resolution
  image for accurate OCR.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for
details.

Enjoy using **Textractor** to make your PDF files searchable and
error-free with integrated spell-checking
