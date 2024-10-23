import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
from datetime import datetime
import enchant  # For spell checking

# Path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust the path as needed

# Path to Hunspell dictionaries
enchant.set_param("enchant.myspell.dictionary.path", r"C:\Users\MALA154\hunspell") # Adjust the path as needed

# Initialize dictionaries for English and German
english_dict = enchant.Dict("en_US")
german_dict = enchant.Dict("de_DE")

# GUI Application
def select_folders():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        input_folder.set(folder_selected)

def select_output_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_folder.set(folder_selected)

def process_pdfs():
    input_dir = input_folder.get()
    output_dir = output_folder.get()

    if not input_dir or not output_dir:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return

    # Create a log file
    log_file = os.path.join(output_dir, "conversion_log.txt")
    with open(log_file, "w") as log:
        log.write(f"Conversion Log - {datetime.now()}\n\n")

        for foldername, subfolders, filenames in os.walk(input_dir):
            for filename in filenames:
                if filename.endswith('.pdf'):
                    file_path = os.path.join(foldername, filename)
                    log.write(f"Processing: {file_path}\n")
                    try:
                        # Open the PDF file and check if it's non-searchable
                        with open(file_path, 'rb') as pdf_file:
                            pdf_reader = PdfReader(pdf_file)
                            if pdf_reader.is_encrypted:
                                log.write("  Skipping encrypted PDF.\n")
                                continue

                            # Check for non-searchable PDFs by analyzing the content
                            text_found = False
                            for page_num in range(len(pdf_reader.pages)):
                                page = pdf_reader.pages[page_num]
                                text = page.extract_text()
                                if text and text.strip():  # If any page contains text, it is searchable
                                    text_found = True
                                    break

                            if text_found:
                                log.write("  PDF is already searchable. Skipping...\n")
                            else:
                                # Convert non-searchable PDF to searchable PDF
                                convert_pdf_to_searchable(file_path, output_dir, log)

                    except Exception as e:
                        log.write(f"  Error: {e}\n")
                        continue

        messagebox.showinfo("Process Complete", "PDF conversion completed.")
        
def convert_pdf_to_searchable(file_path, output_dir, log):
    try:
        # Convert PDF pages to images
        images = convert_from_path(file_path)

        # Create a new PDF to write searchable text
        pdf_writer = PdfWriter()

        for img_index, image in enumerate(images):
            # Perform OCR on the image to extract raw text
            raw_text = pytesseract.image_to_string(image, lang="deu+eng")  # OCR for both German and English

            # Run spell check on the extracted text
            corrected_text = spell_check(raw_text)

            # Convert the corrected text back to PDF format
            pdf_page = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')

            # Add the corrected PDF page to the writer
            pdf_writer.add_page(PdfReader(BytesIO(pdf_page)).pages[0])

        # Construct the output file path
        relative_path = os.path.relpath(file_path, os.path.dirname(file_path))
        output_file_path = os.path.join(output_dir, relative_path)
        output_dir_path = os.path.dirname(output_file_path)

        if not os.path.exists(output_dir_path):
            os.makedirs(output_dir_path)

        # Write the new searchable PDF
        with open(output_file_path, 'wb') as f_out:
            pdf_writer.write(f_out)

        log.write(f"  Converted and saved to: {output_file_path}\n")
    
    except Exception as e:
        log.write(f"  Error during conversion: {e}\n")

# Spell Check Function
def spell_check(text):
    corrected_text = []
    words = text.split()

    for word in words:
        # Check if word is valid in either English or German
        if english_dict.check(word) or german_dict.check(word):
            corrected_text.append(word)  # Keep the original word if valid
        else:
            # Suggest the most likely correction from either dictionary
            suggestions = english_dict.suggest(word) + german_dict.suggest(word)
            if suggestions:
                corrected_text.append(suggestions[0])  # Use the first suggestion
            else:
                corrected_text.append(word)  # If no suggestions, keep the original word

    return ' '.join(corrected_text)

# GUI Setup
root = tk.Tk()
root.title("PDF Searchable Text Converter")

input_folder = tk.StringVar()
output_folder = tk.StringVar()

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Select Input Folder:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(frame, textvariable=input_folder, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Browse", command=select_folders).grid(row=0, column=2, padx=5, pady=5)

tk.Label(frame, text="Select Output Folder:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(frame, textvariable=output_folder, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=5, pady=5)

tk.Button(root, text="Start Conversion", command=process_pdfs).pack(pady=10)

root.mainloop()
