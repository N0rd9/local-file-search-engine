import difflib
from database import get_all_files

def search(query, file_type="All"):
    query = query.lower()
    results = []

    for name, path, ext in get_all_files():

        if file_type != "All" and ext != file_type:
            continue

        if query == name:
            score = 100
        elif query in name:
            score = 70 + name.count(query)
        else:
            score = int(difflib.SequenceMatcher(None, query, name).ratio() * 50)

        if score > 20:
            results.append((score, path))

    results.sort(reverse=True)
    return [path for score, path in results[:100]]
