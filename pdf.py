import customtkinter as ctk
from PyPDF2 import PdfReader, PdfWriter
from tkinter.filedialog import askopenfilenames, asksaveasfilename

input_str = " "
output_str = " "
input_label_path = " "
output_label_path = " "
merge_complete = " "

def merge_and_compress(input, output):
    writer = PdfWriter()
    for pdf in input:
        reader = PdfReader(pdf)
        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)
        writer.add_metadata(reader.metadata)
        writer.remove_links()
    with open(output, "wb") as f:
        writer.write(f)
    merge_complete.configure(text="Pdfs merged")

def input_to_str():
    global input_str , input_label_path
    input_str = askopenfilenames(initialdir="/", title="Select file",
                     filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    input_label_path.configure(text=input_str)
def output_to_str():
    global output_str, output_label_path
    output_str = asksaveasfilename(initialdir="/", title="Save file",
                    filetypes=(("txt files", "*.pdf"),("all files", "*.*")))
    output_label_path.configure(text=output_str)
def main():
    global input_str,output_str, input_label_path, output_label_path, merge_complete
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("merge and compress pdf's")
    root.geometry("500x500")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady="20",padx="20", fill="both", expand=True)

    input_label = ctk.CTkLabel(master=frame, text="Input paths:")
    input_button = ctk.CTkButton(master=frame, text="Select Pdf files", command=lambda: input_to_str())
    input_label_path = ctk.CTkLabel(master=frame, text="Choose source file(s)")
    input_label.pack(padx="5",pady="5")
    input_button.pack(padx="5",pady="5")
    input_label_path.pack()

    output_label = ctk.CTkLabel(master=frame, text="Iutput paths:")
    output_button = ctk.CTkButton(master=frame, text="Select output", command=lambda: output_to_str())
    output_label_path = ctk.CTkLabel(master=frame, text="Choose file destination")
    output_label.pack(padx="5",pady="5")
    output_button.pack(padx="5",pady="5")
    output_label_path.pack()

    merge_button = ctk.CTkButton(master=root, text="Merge PDFs", command=lambda: merge_and_compress(input_str, output_str))
    merge_complete = ctk.CTkLabel(master = root, text=" :) ")
    merge_button.pack(padx="15",pady="15")
    merge_complete.pack(padx="15",pady="15")
    root.mainloop()

if __name__ == "__main__":
  main()
