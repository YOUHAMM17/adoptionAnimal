import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('''CREATE TABLE animals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    espece TEXT NOT NULL,
    race TEXT NOT NULL,
    age INTEGER NOT NULL,
    description TEXT NOT NULL,
    courriel TEXT NOT NULL,
    adresse TEXT NOT NULL,
    ville TEXT NOT NULL,
    cp TEXT NOT NULL
)''')
conn.close()
