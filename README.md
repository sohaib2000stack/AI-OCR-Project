# 📄 AI-Powered OCR & PDF Processing Project 🚀

## 📌 Overview
This project allows users to **extract text** from **images and PDFs** (including scanned PDFs).  
The extracted text can also be **processed using AI for summarization and analysis**.

---

## ✅ Features
- **Extract text from Images (`.jpg`, `.png`, etc.)** using OCR.
- **Extract text from PDFs** (both selectable and scanned).
- **AI-Powered Text Processing** (Summarization and Analysis).

---

## 🚀 Installation

### **1️⃣ Install Dependencies**
Ensure you have Python installed (Python 3.7+ recommended).  
Run the following command in your terminal or command prompt:

```bash
pip install pytesseract pdf2image pypdf pdfminer.six reportlab docx transformers
```

### **2️⃣ Set Up Tesseract OCR**
Download and install **Tesseract OCR** from:  
🔗 [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

After installation, update `ocr.py` with the correct Tesseract path:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## 📂 Project Structure
```
📂 AI-OCR-Project
│── ocr.py               # Handles text extraction
│── main.py              # Runs the program & user interface
│── gen_ai.py            # AI-powered text summarization
│── requirements.txt      # List of required dependencies
│── README.md            # Project documentation
```

---

## 🚀 How to Use

### **1️⃣ Run the Main Script**
To start the program, open a terminal and run:
```bash
python main.py
```

### **2️⃣ Choose an Option**
You will be prompted to select an option:
```
Select an option:
(1) Extract text from Image
(2) Extract text from PDF
```

#### **🖼️ Extract Text from an Image**
1. Enter the **image file path**.
2. The extracted text will be displayed.

#### **📄 Extract Text from a PDF**
1. Enter the **PDF file path**.
2. If the PDF has **selectable text**, it will be extracted directly.
3. If the PDF is **scanned**, OCR will extract the text.

---

## 📌 Example Output

### **Extracted Text**
```
This is an example of extracted text from an image or PDF.
```

### **AI-Generated Summary**
```
This document discusses the properties of light and its interaction with different materials.
```

---

## 🔧 Troubleshooting

### **1️⃣ OCR Not Working?**
- Make sure **Tesseract OCR** is installed and the path is correctly set in `ocr.py`.

### **2️⃣ PDF Text Not Extracting?**
- Ensure `pdfplumber` and `pytesseract` are installed.
- Try using a different PDF file.

---

## 📜 License
This project is **open-source**. Feel free to modify and improve it! 🚀

---

## 👨‍💻 Author
Created by **[Sohaib Ul Hasan]** 😊  
```

---

### **✅ How to Save This as `README.md`**
1️⃣ Open **VS Code** or any text editor.  
2️⃣ Create a new file named **`README.md`** in your project folder.  
3️⃣ Copy and paste the above content into the file.  
4️⃣ **Save the file.**  

---

### **🚀 Now Your Project Has a Proper README!** 🎉  
Let me know if you need any more modifications! 😊
