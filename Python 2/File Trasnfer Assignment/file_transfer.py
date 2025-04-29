import tkinter as tk
from tkinter import filedialog


class ParentWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.master.title("File Transfer")

        
        self.sourceDir_btn = tk.Button(
            text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        self.source_dir = tk.Entry(width=75)
        self.source_dir.grid(row=0, column=1, padx=(20, 10), pady=(30, 0))

        
        self.destDir_btn = tk.Button(
            text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        self.destination_dir = tk.Entry(width=75)
        self.destination_dir.grid(row=1, column=1, padx=(20, 10), pady=(15, 10))

    
    def sourceDir(self):
        selectSourceDir = filedialog.askdirectory()
        self.source_dir.delete(0, tk.END)
        self.source_dir.insert(0, selectSourceDir)

    
    def destDir(self):
        selectDestDir = filedialog.askdirectory()
        self.destination_dir.delete(0, tk.END)
        self.destination_dir.insert(0, selectDestDir)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


import tkinter as tk
from tkinter import filedialog
import shutil
import os


class ParentWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("File Transfer")

        
        self.sourceDir_btn = tk.Button(
            text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        self.source_dir = tk.Entry(width=75)
        self.source_dir.grid(row=0, column=1, padx=(20, 10), pady=(30, 0))

        
        self.destDir_btn = tk.Button(
            text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        self.destination_dir = tk.Entry(width=75)
        self.destination_dir.grid(row=1, column=1, padx=(20, 10), pady=(15, 10))

        
        self.transfer_btn = tk.Button(
            text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(20, 10), pady=(15, 10))

       
        self.exit_btn = tk.Button(
            text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=0, padx=(20, 10), pady=(15, 10))

    

    
    def sourceDir(self):
        selectSourceDir = filedialog.askdirectory()
        self.source_dir.delete(0, tk.END)
        self.source_dir.insert(0, selectSourceDir)

    
    def destDir(self):
        selectDestDir = filedialog.askdirectory()
        self.destination_dir.delete(0, tk.END)
        self.destination_dir.insert(0, selectDestDir)

    
    def transferFiles(self):
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        files = os.listdir(source)

        for file in files:
            currentFile = os.path.join(source, file)
            if os.path.isfile(currentFile):
                shutil.move(currentFile, destination)
                print(f"Moved: {file}")
        print("All eligible files have been transferred!")

    
    def exit_program(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


import os
import shutil
import datetime

class FileTransfer:
    def __init__(self, source_dir, destination_dir):
        self.source_dir = source_dir  
        self.destination_dir = destination_dir  

    def transferFiles(self):
        """
        This function transfers files that are either new or modified within the last 24 hours
        from the source directory to the destination directory.
        """
        
        current_time = datetime.datetime.now()

        
        for filename in os.listdir(self.source_dir):
            
            source_file = os.path.join(self.source_dir, filename)
            
            
            if os.path.isfile(source_file):
               
                last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(source_file))

                
                time_difference = current_time - last_modified_time

                
                if time_difference <= datetime.timedelta(days=1):
                    
                    destination_file = os.path.join(self.destination_dir, filename)

                    
                    shutil.copy2(source_file, destination_file)
                    print(f"Transferred: {filename}")
                else:
                    print(f"Skipped (not modified in the last 24 hours): {filename}")


source_folder = 'Users/mirko/OneDrive/Desktop/CustomerSource'
destination_folder = 'Users/mirko/OneDrive/Desktop/CustomerDestination'

file_transfer = FileTransfer(source_folder, destination_folder)
file_transfer.transferFiles()
