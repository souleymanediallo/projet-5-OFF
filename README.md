# Projet 5 : Utilisez les données publiques de l'OpenFoodFacts

## Contexte 

Pur Beurre est une entreprise axée sur les habitudes alimentaires et qui propose à ses utilisateurs une aide à la gestion d’une alimentation plus saine. Pour ce faire, elle souhaite créer un programme permettant, via une interaction depuis la base Open Food Facts, de récupérer les aliments, de les comparer et de choisir un substitut plus sain.

## Description du parcours utilisateur
L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :

1. Quel aliment souhaitez-vous remplacer ?
2. Retrouver mes aliments substitués.

L'utilisateur sélectionne son choix et le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses.

L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.


## Fonctionnalités
* Recherche d'aliments dans la base Open Food Facts.
* L'utilisateur interagit avec le programme dans le terminal,
* Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question,
* La recherche doit s'effectuer sur une base MySql.