import tkinter as tk
from tkinter import filedialog
import os
import PyPDF2

class PDFFileMergingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF File Merging App")

        self.file_paths = []
        
        self.btn_open_files = tk.Button(self.master, text="Open Files", command=self.open_files)
        self.btn_open_files.pack(pady=1)
        
        self.text_area = tk.Text(self.master, height=10, width=50, wrap=tk.NONE)
        self.text_area.pack(pady=3, padx=10, fill=tk.BOTH, expand=True)
        
        self.btn_move_up = tk.Button(self.master, text="Move Up", command=self.move_up)
        self.btn_move_up.pack(side=tk.LEFT, padx=5)
        
        self.btn_move_down = tk.Button(self.master, text="Move Down", command=self.move_down)
        self.btn_move_down.pack(side=tk.LEFT, padx=5)
        
        self.btn_merge_pdfs = tk.Button(self.master, text="Merge PDFs", command=self.merge_pdfs)
        self.btn_merge_pdfs.pack()

    def open_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        
        for file_path in file_paths:
            self.file_paths.append(file_path)
            self.text_area.insert(tk.END, file_path + "\n")
            
    def move_up(self):
        current_index = self.text_area.index(tk.INSERT)
        if current_index != "1.0":
            current_line = int(current_index.split('.')[0])
            prev_line = current_line - 1
            self.swap_lines(current_line, prev_line)
        
    def move_down(self):
        current_index = self.text_area.index(tk.INSERT)
        line_count = int(self.text_area.index(tk.END).split('.')[0])
        if current_index != "{}.0".format(line_count):
            current_line = int(current_index.split('.')[0])
            next_line = current_line + 1
            self.swap_lines(current_line, next_line)
            
    def swap_lines(self, line1, line2):
        lines = self.text_area.get("1.0", tk.END).split("\n")
        lines[line1 - 1], lines[line2 - 1] = lines[line2 - 1], lines[line1 - 1]
        new_lines = [line for line in lines if line.strip()]  # Remove empty lines
        new_text = "\n".join(new_lines)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", new_text)
        self.text_area.mark_set(tk.INSERT, "{}.0".format(line2))
        
    def merge_pdfs(self):
        # Get content of text area
        text_area_content = self.text_area.get("1.0", tk.END)
        
        # Check if any paths are present
        if not text_area_content.strip():
            tk.messagebox.showerror("Error", "No PDFs to merge.")
            return
        
        # Split content into lines and remove empty lines
        lines = [line.strip() for line in text_area_content.split("\n") if line.strip()]
        invalid_files = []
        non_existing_files = []
        
        # Check validity of each file
        for i, path in enumerate(lines, start=1):
            if not os.path.isfile(path):
                non_existing_files.append(i)
            elif not path.lower().endswith('.pdf'):
                invalid_files.append(i)
        
        # Generate error message
        error_message = ""
        if non_existing_files:
            error_message += "Files do not exist on lines: {}\n".format(", ".join(map(str, non_existing_files)))
        if invalid_files:
            error_message += "Invalid PDF files on lines: {}\n".format(", ".join(map(str, invalid_files)))
        
        # Show error message if there are invalid files
        if error_message:
            tk.messagebox.showerror("Error", error_message)
            return
        
        # Open save file dialog
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_file:
            # Merge PDFs
            merge_pdfs_from_text_area(text_area_content, output_file)
            tk.messagebox.showinfo("Success", "PDFs merged successfully!")

def merge_pdfs_from_text_area(text_area_content, output):
    merger = PyPDF2.PdfMerger()
    paths = text_area_content.strip().split("\n")
    for path in paths:
        if os.path.isfile(path.strip()) and path.strip().lower().endswith('.pdf'):
            merger.append(path.strip())
    merger.write(output)
    merger.close()

def main():
    root = tk.Tk()
    app = PDFFileMergingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
