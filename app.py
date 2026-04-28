import tkinter as tk
from tkinter import filedialog
from indexer import index_folder
from search_engine import search
from database import create_table
import os
import subprocess

create_table()

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        index_folder(folder)
        status.config(text="Indexing complete")

def update_search(*args):
    query = entry.get()
    results = search(query, filter_var.get())

    listbox.delete(0, tk.END)

    for r in results:
        listbox.insert(tk.END, r)

def open_file(event):
    selection = listbox.curselection()
    if selection:
        path = listbox.get(selection[0])
        try:
            os.startfile(path)
        except:
            subprocess.call(["open", path])

root = tk.Tk()
root.title("Search Engine PRO")
root.geometry("700x550")

tk.Button(root, text="Index Folder", command=choose_folder).pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)
entry.bind("<KeyRelease>", update_search)

filter_var = tk.StringVar(value="All")
tk.OptionMenu(root, filter_var, "All", ".py", ".txt", ".pdf").pack()

listbox = tk.Listbox(root, width=90, height=20)
listbox.pack()
listbox.bind("<Double-Button-1>", open_file)

status = tk.Label(root, text="")
status.pack()

root.mainloop()
