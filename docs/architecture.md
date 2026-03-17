# Architecture cible

## 1. Vision simple

La plateforme doit prendre une application, la deployer sur Azure, puis rendre son fonctionnement observable.

Autrement dit, on ne veut pas seulement "mettre l'application en ligne". On veut aussi etre capable de repondre a des questions comme :

- est-ce que l'application fonctionne ?
- est-ce qu'elle est lente ?
- ou se produit la panne ?
- quel composant est responsable ?

## 2. Architecture technique

Voici l'architecture cible que nous allons construire.

```text
GitHub repo
   |
   v
Pipeline / scripts d'automatisation
   |
   +--> Analyse IA de la stack (plus tard)
   |
   +--> Build image Docker
   |
   v
Azure Container Registry (ACR)
   |
   v
Azure Kubernetes Service (AKS)
   |
   +--> Application web
   +--> Base de donnees PostgreSQL
   +--> OpenTelemetry Collector
   |
   v
Azure Monitor / Log Analytics / Application Insights
```

## 3. Role de chaque composant

### GitHub

Le depot contient le code source. Dans le Palier 2, la plateforme devra accepter une URL Git comme entree.

### Terraform

Terraform sert a decrire l'infrastructure sous forme de code.

Au lieu de cliquer manuellement dans le portail Azure, on ecrit des fichiers qui declarent :

- le groupe de ressources
- le cluster AKS
- le registre ACR
- les ressources liees a l'observabilite

Avantage :

- reproductible
- versionnable
- modifiable sans repartir de zero

### ACR

`Azure Container Registry` stocke les images Docker.

L'application sera construite en image, puis poussee dans ACR avant d'etre deployee sur AKS.

### AKS

`Azure Kubernetes Service` est le cluster Kubernetes gere par Azure.

C'est lui qui fera tourner :

- l'application
- la base de donnees si on la conteneurise pour la demo
- le collecteur OpenTelemetry

### OpenTelemetry Collector

Le Collector recoit les signaux d'observabilite :

- traces
- logs
- metriques

Puis il les redirige vers la destination choisie.

### Azure Monitor

Azure Monitor est la couche de visualisation et d'analyse.

Il permet de :

- voir les requetes
- suivre les traces distribuees
- analyser les erreurs
- identifier le point de rupture lors d'un incident

## 4. Definition du MVP Palier 1

Le MVP doit demontrer une competence simple mais forte :

"Je sais deployer une application sur AKS et je sais diagnostiquer un incident grace a l'observabilite."

Pour y arriver, notre MVP devra inclure :

- une app de test
- une base de donnees
- une instrumentation OpenTelemetry
- un collecteur
- un scenario de panne
- une demonstration de diagnostic

## 5. Ce que nous ne ferons pas tout de suite

Pour debuter, nous n'allons pas commencer par :

- l'auto-generation complete de Dockerfiles
- l'auto-instrumentation zero-touch
- une architecture multi-environnements complexe

Ce sont de bonnes idees, mais pas le bon point de depart pour un debutant ni pour un MVP de hackathon.
