import tkinter as tk
from tkinter import filedialog

# Fuction to load a geotiff file

def load_file():
    # Create a Tkinter root window (it won't be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.call('wm', 'attributes', '.', '-topmost', True)  # Bring the file dialog to the front
    
    # Open the file dialog to select geotiff file
    file_path = filedialog.askopenfilename(
        title="Select a geotiff file",
        filetypes=[
            ("geotiff", "*.tif"),
            ("All files", "*.*")
        ]
    )
    if file_path:        
        print(f"Selected file: {file_path}")
        return file_path

def load_folder():
    # Create a Tkinter root window (it won't be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.call('wm', 'attributes', '.', '-topmost', True)  # Bring the file dialog to the front
    
    # Open the file dialog to select geotiff folder
    folder_path = filedialog.askdirectory()

    print(f"Selected folder: {folder_path}")
    return folder_path