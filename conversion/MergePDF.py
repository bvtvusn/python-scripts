import PyPDF2

def merge_pdfs(paths, output):
    merger = PyPDF2.PdfMerger()
    for path in paths:
        merger.append(path)
    merger.write(output)
    merger.close()

# List of PDF files to merge
pdf_files = [r"C:\Users\hrm\Downloads\reddit.pdf",r"C:\Users\hrm\Downloads\PDFCHAIN.pdf"]
#pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

# Output file name
output_file = r"C:\Users\hrm\Downloads\outputPDF.pdf"

# Merge PDFs
merge_pdfs(pdf_files, output_file)

print("PDFs merged successfully!")
