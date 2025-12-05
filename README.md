# 🐍 Python Automation Tools

A collection of reliable Python scripts for automating repetitive tasks. Perfect for freelancers who need quick, efficient solutions to streamline workflows.

---

## 📖 About This Project

The **Python Automation Tools** repository provides a curated set of lightweight, battle-tested scripts to handle common automation needs.  
Whether you're managing files, processing documents, scraping data, or sending communications, these tools save hours of manual work.

**Use Cases:**
- **File Management:** Bulk rename or organize files for client deliverables.
- **Document Processing:** Extract text from PDFs or merge reports for analysis.
- **Data Collection:** Scrape web content and export to CSV for research or reporting.
- **Communication Automation:** Send personalized emails in bulk.
- **Data Cleaning:** Standardize Excel sheets for dashboards or audits.

---

## ✨ Core Features

- **Modular Scripts:** Each tool is self-contained, easy to customize, and runs independently.
- **Minimal Dependencies:** Leverages popular libraries like Pandas, BeautifulSoup, and PyPDF2 for broad compatibility.
- **Command-Line Ready:** Simple execution with optional arguments for flexibility.
- **Error Handling:** Built-in logging and validation to prevent crashes on edge cases.
- **Cross-Platform:** Works on Windows, macOS, and Linux with Python 3.8+.

---

## 📂 Project Structure

```
python-automation-tools/
├── rename_files.py     # Sequential file renaming utility
├── pdf_to_text.py      # PDF text extraction to TXT
├── pdf_merge_split.py  # PDF merging and splitting tool
├── web_scraper.py      # Basic web data scraper to CSV
├── email_sender.py     # Templated email sender
├── excel_cleaner.py    # Excel data cleaning and formatting
├── .gitignore          # Standard Git ignores
└── README.md           # This documentation file
```

---

## 🛠 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/python-automation-tools.git
cd python-automation-tools
```

### 2. Install Dependencies

Create a virtual environment for isolation:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:

```bash
pip install pypdf2 requests beautifulsoup4 pandas openpyxl
```

### 3. Run the Scripts

Each script can be executed directly. Most accept command-line arguments—check inline docstrings with `python script.py --help`.

```bash
# Example runs
python rename_files.py --folder /path/to/files
python pdf_to_text.py --input document.pdf --output text.txt
python pdf_merge_split.py --merge file1.pdf file2.pdf --output combined.pdf
python web_scraper.py --url https://example.com --output data.csv
python email_sender.py --template email.html --recipients recipients.csv
python excel_cleaner.py --input messy.xlsx --output clean.xlsx
```

💡 **Pro Tip:** Customize paths and add logging with `--verbose` where supported for debugging.

---

## 🔧 Script Details

| Script              | Description                                      | Key Dependencies          | Usage Example |
|---------------------|--------------------------------------------------|---------------------------|---------------|
| **rename_files.py** | Renames files in a folder sequentially (e.g., `file_0.ext`). | `os`, `glob`             | `python rename_files.py --folder ./images` |
| **pdf_to_text.py**  | Extracts all text from a PDF and saves to TXT.   | `PyPDF2`                 | `python pdf_to_text.py --input report.pdf` |
| **pdf_merge_split.py** | Merges multiple PDFs or splits into individual pages. | `PyPDF2`              | `python pdf_merge_split.py --split big.pdf` |
| **web_scraper.py**  | Scrapes table/text from a URL and exports to CSV.| `requests`, `beautifulsoup4` | `python web_scraper.py --url https://site.com/table` |
| **email_sender.py** | Sends templated emails via SMTP (Gmail/Outlook). | `smtplib`, `email`       | `python email_sender.py --config config.ini` |
| **excel_cleaner.py**| Removes duplicates, formats columns, and validates data in Excel. | `pandas`, `openpyxl` | `python excel_cleaner.py --sheet sales_data` |

---

## 💻 Tech Stack

| Library/Tool | Role                                      |
|--------------|-------------------------------------------|
| **PyPDF2**   | PDF reading, merging, and text extraction  |
| **requests** | HTTP requests for web scraping            |
| **BeautifulSoup** | HTML/XML parsing for data extraction     |
| **pandas**   | Data manipulation and CSV/Excel handling  |
| **openpyxl** | Excel file reading/writing                |
| **smtplib**  | Email sending via SMTP                    |

---

## 🤝 Contributing

Contributions welcome! Fork the repo, add enhancements (e.g., new scripts or features), and submit a pull request.  
For issues or ideas, open a discussion.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
