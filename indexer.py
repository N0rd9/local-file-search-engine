import os
from database import insert_file

def index_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            ext = os.path.splitext(file)[1]

            insert_file(file.lower(), path, ext)
