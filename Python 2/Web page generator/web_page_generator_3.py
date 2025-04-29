
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("Webpage Generator")

        
        self.custom_text = Label(self.master, text="Would you like to create custom text for your webpage?", font=("Arial", 12))
        self.custom_text.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky=N+W)

        self.txt_customText = Entry(self.master, text="", width=80)
        self.txt_customText.grid(row=1, column=0, padx=(10, 0), pady=(10, 10))

        self.btnSubmit = Button(self.master, text="Submit Custom Text", width=20, height=2, command=self.customEntry)
        self.btnSubmit.grid(row=2, column=0, padx=(10, 0), pady=(0, 10))

        self.btnDefault = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultText)
        self.btnDefault.grid(row=2, column=1, padx=(10, 0), pady=(0, 10))

    
    def customEntry(self):
        customText = self.txt_customText.get()
        htmlFile = open("user_customized.html", "w")
        htmlContent = f"<html>\n<body>\n<p>{customText}</p>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("user_customized.html")

    
    def defaultText(self):
        htmlFile = open("user_customized.html", "w")
        htmlContent = "<html>\n<body>\n<p>Stay tuned for our amazing awesome sale!</p>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("user_customized.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
