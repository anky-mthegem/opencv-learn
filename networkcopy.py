import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def copy_file():
    source_path = source_entry.get()
    destination_path = destination_entry.get()
    
    try:
        shutil.copy(source_path, destination_path)
        messagebox.showinfo("Success", "File copied successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy file: {e}")

def browse_source():
    source_path = filedialog.askopenfilename()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_path)

def browse_destination():
    destination_path = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, destination_path)

# Create the main window
root = tk.Tk()
root.title("File Copier")

# Create and place widgets
source_label = tk.Label(root, text="Source File Path:")
source_label.grid(row=0, column=0, padx=10, pady=10)

source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=10, pady=10)

source_button = tk.Button(root, text="Browse", command=browse_source)
source_button.grid(row=0, column=2, padx=10, pady=10)

destination_label = tk.Label(root, text="Destination Folder:")
destination_label.grid(row=1, column=0, padx=10, pady=10)

destination_entry = tk.Entry(root, width=50)
destination_entry.grid(row=1, column=1, padx=10, pady=10)

destination_button = tk.Button(root, text="Browse", command=browse_destination)
destination_button.grid(row=1, column=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy", command=copy_file)
copy_button.grid(row=2, column=1, pady=20)

# Add email label in the bottom-right corner
email_label = tk.Label(root, text="amanr@godrej.com", anchor="e")
email_label.grid(row=3, column=2, padx=10, pady=10, sticky="e")

# Start the Tkinter event loop
root.mainloop()