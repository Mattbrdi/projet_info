La version la plus avancée est Raphael.py avec le module implémenté par Mattis
Participants : Mattis BORDERIES Amine AMZAI, Maxime DE BUSSAC, Raphael POUX

pour lancer le projet : lancer le main 

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
Perso.py : Gestion du personnage et de sa téléportation, gere le personnage, ses déplacements et les forces qui s'appliquent sur lui (gravité, frottement), gere l'affichage du personnage
portail.py : Gestion des portails
carte.txt : Une carte
carte_2.txt : Une seconde carte plus fournie 
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



Ce que j'ai appris : 
Mattis : mieux comprendre l'utilité des classes : une bien meilleur lisibilité du code 
lecture d'evenement et les subtilité sur la gestion d'affichage : meilleur compréhension de la librairie pygame 
Amine : Les classes sont un outil très pratique. Il est important d'essayer de bien réfléchir en amont à l'architecture du code pour qu'il soit à la fois le plus lisible et le plus compréhensible.  
