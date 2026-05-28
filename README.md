# Chess Tournament Manager

## Description

Chess Tournament Manager est une application Python permettant de gérer des tournois d'échecs depuis un terminal.

Le projet a été développé avec une architecture MVC (Model / View / Controller) et utilise TinyDB pour la sauvegarde des données au format JSON.

### Fonctionnalités principales

* gestion des joueurs
* gestion des tournois
* ajout et suppression de joueurs dans un tournoi
* génération automatique des rounds
* système suisse simplifié
* prévention des rematchs
* saisie et modification des scores
* classement automatique des joueurs
* sauvegarde persistante des données
* génération d'un rapport Flake8

---

# Installation

## 1. Cloner le projet

```bash
git clone <url-du-repository>
cd chess_tournament
```

---

## 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

---

## 3. Activer l'environnement virtuel

### Windows

```bash
.venv\Scripts\activate
```

### Linux / MacOS

```bash
source .venv/bin/activate
```

---

## 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# Lancer le programme

```bash
python main.py
```

---

# Générer le rapport Flake8

```bash
flake8 controllers database models views main.py --max-line-length=119 --exclude=.venv --format=html --htmldir=flake8_rapport
```

Le rapport HTML sera généré dans le dossier :

```text
flake8_rapport/
```

---

# Structure du projet

```text
chess_tournament/
│
├── controllers/
├── database/
├── models/
├── views/
├── flake8_rapport/
├── main.py
├── requirements.txt
└── README.md
```

---

# Architecture MVC

Le projet utilise une architecture MVC :

## Models

Les modèles représentent les données de l'application :

* Player
* Match
* Round
* Tournament

Ils gèrent également :

* la sérialisation JSON
* la désérialisation JSON

---

## Views

Les vues gèrent :

* l'affichage dans le terminal
* les saisies utilisateur
* les menus

---

## Controllers

Les contrôleurs gèrent :

* la logique métier
* la génération des rounds
* les calculs de classement
* les vérifications métier

---

# Base de données

Le projet utilise TinyDB pour sauvegarder les données dans un fichier JSON.

Les données enregistrées :

* joueurs
* tournois
* rounds
* matchs
* scores

---

# Fonctionnalités détaillées

## Gestion des joueurs

* créer un joueur
* afficher les joueurs
* supprimer un joueur

---

## Gestion des tournois

* créer un tournoi
* afficher les tournois
* supprimer un tournoi

---

## Gestion des inscriptions

* ajouter un joueur à un tournoi
* retirer un joueur d'un tournoi
* prévention des doublons

---

## Gestion des rounds

* génération automatique des rounds
* système suisse simplifié
* prévention des rematchs
* suivi des rounds terminés

---

## Gestion des résultats

* saisie des scores
* modification des scores
* calcul automatique du classement

---

# Qualité du code

Le projet respecte les standards PEP8 grâce à Flake8.

Un rapport HTML est généré dans le dossier :

```text
flake8_rapport/
```

---

# Auteur

Florent
