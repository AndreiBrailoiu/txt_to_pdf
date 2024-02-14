import tkinter as tk
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(tk.END, file_path)

def convert_to_pdf():
    input_file = input_file_entry.get()
    if not input_file:
        status_label.config(text="Please select a text file first")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_file:
        try:
            with open(input_file, 'r') as f:
                content = f.readlines()

            doc = SimpleDocTemplate(output_file, pagesize=letter)
            styles = getSampleStyleSheet()
            flowables = []

            for line in content:
                # Calculate indentation based on the number of leading spaces
                indentation = 0
                for char in line:
                    if char == ' ':
                        indentation += 1
                    else:
                        break

                # Add the line with the calculated indentation
                paragraph = Paragraph('&nbsp;' * indentation + line[indentation:], styles["Normal"], encoding='utf8')
                flowables.append(paragraph)

            doc.build(flowables)

            status_label.config(text="Conversion completed successfully!", fg="green")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}", fg="red")

# Create the main window
root = tk.Tk()
root.title("Text to PDF Converter")

# Create input file selection components
input_file_label = tk.Label(root, text="Select Text File:")
input_file_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=5, pady=5)

select_file_button = tk.Button(root, text="Browse", command=select_file)
select_file_button.grid(row=0, column=2, padx=5, pady=5)

# Create convert to PDF button
convert_button = tk.Button(root, text="Convert to PDF", command=convert_to_pdf)
convert_button.grid(row=1, column=1, padx=5, pady=5)

# Create a label for displaying status
status_label = tk.Label(root, text="", fg="black")
status_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()