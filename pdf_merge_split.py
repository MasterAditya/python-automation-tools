from PyPDF2 import PdfReader, PdfWriter

# Merge PDFs
pdfs_to_merge = ["file1.pdf", "file2.pdf"]
writer = PdfWriter()
for pdf in pdfs_to_merge:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)
with open("merged.pdf", "wb") as f:
    writer.write(f)
print("Merged PDFs saved as merged.pdf")

# Split PDF example (first page)
reader = PdfReader("merged.pdf")
writer = PdfWriter()
writer.add_page(reader.pages[0])
with open("split_page1.pdf", "wb") as f:
    writer.write(f)
print("First page saved as split_page1.pdf")
