# Projet API ESILV - Vue d'ensemble des nouvelles sur l'IA

## Projet
**Créer une API pour une vue d'ensemble des nouvelles sur l'Intelligence Artificielle (IA)**

Ce projet implique la création d'une API fournissant des nouvelles liées à l'Intelligence Artificielle (IA). Notre groupe a sélectionné un site renommé dans le domaine de l'IA comme source.

## Objectif

L'objectif est de récupérer des informations du site choisi, soit par scraping, soit via une API existante. Nous avons créé plusieurs endpoints à des fins différentes :

- `/get_data`: Récupère une liste d'articles du site.
- `/articles`: Affiche des informations sur les articles, y compris le numéro de l'article, le titre, la date de publication.
- `/article/<number>`: Accède au contenu d'un article spécifié.
- `/ml/<number>`: Effectue une analyse de sentiment sur le contenu d'un article spécifié.

## Mise en œuvre et déploiement

Le projet a été déployé sur AWS Elastic Beanstalk, ce qui permet d'accéder à l'API publiquement. Voici le lien pour accéder à l'API :

[http://esilv-tim-karl-project-env.us-east-2.elasticbeanstalk.com/](http://esilv-tim-karl-project-env.us-east-2.elasticbeanstalk.com/)

## Utilisation de l'API

Pour interagir avec l'API, utilisez les endpoints suivants :

- **Récupérer les données des articles** :
GET /get_data

- **Afficher un résumé des articles** :

GET /articles


- **Accéder au contenu d'un article spécifique** :
GET /article/1


- **Analyser le sentiment d'un article** :
GET /ml/1

## Équipe

Ce projet a été réalisé par :

- Karl AVODO
- Tim L



