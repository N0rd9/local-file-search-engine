import os
import tkinter as tk
from tkinter import filedialog
import difflib
import subprocess

file_index = []

# ------------------ INDEXING ------------------

def index_files(folder):
    global file_index
    file_index = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_index.append({
                "name": file.lower(),
                "path": os.path.join(root, file),
                "ext": os.path.splitext(file)[1]
            })

    status_label.config(text=f"Indexed {len(file_index)} files")

# ------------------ SEARCH ------------------

def search_files(query, file_type):
    query = query.lower()
    results = []

    for file in file_index:
        if file_type != "All" and file["ext"] != file_type:
            continue

        name = file["name"]

        # Exact match
        if query == name:
            score = 100
        # Partial match
        elif query in name:
            score = 70 + name.count(query)
        else:
            # Fuzzy match
            ratio = difflib.SequenceMatcher(None, query, name).ratio()
            score = int(ratio * 50)

        if score > 20:
            results.append((score, file))

    results.sort(reverse=True, key=lambda x: x[0])
    return [file for score, file in results]

# ------------------ UI ------------------

def update_search(*args):
    query = search_entry.get()
    file_type = filter_var.get()

    listbox.delete(0, tk.END)

    if not query:
        return

    results = search_files(query, file_type)

    for file in results[:100]:
        listbox.insert(tk.END, file["path"])

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)
        index_files(folder)

def open_file(event):
    selection = listbox.curselection()
    if selection:
        path = listbox.get(selection[0])
        try:
            os.startfile(path)  # Windows
        except:
            subprocess.call(["open", path])  # Mac/Linux

# ------------------ UI SETUP ------------------

root = tk.Tk()
root.title("File Search Engine PRO")
root.geometry("700x550")

# Folder selection
folder_entry = tk.Entry(root, width=50)
folder_entry.pack(pady=5)
folder_entry.insert(0, "C:/")

tk.Button(root, text="Choose Folder", command=choose_folder).pack(pady=5)

# Search
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=10)
search_entry.bind("<KeyRelease>", update_search)

# Filter
filter_var = tk.StringVar(value="All")
filter_menu = tk.OptionMenu(root, filter_var, "All", ".txt", ".py", ".pdf")
filter_menu.pack()

# Results
listbox = tk.Listbox(root, width=90, height=20)
listbox.pack(pady=10)
listbox.bind("<Double-Button-1>", open_file)

# Status
status_label = tk.Label(root, text="Select folder to index")
status_label.pack()

root.mainloop()
