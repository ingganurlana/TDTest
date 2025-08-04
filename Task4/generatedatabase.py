import xml.etree.ElementTree as ET
import sqlite3
from pathlib import Path


# Parse the XML file
tree = ET.parse(Path(__file__).with_name('example_file.xml'))
root = tree.getroot()

# Connect to SQLite (or create it)
conn = sqlite3.connect(Path(__file__).with_name('books.db'))
cursor = conn.cursor()

# Create a table (adjust as needed)
cursor.execute('''
CREATE TABLE IF NOT EXISTS book (
    title TEXT,
    author TEXT,
    genre TEXT,
    year TEXT,
    publisher TEXT
    
)
''')

# Insert data
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    genre = book.find('genre').text
    year = book.find('year').text
    publisher = book.find('publisher').text

    cursor.execute('''
    INSERT OR REPLACE INTO book (title, author, genre, year, publisher) VALUES (?, ?, ?, ?, ?)
    ''', (title, author, genre, year, publisher))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data imported into books.db")
