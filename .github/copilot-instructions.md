# Instructions pour agents GitHub Copilot (project-specific)

But: Ce dépôt est très minimal — il contient actuellement un seul fichier `Untitled-1.py` à la racine. Ces instructions aident un agent à être immédiatement productif sans supposer d'infrastructure complexe.

1) Vue d'ensemble rapide
- Structure: projet minimal, fichier principal : `Untitled-1.py`.
- Objectif probable: script Python expérimental / brouillon. Aucun fichier de configuration, dépendances, tests ou CI détectés.

2) Que faire en premier
- Ne pas modifier le projet majeur sans demander: signalez que le dépôt est un brouillon et proposez d'ajouter une structure (venv, `requirements.txt`, `README.md`) avant de refactorer.
- Si une fonctionnalité est demandée, proposez une petite structure (par ex. `src/`, `tests/`, `requirements.txt`) et attendez approbation.

3) Commandes utiles (environnement Windows PowerShell)
- Exécuter le script:
  python "c:\Users\DELL\Documents\fac projet\Untitled-1.py"
- Créer un venv recommandé:
  python -m venv .venv; .\.venv\Scripts\Activate.ps1
- Installer dépendances (si `requirements.txt` ajouté):
  pip install -r requirements.txt

4) Conventions et patterns observables
- Aucun pattern applicatif spécifique détecté (fichier unique). Attendez des conventions explicites du mainteneur avant d'imposer une architecture.
- Nom de fichier actuel est un indicateur de brouillon — proposer un renommage structuré (`main.py` ou `src/` + module) si le mainteneur accepte.

5) Règles pour l'agent (pratiques concrètes — pas génériques)
- Préservation: Ne changez pas le comportement existant du fichier sans tests et sans l'accord explicite de l'utilisateur.
- Tests: Si vous créez des tests, placez-les sous `tests/` et fournissez une commande `python -m pytest` dans le README. Créez un `requirements.txt` contenant `pytest` si nécessaire.
- Commits: Fournissez des commits atomiques avec messages clairs. Exemple: `feat: add CLI and entrypoint for Untitled-1.py`

6) Quand proposer des changements structurels
- Proposez d'abord (PR ou commentaire) :
  - conversion en package (`src/`),
  - ajout d'un point d'entrée `main.py` ou CLI,
  - ajout d'un `README.md` décrivant l'intention du script.
- Incluez un plan de migration en 3 étapes et tests minimaux avant de toucher au code de production.

7) Intégrations / dépendances
- Aucun service externe détecté dans le repo. Si vous ajoutez des intégrations (DB, API), documentez les variables d'environnement nécessaires dans le README.

8) Exemples concrets (si on améliore ce dépôt)
- Exemple de petite amélioration sûre: ajouter un wrapper `if __name__ == '__main__':` dans `Untitled-1.py` et proposer un test minimal qui importe une fonction isolée.
- Exemple de ticket à proposer à l'utilisateur: "Rendre `Untitled-1.py` réutilisable en extrayant la logique dans `src/module.py` et ajouter tests".

9) Questions à poser au mainteneur (prioritaires)
- Quel est le but de `Untitled-1.py` ? (script d'analyse, prototype, exercice?)
- Souhaitez-vous que je restructure le projet (tests, packaging) ou préférez-vous des changements incrémentiels ?

10) Références internes
- Fichier principal: `Untitled-1.py` (racine)

--
Si vous voulez, je peux maintenant :
- créer un `README.md` minimal qui décrit le but et les commandes d'exécution, ou
- proposer une PR de restructuration (extraction en `src/`, ajout d'un test) — dites lequel vous préférez.

Veuillez indiquer si certains éléments ci-dessus sont incorrects ou si vous souhaitez que je fusionne avec un fichier d'instructions existant (si vous en ajoutez un).