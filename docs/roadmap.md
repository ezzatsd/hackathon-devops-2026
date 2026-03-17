# Roadmap du projet

## Phase 1 - Cadrage

Objectif :
Transformer le sujet en plan de travail executable.

Sorties attendues :

- architecture cible
- choix de stack
- decoupage par paliers

## Phase 2 - Infrastructure Azure

Objectif :
Creer les ressources de base avec Terraform.

Ressources visees :

- Resource Group
- Azure Container Registry
- Azure Kubernetes Service
- Log Analytics Workspace

Ce qu'il faudra comprendre :

- ce qu'est une ressource Azure
- comment Terraform garde un etat
- pourquoi une infra as code est plus fiable qu'une creation manuelle

## Phase 3 - Application de reference

Objectif :
Choisir et preparer une application simple a deployer.

Cible recommandee :

- Node.js / Express
- PostgreSQL

Ce qu'il faudra faire :

- recuperer ou creer l'application
- creer le `Dockerfile`
- construire l'image
- la pousser dans `ACR`

## Phase 4 - Deploiement Kubernetes

Objectif :
Faire tourner l'application sur AKS.

Objets Kubernetes a prevoir :

- `Namespace`
- `Deployment`
- `Service`
- `Secret`
- eventuellement `Ingress`

Ce qu'il faudra comprendre :

- difference entre un Pod et un Deployment
- difference entre un Service et un Ingress
- comment l'application accede a sa base de donnees

## Phase 5 - Observabilite

Objectif :
Rendre l'application visible et diagnosticable.

Ce qu'il faudra mettre en place :

- SDK OpenTelemetry dans l'application
- OpenTelemetry Collector dans le cluster
- export vers Azure Monitor

Ce qu'il faudra comprendre :

- difference entre logs, metriques et traces
- ce qu'est une trace distribuee
- comment identifier un point de rupture

## Phase 6 - Incident Day 2

Objectif :
Prouver la valeur de la plateforme.

Scenario suggere :

- la base PostgreSQL est arretee ou inaccessible
- l'application echoue sur certaines requetes
- les traces permettent de localiser la panne

## Phase 7 - Bonus IA

Objectif :
Automatiser l'analyse d'un depot Git.

Ce qu'on ajoutera plus tard :

- clonage automatique d'une URL Git
- analyse IA de la stack
- detection de la base de donnees
- generation d'artefacts de build/deploiement
