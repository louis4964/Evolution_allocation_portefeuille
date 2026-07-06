# Simulation de portefeuille d’investissement

## Description
Ce projet implémente en Python une simulation d’évolution de portefeuille d’investissement dans le temps. Il permet de modéliser la croissance d’un capital initial avec ou sans versements mensuels, en intégrant un rendement annuel fixe ainsi qu’un traitement simplifié de la fiscalité sur les gains.

L’objectif est de comparer l’évolution du capital brut, du capital net après impôts et des impôts générés au cours du temps.

## Fonctionnalités
- Simulation de capital initial investi sur plusieurs années
- Ajout optionnel de versements mensuels
- Capitalisation composée des intérêts
- Calcul simplifié de la fiscalité (taux fixe de 30% sur les gains)
- Suivi de l’évolution du patrimoine dans le temps
- Visualisation graphique des résultats

## Paramètres du modèle
- **P0** : capital initial investi
- **n** : durée de l’investissement (en années)
- **mensualité** : activation ou non des versements mensuels
- **m** : montant des versements mensuels
- **R** : rendement annuel du portefeuille

## Méthodologie
Le modèle repose sur la capitalisation composée :
- Sans versements :  
  \( Capital_t = P_0 (1 + R)^t \)

- Avec versements mensuels :  
  accumulation des flux mensuels capitalisés au taux annuel R

Une fiscalité simplifiée est appliquée :
- impôt = 30% des gains réalisés

## Utilisation
- Définir les paramètres dans l’appel de fonction
- Lancer le script Python
- Visualiser l’évolution du capital, des impôts et du capital net

## Structure
- `main.py` : script principal de simulation
- `README.md` : documentation du projet
- `requirements.txt` : dépendances nécessaires

## Exemple d’utilisation
```python
portefeuille(4000, 20, "oui", 600, 0.1)
```

## Résultats affichés
Le programme génère :
- Courbe du capital investi
- Barres du capital brut et net après impôts
- Courbe des impôts cumulés
- Valeurs finales du portefeuille

## Technologies utilisées
- Python 3
- NumPy
- Matplotlib

## Licence 
Ce projet est réalisé sous licence MIT

## Auteur
Louis THOMAS