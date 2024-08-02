import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from PIL import Image

class main_app:
    def __init__(self, **kwargs):
        self.root = tk.Tk()
        self.root.title("PNG into ICO")
        self.root.config(bg="black")

        self.layout()

    def layout(self):
        self.input_text_label = tk.Label(self.root,
                                         text="input file name",
                                         bg="black",
                                         fg="white")
        self.output_text_label = tk.Label(self.root,
                                          text="output file name",
                                          bg="black",
                                          fg="white")
        self.input_files_button = tk.Button(self.root,
                                            text="input file",
                                            bg="black",
                                            fg="white",
                                            width=20,
                                            command=self.open_image)
        self.output_files_button = tk.Button(self.root,
                                             text="output file",
                                             bg="black",
                                             fg="white",
                                             width=20,
                                             command=self.convert_image)

        self.input_text_label.grid(row=0, column=0)
        self.output_text_label.grid(row=1, column=0)
        self.input_files_button.grid(row=0, column=1)
        self.output_files_button.grid(row=1, column=1)

    def open_image(self):
        filetypes = (
            ('png files', '*.png'),
            ('all files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='\\',
            filetypes=filetypes
        )

        showinfo(
            title='Selected File',
            message=filename
        )

        self.image_path = filename
        self.image_destination = self.image_path.replace(".png", ".ico")

    def convert_image(self):
        main_image = Image.open(self.image_path)
        main_image.save(self.image_destination, format="ICO")

        showinfo(
            title='File successfully converted',
            message=self.image_destination
        )

if __name__ == "__main__":
    app = main_app()
    app.root.mainloop()
