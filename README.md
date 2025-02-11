Gestion des Matchs de football en Ligne
Ce projet est une application web développée avec Flask, permettant de gérer les matchs de football et les joueurs. 
Il inclut une interface utilisateur pour consulter les matchs et un panneau d'administration pour gérer les matchs et les joueurs. L'accès à l'interface administrateur est sécurisé par un code root.

FONCTIONNALITÉ
- Côté Utilisateur
  Voir les matchs en direct : Consultez les matchs actuellement en cours.
  Voir les matchs à venir : Consultez les matchs prévus.
  Historique des matchs : Consultez les matchs terminés, avec les scores et les meilleurs joueurs.
  Classement des joueurs : Affichez le classement des joueurs basé sur leurs points.
- Côté Administrateur
  Gestion des matchs : Créez, modifiez et supprimez des matchs. Vous pouvez définir les scores et le meilleur joueur pour les matchs terminés.
  Gestion des joueurs : Créez, modifiez et supprimez des joueurs. Les joueurs sont associés à des équipes et ont des points.
  Sécurisation de l'Accès Admin
  L'accès à l'interface administrateur est protégé par un Code Root. L'utilisateur doit entrer ce code dans un formulaire popup pour accéder à la gestion des matchs et des joueurs.

Installation et Prérequis
1. Cloner le projet
  git clone https://github.com/RogKenzas/Gestion-de-match-de-football-en-ligne.git
  cd Gestion-de-match-de-football-en-ligne
2. Créer un environnement virtuel (recommandé)
  - Windows :
      python -m venv venv
      venv\Scripts\activate
3. Installer les dépendances
  pip install -r requirements.txt
4. Lancer l'application Flask
  flask run
L'application sera accessible sur http://127.0.0.1:5000.

Structure du Projet
gestion_matchs/
├── app.py                 # Code principal de l'application Flask
├── models.py              # Modèles pour gérer les données (matchs et joueurs)
├── data/
│   ├── players.json       # Fichier JSON contenant les données des joueurs
│   └── matches.json       # Fichier JSON contenant les données des matchs
├── templates/             # Templates HTML
│   ├── base.html          # Template de base pour l'UI
│   ├── admin_dashboard.html
│   ├── admin_matches.html
│   ├── admin_edit_match.html
│   ├── admin_edit_player.html
│   ├── admin_players.html
│   ├── user_home.html
│   ├── live_matches.html
│   ├── upcoming_matches.html
│   ├── match_history.html
│   └── ranking.html
├── static/                # Dossier contenant les fichiers statiques (CSS, JS, etc.)
│   ├── css/
│   ├── js/
│   └── images/
├── requirements.txt       # Liste des dépendances Python nécessaires
└── README.md              # Documentation du projet

- Technologies utilisées
  * Flask : Framework web pour Python.
  * Bootstrap : Framework CSS pour la mise en page et les composants.
  * JSON : Format de fichier pour stocker les données des joueurs et des matchs.
  Licence
  Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
  
- Suggestions pour de futures améliorations :
  Ajouter une base de données pour gérer les joueurs et les matchs (ex. SQLite, PostgreSQL).
  Améliorer la sécurisation de l'application (authentification utilisateur, cryptage des mots de passe, etc.).
  Ajouter un système de notifications pour informer les utilisateurs des nouveaux matchs ou résultats.
