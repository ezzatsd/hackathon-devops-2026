# Terraform explique simplement

## Pourquoi on ecrit Terraform maintenant

Le sujet exige une infrastructure geree en code.

Cela veut dire qu'au lieu de cliquer dans Azure Portal pour creer les ressources une par une, on les decrit dans des fichiers texte.

Ce choix a plusieurs avantages :

- tu peux relire ce qui sera cree
- tu peux versionner les changements dans Git
- tu peux recreer le meme environnement plus tard
- tu diminues les erreurs manuelles

## Les fichiers que nous avons crees

### `terraform/versions.tf`

Ce fichier fixe :

- la version minimale de Terraform
- le provider `azurerm`
- la connexion a Azure via `subscription_id`

En pratique, c'est le point d'entree technique de Terraform.

### `terraform/variables.tf`

Ce fichier declare les entrees du projet.

Exemples :

- `location` : dans quelle region Azure on deploie
- `project_name` : sert a nommer les ressources
- `node_count` : nombre de machines dans AKS
- `vm_size` : taille des VM

L'idee importante :
une variable permet d'eviter d'ecrire des valeurs en dur partout.

### `terraform/main.tf`

C'est le coeur du socle.

Il decrit les ressources principales :

- `Resource Group`
- `Log Analytics Workspace`
- `Application Insights`
- `Azure Container Registry`
- `Azure Kubernetes Service`
- droit `AcrPull` pour qu'AKS puisse recuperer les images dans ACR

### `terraform/outputs.tf`

Ce fichier sert a recuperer facilement certaines informations apres le deploiement.

Par exemple :

- le nom du cluster
- l'adresse du registre ACR
- la connection string d'Application Insights

### `terraform/terraform.tfvars.example`

Ce fichier montre le format des valeurs a fournir.

On ne met pas directement de secrets reels dedans. On l'utilise comme modele pour creer un vrai `terraform.tfvars` local.

## Pourquoi ces ressources sont utiles au sujet

### Resource Group

C'est le conteneur logique Azure qui regroupe les ressources du projet.

### ACR

Il stocke les images Docker de l'application.

### AKS

Il execute les conteneurs dans Kubernetes.

### Log Analytics + Application Insights

Ils servent de base a l'observabilite dans Azure.

Sans eux, tu deployes. Avec eux, tu comprends ce qu'il se passe.

## Ce que nous n'avons pas encore fait

Nous n'avons pas encore :

- initialise Terraform
- verifie que les versions existent cote Azure
- applique le plan sur une souscription reelle

C'est normal.

Avant d'executer une infrastructure, il faut d'abord comprendre ce qu'on va creer.
