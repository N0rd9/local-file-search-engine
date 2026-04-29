# Local File Search Engine

A modular desktop file search system that indexes folders, stores file metadata in SQLite, and retrieves results through real-time fuzzy matching. The project is structured as a small system design exercise with clear separation between the UI, indexer, database, and search logic.

## Features

- Index local folders
- Persist indexed files with SQLite
- Search in real time as the query changes
- Use fuzzy matching for more flexible results
- Filter by file type
- Open files directly from the results list
- Keep UI, indexing, search, and storage logic separated

## Architecture

```text
Tkinter UI
   |
   +-- Indexer: scans folders and records file paths
   |
   +-- Database: stores indexed files in SQLite
   |
   +-- Search Engine: ranks and filters matches
```

## Tech Stack

- Python
- Tkinter
- SQLite
- difflib

## Run

```bash
python app.py
```

## What It Demonstrates

- Modular application structure
- Persistent indexing
- Desktop UI events
- Local search workflows
- Basic ranking and fuzzy matching
