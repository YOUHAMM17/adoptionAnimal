import sqlite3

conn = sqlite3.connect('base_de_donnees.db')
conn.execute('''CREATE TABLE animaux (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    espece TEXT NOT NULL,
    race TEXT NOT NULL,
    age INTEGER NOT NULL,
    description TEXT NOT NULL,
    courriel TEXT NOT NULL,
    adresse TEXT NOT NULL,
    ville TEXT NOT NULL,
    code_postal TEXT NOT NULL
)''')
conn.close()