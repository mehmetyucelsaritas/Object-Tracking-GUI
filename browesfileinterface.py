from tkinter import *
from tkinter import filedialog


class FileDialog:
    def __init__(self):
        self.filepath = ""
        self.window = Tk()
        self.window.title("NeuroLab Tracking Gui")
        self.window.configure(background="#f7f5dd")

        self.logo_image = PhotoImage(file=".\\images\\NeuroLab Logo.png")
        self.background_image = PhotoImage(file=".\\images\\background.png")
        self.canvas = Canvas(width=200, height=224, background="#f7f5dd", highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.logo_image)
        self.canvas.create_image(200,224, image=self.background_image)
        self.canvas.grid(column=0, row=0, padx=20)

        self.file_select_button = Button(text="Browse Files", highlightthickness=0, command=self.browse_files)
        self.file_select_button.configure(background="#f7f5dd")
        self.file_select_button.grid(column=0, row=1, pady=10)

        self.window.mainloop()

    def browse_files(self):
        """
        It assigns the selected file path to filepath variable

        :return: empty
        """
        self.filepath = filedialog.askopenfilename(initialdir="/",
                                                   title="Select a File",
                                                   filetypes=(("Video Files", "*.avi*"),
                                                              ("Excel Files", "*.xlsx*"),
                                                              ("All Files", "*.*")))
        self.window.destroy()


