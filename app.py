import logging
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    animals = conn.execute('SELECT * FROM animals ORDER BY RANDOM() LIMIT 5').fetchall()
    conn.close()
    return render_template('index.html', animals=animals)

@app.route('/animal/<int:id>')
def animal(id):
    conn = get_db_connection()
    animal = conn.execute('SELECT * FROM animals WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('animal.html', animal=animal)

@app.route('/search')
def search():
    query = request.args.get('query')
    conn = get_db_connection()
    results = conn.execute('SELECT * FROM animals WHERE nom LIKE ?', ('%' + query + '%',)).fetchall()
    conn.close()
    return render_template('search_results.html', results=results)

@app.route('/add_animal', methods=['GET', 'POST'])
def add_animal():
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
            cp = request.form['cp']

            logging.debug(f"Nom: {nom}, Espece: {espece}, Race: {race}, Age: {age}, Description: {description}, Courriel: {courriel}, Adresse: {adresse}, Ville: {ville}, CP: {cp}")

            conn = get_db_connection()
            conn.execute('INSERT INTO animals (nom, espece, race, age, description, courriel, adresse, ville, cp) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                         (nom, espece, race, age, description, courriel, adresse, ville, cp))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        except Exception as e:
            logging.error(f"Erreur lors de l'ajout de l'animal : {e}")
            return render_template('add_animal.html', error="Une erreur s'est produite lors de l'ajout de l'animal.")
    return render_template('add_animal.html')

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/search')
def search():
    query = request.args.get('query')
    if query:
        conn = get_db_connection()
        results = conn.execute('SELECT * FROM animals WHERE nom LIKE ? OR espece LIKE ? OR race LIKE ? OR description LIKE ?',
                               ('%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%')).fetchall()
        conn.close()
        return render_template('search_results.html', results=results)
    else:
        return render_template('search_results.html', results=[])
@app.route('/add_animal', methods=['GET', 'POST'])
def add_animal():
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
            cp = request.form['cp']

            # Validation côté serveur
            if not all([nom, espece, race, age, description, courriel, adresse, ville, cp]):
                return render_template('add_animal.html', error="Tous les champs sont obligatoires.")
            if len(nom) < 3 or len(nom) > 20:
                return render_template('add_animal.html', error="Le nom doit avoir entre 3 et 20 caractères.")
            if not age.isdigit() or int(age) < 0 or int(age) > 30:
                return render_template('add_animal.html', error="L'âge doit être une valeur numérique entre 0 et 30.")
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, courriel):
                return render_template('add_animal.html', error="Le courriel doit avoir un format valide.")
            postal_code_pattern = r'^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$'
            if not re.match(postal_code_pattern, cp):
                return render_template('add_animal.html', error="Le code postal doit avoir un format canadien valide.")

            conn = get_db_connection()
            conn.execute('INSERT INTO animals (nom, espece, race, age, description, courriel, adresse, ville, cp) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                         (nom, espece, race, age, description, courriel, adresse, ville, cp))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        except Exception as e:
            return render_template('add_animal.html', error="Une erreur s'est produite lors de l'ajout de l'animal.")
    return render_template('add_animal.html')
