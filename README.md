Participants : Mattis BORDERIES Amine AMZAI, Maxime DE BUSSAC, Raphael POUX

pour lancer le projet : lancer le main , autre version du jeu plus fluide mais dynamique pas convaincante sur raphael.py

Fonctionnalités : 

Menu principal : permet de commencer la partie, lire les instructions, ou quitter le jeu. 
Une carte où le joueur peut évoluer. 
Les cartes sont des fichiers textes qui sont lues par le jeu, elles contiennent des zones accessibles, des obstacles, et le point d'apparition du joueur. 
Gestion du joueur :
Gestion des portails : Le joueur peut placer et déplacer des portails. Les portails sont placés dans le mur visé par le joueur et prennent automatiquement la bonne orientation.
L'orientation d'un portail influe sur la gestion de la vitesse en sortie d'un portail. 

main.py : Permet de lancer le programme, et de naviguer entre les différents modes (instructions, et game) 

button.py : Gestion des boutons utilisés dans le menu principal

instructions.py ! Permet d'afficher les instructions

game.py : Le jeu à proprement dit

Map.py : Permet de passer d'une carte en fichier texte à une map affichée à l'écran 

Perso.py : Gestion du personnage et de sa téléportation, gere le personnage, ses déplacements et les forces qui s'appliquent sur lui (gravité, frottement), gère l'affichage du personnage

portail.py : Gestion des portails

carte.txt : Une carte

carte_2.txt, carte_3.txt,carte_4.txt : Des cartes plus fournies

credits.py : L'écran de crédits

On a également codé une deuxième version du jeu avec un affichage et un fonctionnement différent.



README.md : ( Ce que vous êtes en train de lire en ce moment même ^^)



Difficultées rencontrées :
Mattis : Lecture de la Map : choix du format (finalement sous forme de matrice)
gerer les collisions (finalement en stockant les coordonnées accessibles et réduire la vitesse si la prochaine positions se trouve hors des positions accessibles)
Nouveau problème à partir de ca : lenteur du programme lorsque j'avance sur un mur en le collant du à une boucle while trop longue --> pas de solution pour la raccourcir sans conserver la meme dynamique du jeu 
gerer la gravité et les histoires de vitesse maximal, tout en mettant des frottements lorsque l'on est au sol 
Amine : 
-Gestion des portails: La gestion des nombreux cas particuliers qui rendent l'écriture fastidieuse, ce qui pousse alors à essayer d'optimiser le code pour le rendre 
plus lisible. Dans des cas particuliers les téléportations peuvent être sources de bugs.
-Git: Gérer les conflits, et adapter son code aux autres de manière générale. 
Raphaël :
L'envergure du projet a été un problème majeur car elle a ralenti considérablement les phases de test et l'ajustement des paramètres de jeu.
De plus, la réunion des différentes parties du code a été la source de nombreux bugs.



Ce que j'ai appris : 
Mattis : mieux comprendre l'utilité des classes : une bien meilleur lisibilité du code 
lecture d'evenement et les subtilité sur la gestion d'affichage : meilleur compréhension de la librairie pygame 
Amine : Les classes sont un outil très pratique. Il est important d'essayer de bien réfléchir en amont à l'architecture du code pour qu'il soit à la fois le plus lisible et le plus compréhensible.  
Raphaël : Les classes sont très pratiques pour créer des objets, les modifier et les faire interagir. Les bugs que l'on rencontre sont soit dus à la manière dont on veut que
les interactions se fassent, soit à la manière qu'on a de coder ces interactions. Il est capital de comprendre la source du bug pour le résoudre. 
