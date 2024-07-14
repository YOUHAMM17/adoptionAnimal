import sqlite3

conn = sqlite3.connect('base_de_donnees.db')

animaux = [
    ('Bella', 'Chien', 'Schnauzer', 5, 'Chien affectueux et joueur', 'proprietaire1@example.com', '123 Rue Principale', 'Montréal', 'H2X 1Y4'),
    ('Milo', 'Chat', 'Persan', 3, 'Chat calme et câlin', 'proprietaire2@example.com', '456 Avenue des Érables', 'Québec', 'G1A 2B5'),
    ('Nemo', 'Poisson', 'Clown', 1, 'Poisson coloré et actif', 'proprietaire3@example.com', '789 Boulevard Saint-Laurent', 'Trois-Rivières', 'G8Z 3L2'),
    ('Rex', 'Chien', 'Labrador', 7, 'Chien loyal et énergique', 'proprietaire4@example.com', '1010 Rue de la Paix', 'Sherbrooke', 'J1H 4M5'),
    ('Luna', 'Chat', 'Siamois', 4, 'Chat curieux et intelligent', 'proprietaire5@example.com', '1212 Avenue Royale', 'Laval', 'H7N 6K3')
]

conn.executemany('''
    INSERT INTO animaux (nom, espece, race, age, description, courriel, adresse, ville, code_postal)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', animaux)

conn.commit()
conn.close()