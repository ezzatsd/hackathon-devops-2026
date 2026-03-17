# Hackathon DevOps 2026

Ce depot sert a construire une plateforme DevOps orientee observabilite, automatisation et IA, conformement au sujet "Observabilite, automatisation et IA au coeur du DevOps moderne".

Le projet sera mene comme si tu debutais en DevOps. L'objectif n'est donc pas seulement de "faire marcher" la solution, mais aussi de comprendre clairement pourquoi chaque brique existe.

## 1. Ce que demande le sujet

Le sujet impose de construire une plateforme capable de :

- deployer une application sur Azure Kubernetes Service (`AKS`)
- gerer l'infrastructure avec `Terraform` ou `Bicep`
- integrer une couche d'observabilite avec `OpenTelemetry`
- centraliser les signaux vers `Azure Monitor` ou une stack `Grafana/Loki/Tempo`
- utiliser l'IA (`Azure OpenAI`) pour analyser un depot Git et comprendre sa stack

Le niveau minimum pour valider le projet est le `Palier 1`.

## 2. Notre strategie

Comme le depot est vide, on va avancer par couches.

### Etape A - Reussir le Palier 1

On vise d'abord un MVP solide :

- provisionner `AKS` et `ACR` avec `Terraform`
- deployer une application de reference
- installer un `OpenTelemetry Collector`
- instrumenter l'application
- simuler une panne
- montrer comment retrouver la cause dans les traces/logs/metriques

C'est la partie la plus importante du hackathon, car elle conditionne la reussite du projet.

### Etape B - Preparer le Palier 2

Une fois le socle stable, on ajoutera :

- analyse d'un depot Git fourni en entree
- detection de la stack par IA
- generation automatique des artefacts de deploiement

### Etape C - Viser le Palier 3

Si le temps le permet, on ajoutera l'auto-instrumentation sans modifier le code source.

## 3. Choix pragmatique pour le MVP

Pour un hackathon, le plus raisonnable est de choisir une stack simple a comprendre et bien documentee.

Nous partirons sur :

- une application `Node.js / Express`
- une base `PostgreSQL`
- `Terraform` pour l'infrastructure
- `AKS` comme cluster Kubernetes
- `ACR` pour stocker les images Docker
- `OpenTelemetry Collector` pour collecter les signaux
- `Azure Monitor` comme cible principale

Pourquoi ce choix :

- la stack Node.js est prioritaire dans le sujet
- elle est pedagogique pour debuter
- elle se prete bien a l'instrumentation OpenTelemetry

## 4. Structure du depot

Le depot sera organise ainsi :

```text
.
├── README.md
├── docs/
│   ├── architecture.md
│   └── roadmap.md
├── terraform/
├── kubernetes/
├── scripts/
└── app/
```

## 5. Methode de travail

A chaque etape, on gardera toujours ce schema mental :

1. Comprendre le besoin.
2. Choisir la bonne brique technique.
3. Ecrire la configuration ou le code.
4. Verifier le resultat.
5. Expliquer ce qu'on vient de faire.

## 6. Prochaine etape

La prochaine etape concrete est d'ecrire l'architecture cible et la roadmap du MVP.
Ensuite, on commencera la partie implementation en creant la structure Terraform et les premiers fichiers de configuration.
