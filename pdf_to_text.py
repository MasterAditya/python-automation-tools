from pypdf import PdfReader

pdf_file = "input.pdf"
output_file = "output.txt"

reader = PdfReader(pdf_file)
text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Text extracted to '{output_file}'")
