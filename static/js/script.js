document.getElementById('addAnimalForm').addEventListener('submit', function(event) {
    let valid = true;

    let nom = document.getElementById('nom').value;
    let age = document.getElementById('age').value;
    let courriel = document.getElementById('courriel').value;
    let adresse = document.getElementById('adresse').value;
    let ville = document.getElementById('ville').value;
    let cp = document.getElementById('cp').value;

    // Réinitialiser les messages d'erreur
    document.getElementById('nomError').textContent = '';
    document.getElementById('ageError').textContent = '';
    document.getElementById('courrielError').textContent = '';
    document.getElementById('adresseError').textContent = '';
    document.getElementById('villeError').textContent = '';
    document.getElementById('cpError').textContent = '';

    if (nom.length < 3 || nom.length > 20) {
        valid = false;
        document.getElementById('nomError').textContent = 'Le nom doit avoir entre 3 et 20 caractères.';
    }

    if (isNaN(age) || age < 0 || age > 30) {
        valid = false;
        document.getElementById('ageError').textContent = 'L\'âge doit être une valeur numérique entre 0 et 30.';
    }

    let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailPattern.test(courriel)) {
        valid = false;
        document.getElementById('courrielError').textContent = 'Le courriel doit avoir un format valide.';
    }

    let postalCodePattern = /^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$/;
    if (!postalCodePattern.test(cp)) {
        valid = false;
        document.getElementById('cpError').textContent = 'Le code postal doit avoir un format canadien valide.';
    }

    if (!adresse.includes(',')) {
        valid = false;
        document.getElementById('adresseError').textContent = 'L\'adresse doit contenir une adresse civique, ville et code postal.';
    }

    if (ville.length === 0) {
        valid = false;
        document.getElementById('villeError').textContent = 'La ville est obligatoire.';
    }

    if (!valid) {
        event.preventDefault();
    }
});
