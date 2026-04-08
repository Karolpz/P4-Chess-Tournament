# Chess Tournament Manager

Application de gestion de tournois d'échecs en ligne de commande, développée en Python avec une architecture MVC.

## Fonctionnalités

- Créer et gérer des tournois d'échecs
- Ajouter et gérer des joueurs
- Générer automatiquement les paires de matchs (système suisse)
- Enregistrer les résultats des matchs
- Générer des rapports (classements, historique)
- Persistance des données en JSON

## Installation

### Prérequis

- Python 3.x

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