# Kubernetes explique simplement

## Ce que contiennent ces manifests

Nous avons prepare trois blocs :

- une base PostgreSQL
- une application Node.js / Express
- un OpenTelemetry Collector

## Pourquoi PostgreSQL est present

Le sujet demande un scenario de diagnostic en production.

Pour demontrer la valeur de l'observabilite, il faut une dependance reelle.
La base de donnees est ideale pour cela, car une panne de base provoque un comportement facile a observer :

- l'application repond encore sur certains endpoints
- les endpoints qui interrogent la base tombent en erreur
- les traces permettent d'identifier le composant en faute

## Pourquoi l'application est simple

Pour un debutant, il vaut mieux une application courte mais lisible.

Les endpoints sont :

- `/` : reponse simple pour verifier que l'app tourne
- `/health` : verifie la connexion a PostgreSQL
- `/users` : lit des donnees en base

## Pourquoi le Collector est separe

Le Collector sert d'intermediaire entre l'application et Azure Monitor.

L'application envoie ses signaux au Collector.
Le Collector :

- recoit les traces
- les structure
- les exporte vers Azure

Cela permet de centraliser l'observabilite et de faire evoluer la plateforme plus facilement.

## Comment deployer plus tard

Quand AKS sera pret, on pourra appliquer tous les manifests avec :

```bash
kubectl apply -k kubernetes/
```

Avant cela, il faudra remplacer :

- `CHANGE_ME_ACR_LOGIN_SERVER` dans le deployment applicatif
- `CHANGE_ME` dans le secret du Collector

## Scenario de panne prevu

Pour la demonstration Day 2, le scenario le plus simple sera :

1. l'application fonctionne normalement
2. PostgreSQL devient indisponible
3. `/health` et `/users` retournent une erreur
4. les traces montrent que l'echec vient de la base
