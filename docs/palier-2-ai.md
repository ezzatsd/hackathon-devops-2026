# Palier 2 - Bonus IA

## Objectif

Le Palier 2 demande a la plateforme d'accepter une URL Git, de recuperer le depot, de comprendre automatiquement la stack technique, puis de preparer les decisions de build et de deploiement.

Dans l'etat actuel du projet, l'objectif raisonnable est de preparer une base exploitable :

- clonage automatique d'un depot
- detection heuristique de la stack
- extraction d'indices utiles pour Azure OpenAI
- generation d'un rapport JSON exploitable

## Ce que fait le prototype

Le script :

- clone un depot Git dans un dossier de travail local
- inspecte les fichiers frequents d'une application
- detecte la stack probable
- detecte les indices de base de donnees
- produit un rapport JSON lisible
- genere un prompt pret a etre envoye a Azure OpenAI

## Fichiers concernes

- `scripts/analyze_repo.py`
- `scripts/prompts/azure_openai_repo_analysis.txt`

## Exemple d'usage

```bash
python3 scripts/analyze_repo.py https://github.com/gothinkster/node-express-realworld-example-app
```

Le script produit :

- un dossier temporaire avec le depot clone
- un rapport JSON avec la stack probable
- un prompt texte pret pour Azure OpenAI

## Limites actuelles

Le script ne genere pas encore automatiquement :

- le `Dockerfile`
- les manifests Kubernetes
- les variables d'environnement de deployment

Il sert de socle pour le bonus, pas encore de plateforme zero-touch complete.

## Evolution logique

La prochaine etape apres ce prototype serait :

1. appeler Azure OpenAI avec le prompt genere
2. parser la reponse
3. convertir cette reponse en decisions de build et de deploiement
4. generer les manifests et le Dockerfile
