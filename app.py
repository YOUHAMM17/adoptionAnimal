from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import logging
import re

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

def obtenir_connexion_bd():
    conn = sqlite3.connect('base_de_donnees.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def accueil():
    conn = obtenir_connexion_bd()
    animaux = conn.execute('SELECT * FROM animaux ORDER BY RANDOM() LIMIT 5').fetchall()
    conn.close()
    return render_template('accueil.html', animaux=animaux)

@app.route('/animal/<int:id>')
def animal(id):
    conn = obtenir_connexion_bd()
    animal = conn.execute('SELECT * FROM animaux WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('animal.html', animal=animal)

@app.route('/recherche')
def recherche():
    requete = request.args.get('requete')
    logging.debug(f"Recherche pour le terme: {requete}")
    if requete:
        conn = obtenir_connexion_bd()
        resultats = conn.execute('SELECT * FROM animaux WHERE nom LIKE ? OR espece LIKE ? OR race LIKE ? OR description LIKE ?',
                               ('%' + requete + '%', '%' + requete + '%', '%' + requete + '%', '%' + requete + '%')).fetchall()
        logging.debug(f"Nombre de résultats: {len(resultats)}")
        conn.close()
        return render_template('resultats_recherche.html', resultats=resultats)
    else:
        return render_template('resultats_recherche.html', resultats=[])

@app.route('/ajouter_animal', methods=['GET', 'POST'])
def ajouter_animal():
    if request.method == 'POST':
        try:
            nom = request.form['nom']
            espece = request.form['espece']
            race = request.form['race']
            age = request.form['age']
            description = request.form['description']
            courriel = request.form['courriel']
            adresse = request.form['adresse']
            ville = request.form['ville']
            code_postal = request.form['code_postal']

            # Validation côté serveur
            if not all([nom, espece, race, age, description, courriel, adresse, ville, code_postal]):
                return render_template('ajouter_animal.html', erreur="Tous les champs sont obligatoires.")
            if len(nom) < 3 or len(nom) > 20:
                return render_template('ajouter_animal.html', erreur="Le nom doit avoir entre 3 et 20 caractères.")
            if not age.isdigit() or int(age) < 0 or int(age) > 30:
                return render_template('ajouter_animal.html', erreur="L'âge doit être une valeur numérique entre 0 et 30.")
            motif_courriel = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(motif_courriel, courriel):
                return render_template('ajouter_animal.html', erreur="Le courriel doit avoir un format valide.")
            motif_code_postal = r'^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$'
            if not re.match(motif_code_postal, code_postal):
                return render_template('ajouter_animal.html', erreur="Le code postal doit avoir un format canadien valide.")

            conn = obtenir_connexion_bd()
            conn.execute('INSERT INTO animaux (nom, espece, race, age, description, courriel, adresse, ville, code_postal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                         (nom, espece, race, age, description, courriel, adresse, ville, code_postal))
            conn.commit()
            conn.close()
            return redirect(url_for('accueil'))
        except Exception as e:
            logging.error(f"Erreur lors de l'ajout de l'animal : {e}")
            return render_template('ajouter_animal.html', erreur="Une erreur s'est produite lors de l'ajout de l'animal.")
    return render_template('ajouter_animal.html')

if __name__ == '__main__':
    app.run(debug=True)