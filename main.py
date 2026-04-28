import os
import tkinter as tk

# ------------------ INDEXING ------------------

file_index = []

def index_files(folder):
    global file_index
    file_index = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_index.append({
                "name": file.lower(),
                "path": os.path.join(root, file)
            })

# ------------------ SEARCH ------------------

def search_files(query):
    query = query.lower()
    results = []

    for file in file_index:
        if query in file["name"]:
            score = file["name"].count(query)
            results.append((score, file))

    results.sort(reverse=True, key=lambda x: x[0])
    return [file for score, file in results]

# ------------------ UI ------------------

def run_search():
    query = entry.get()
    results = search_files(query)

    listbox.delete(0, tk.END)

    for file in results[:50]:
        listbox.insert(tk.END, file["path"])

def choose_folder():
    folder = folder_entry.get()
    index_files(folder)
    status_label.config(text="Indexed!")

root = tk.Tk()
root.title("Local File Search Engine")
root.geometry("600x500")

# Folder input
folder_entry = tk.Entry(root, width=50)
folder_entry.pack(pady=10)
folder_entry.insert(0, "C:/")  # change if needed

tk.Button(root, text="Index Files", command=choose_folder).pack()

# Search
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

tk.Button(root, text="Search", command=run_search).pack()

# Results
listbox = tk.Listbox(root, width=80, height=20)
listbox.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
