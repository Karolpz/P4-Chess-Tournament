# Chess Tournament Manager

Application de gestion de tournois d'échecs en ligne de commande, développée en Python avec une architecture MVC.

## Fonctionnalités

### Gestion des joueurs
- Ajouter un joueur avec ses informations (nom, prénom, date de naissance, identifiant national)
- Validation du format de l'identifiant national
- Affichage de la liste des joueurs triés par ordre alphabétique

### Gestion des tournois
- Créer un tournoi (nom, lieu, dates, nombre de rounds, description)
- Ajouter des joueurs existants à un tournoi en cours
- Lancer les rounds et générer automatiquement les paires (système suisse)
- Évite les rematches entre joueurs déjà affrontés
- Enregistrer les résultats de chaque match (victoire joueur 1, victoire joueur 2, match nul)

### Rapports
- Liste de tous les joueurs enregistrés (ordre alphabétique)
- Liste de tous les tournois
- Détail complet d'un tournoi : rounds, matchs et classement final

### Persistance
- Sauvegarde automatique après chaque action via le décorateur `@autosave`
- Données stockées en JSON dans le dossier `data/`
- Rechargement automatique au démarrage de l'application

## Installation

### Prérequis

- Python 3.10+

### Cloner le projet
```bash
git clone <url-du-repo>
cd P4-Chess-Tournament
```

### Créer et activer l'environnement virtuel
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### Installer les dépendances
```bash
pip install -r requirements.txt
```

## Lancer l'application
```bash
python main.py
```

## Générer le rapport flake8
```bash
flake8 --format=html --htmldir=flake8_report .
```

## Auteur

Caroline — Formation OpenClassrooms, Projet 4