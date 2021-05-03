# Digitalisation au sein d’un ensemble

## Description courte du scénario d'analyse

L'apprentissage d'un cours inclut de nombreuses activitées et  **requière une certaine pédagogie** pour favoriser la compréhension de celui-ci. Ainsi, des activités telles que le visionnage d'une vidéo, la réalisation d'un quiz peuvent intégrer une séquence pédagogique en ligne, alors que d'autres activités comme la participation à un débat, une présentation ne peuvent être réalisés qu'en présentiel. Il est intéressant de comprendre les facteurs qui réduisent **la total digitalisation** d'un module (ex: facteur technique, ou humain). L'object de ce package est de visualiser l'apport de digitaisation dans chaque cours à travers une  institution d'enseignements supérieurs comme l'université, les départements qui l'a composent et les enseignants qui y travaillent. Aussi, le public des cours en ligne étant plus large que son *public natif*, améliorer la digitalisation des cours peuvent améliorer leur popularité.

### Tag

Digitalisation, Ciblage

## Cas d’utilisation

### Orientés concepteurs

#### Identification des ressources exploitables

Parmi les cours proposés par les enseignants, de nombreuses ressources ne sont pas exploités à travers des cours en ligne. Un concepteur souhaite enrichir le contenu de son cours et améliorer la digitalisation de celui-ci. Il lui faut ainsi distinguer les ressources non exploitées et celles non exploitables.

#### Identification des niveaux de digitalisation

On cherche à identifier pour les durées de modules, la proportion de digitalisation de chacun. Des compréhensions possibles sont l'impossibilité de concevoir une grande digitalisation pour le module ou un manque d'implémation du module.

### Orientés administrateurs

#### Distinction au sein d'un groupe

La compréhension des niveaux de digitalisation peut se faire depuis de nombreux échellon (au seins de l'université, d'un département université, ou encore d'un individu) afin d'identifier les ressources qui peuvent être améliorer et possiblement implémenter dans des cours en ligne.

### Orientés chercheurs

Création d'une base de référents agrégés (ex: PRAGE/PRCE) et de leur niveau d'utilisation de ressources en ligne. On peut orienter l'analyse sur la catégorisation de ces référents/enseignants ou encore département, on pourra ainsi s'intéresser à la distinction entre différents cas: celui où l'enseignant utilise très peu de ressources en ligne, celui qui fournit autant de ressources en ligne que de cours magistraux et celui qui utilise plus de ressource en ligne que de cours magistraux. On pourra identifier le niveau de digitalisation des trois patternes respectifs comme «Faible», «Moyen» et «Fort».
Il est possible de chercher les référents avec la possibilité d'ajouter un plus grand nombre de ressources en ligne.

## Inputs

### Logdata

Définition des identifiants des départements universitaire, des référents (enseignants, PRAG/PRCE) et des cours et la temporalité

Departement_ID | Referent_ID  | Cours_ID | Année |
---------------|--------------|----------|-------|
Identifiant unique du département | Identifiant unique du réferent (enseignant) | Identifiant unique du cours | Année du cours |
1 | 10002 | 2035| 2019
1 | 10002 | 2036| 2019
1 | 10003 | 2037| 2019
2 | 10015 | 2520| 2019
3 | 10050 | 2540| 2019

### Niveau de digitalisation

L'analyste a besoin pour réaliser ce travail de connaître de manière exacte la durée de chaque cours/module et leur proporton d'implémentation en ligne. Un travail de nettoyage de la base de données peut avoir été réalisé en amont par l'analyste pour filtrer des cours, des référents ou départements précis ou encore une année. Par exemple, on peut retirer l'année 2020 qui a connu une augmentation inhabituel  de l'utilisation de cours en ligne afin de ne pas obtenir de résultats biaiser.

Base sur laquelle doit être réalisée l'analyse. Contient l'identifiant d'un cours, le temps d'un cours, la durée d'utilisation de cours en ligne et la durée des cours magistraux.

Cours_ID | Temps_Cours  | Temps_Cours_enLigne | Temps_Cours_Présentiel |
---------|--------------|-------------|---------------|
Identifiant unique du cours | Durée totale du cours (cours magistraux et cours en ligne inclut) | Durée totale des cours en ligne | Durée totale des cours magistraux en présentiel |
2030 | 35 | 5   | 30
2031 | 12 | 10  | 2
2032 | 50 | 40  | 10
2033 | 20 | 10  | 10
2034 | 90 | 60  | 30

## Outputs

### Ratio et pourcentage de digitalisation

Ratio compris entre 0 et 1 qui représente la durée totale d'utilisation des ressources en ligne par rapport à la durée totale du cours.
Pourcentage compris entre 0 et 100 qui représente la multiplication du ratio

Cours_ID | Digitalisation_Ratio | Digitalisation_Pourcentage
---------|----------------------|---------------------------|
Identifiant unique du cours | Ratio d'utilisation de ressources en ligne par rapport à la durée totale d'un cours | Pourcentage d'utilisation de ressources en ligne par rapport à la durée total d'un cours |
2030 | 0.14 | 14
2031 | 0.83 | 83
2032 | 0.80 | 80
2033 | 0.50 | 50
2034 | 0.67 | 67

### Niveau digitalisation

List de quatres valeurs représentant les quatres niveaux de digitalisation suivant: «Forte Digitalisation, «Moyenne-Forte Digitalisation, «Moyenne-Faible Digitalisation» et «Faible Digitalisation». Le niveau de digitalisation dépend du ratio/percentage décrit précèdemment.

Cours_ID | Digitalisation_Ratio | Digitalisation_Pourcentage| Niveau_Digitalisation
---------|----------------------|---------------------------|----------------------|
Identifiant unique du cours | Ratio d'utilisation de ressources en ligne par rapport à la durée totale d'un cours | Pourcentage d'utilisation de ressources en ligne par rapport à la durée total d'un cours | Niveau de digitalisation de chaque cours en fonction du ratio/pourcentage
2030 | 0.14 | 14 | Faible Digitalisation
2031 | 0.83 | 83 | Forte Digitalisation
2032 | 0.80 | 80 | Moyenne-Forte Digitalisation
2033 | 0.50 | 50 | Moyenne-Faible Digitalisation
2034 | 0.67 | 67 | Moyenne-Forte Digitalisation

## Indicateur recommandés

Indicateur 1: Proportion des cours avec moins de 20% d'utilisation de ressources en ligne

Indicateur 2: Proportion des cours avec plus de 80% d'utilisation de ressources en ligne

## Exemples

### Cas d'étude Factice

L'étude factice est divisé en trois partie.

1. Pourcentage de Digitalisation d'une Université en fonction du département sur huit années.
2. Pourcentage de Digitalisation d'un Département d'une Université sur la même période que précèdemment.
3. Pourcentage de Digitalisation de chaque Enseignant d'un Département sur une période de quatres années.

La réalisation des études peut être retrouver avec les liens ci-dessous: \
[Lien des données artificielles.](https://github.com/Educational-Analytics/Teaching-Analytics/blob/1b70c30f8483a30083d25b46898308d4a48415ed/Digitalization/Example/Data/Digitalization.csv) \
[Algorithme Python permettant de réaliser les études.](https://github.com/Educational-Analytics/Teaching-Analytics/blob/1b70c30f8483a30083d25b46898308d4a48415ed/Digitalization/Example/Programs/Digitalization.py) \
[Algorithme Python permettant de réaliser les visualisations des études.](https://github.com/Educational-Analytics/Teaching-Analytics/blob/1b70c30f8483a30083d25b46898308d4a48415ed/Digitalization/Example/Programs/Digitalization_VIZ.py)

#### Échelle Universitaire

La première étude se concentre sur l'échelle d'une Université (factice) qui nous permet d'obtenir la figure suivante qui représente une «Heatmap» des pourcentages de digitalization de chaque département d'une université pendant huit années allant de 2013 à 2020:

factice-data: Hybridation au sein d'une Université
![factice-data: Pourcentage de Digitalisation pour chaque département d'une Université en fonction de l'année](https://raw.githubusercontent.com/Hype-13/Teaching-Analytics/main/Digitalization/Example/Figures/Heatmap%20of%20the%20Digitalization%20for%20the%20Factice%20University%20Departments%20from%202013%20to%202020.png)

La figure ci-dessus nous permet d'identifier une amélioration de la digitalization après chaque année plus ou moins importante dans chaque département. On remarque qu'entre 2013 et 2020, l'utilisation de ressources en ligne a doublé avec 25% en moyenne entre 2013 à plus de 50% en 2020.
Il semble qu'au niveau universitaire l'utilisation de ressources en ligne est une possible piste concernant le futur de l'éducation. Cependant l'échelle de cette étude n'offre pas un assez bon ciblage est ne permet pas de comprendre la raison de de cette augmentation au cours des années de l'utilisation des ressources.

#### Échelle Départementale

Un ciblage plus important est celui d'un département d'une université. Dans cette seconde étude qui se concentre sur l'échelle d'un Département d'une université (factice) nous  obtenons la figure suivante qui représente un «Boxplot», la distribution des pourcentages de digitalization d'un département (Management) d'une université pendant huit années allant de 2013 à 2020:

factice-data: Hybridation au sein d'un Département
![factice-data: Distribution du Pourcentage de Digitalisation d'un département d'une Université en fonction de l'année](https://raw.githubusercontent.com/Hype-13/Teaching-Analytics/main/Digitalization/Example/Figures/Boxplot%20of%20the%20Digitalization%20for%20the%20Factice%20University%20Department%20of%20Management%20from%202013%20to%202010.png)

La figure ci-dessus nous permet de comprendre l'amélioration de l'utilisation de ressources en ligne en fonction des années. On remarque notamment la répartition du pourcentage de digitalisation de chaque cours. Nous pouvons observer une une croissance de 5% chaque année avec en 2020 la plus haute distribution et une mediane à 50% de digitalisation soit la moitié des cours qui utilisent des ressources en ligne.
L'échelle départementale est plus précise que celle universitaire est nous permet donc de comprendre la répartition de l'utilisation de ressources en ligne. Toutefois, nous pouvons encore avoir un ciblage plus précis.

#### Échelle Individuelle

Le ciblage le plus important concernant l'effectif d'une Université est l'enseignant d'un département. Dans cette dernière étude, nous obtenons la figure suivante qui représente le pourcentage de digitalisation de chaque enseignant d'un département (Management) pendant quatres années de forte digitalisation allant de 2017 à 2020.

L'analyse de la digitalisation de chaque enseignant d'un département nous permet d'obtenir la figure suivante:

factice-data: Hybridation par Enseignant
![factice-data: Pourcentage de Digitalisation de chaque Enseignant des Départements respectifs; AGORA, LPTM et LT2D de 2017 à 2019](https://raw.githubusercontent.com/Hype-13/Teaching-Analytics/main/Digitalization/Example/Figures/Barplots%20of%20the%20Digitalization%20for%20the%20Factice%20University%20Department%20of%20Management%20from%202017%20to%202019.png)

Le graphique ci-dessus nous permet de comprendre l'amélioration de l'utilisation de ressources d'un département à travers les enseignants de celui-ci. On remarque que certain enseignant possède un niveau de digitalisation plus élévé que d'autres.

## Bibliographie
