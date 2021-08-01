# Solitaire - une histoire de vacances

![](https://github.com/haagor/Solitaire/blob/main/img/solitaire_picture.png)

Je vois ce casse-tête depuis que je suis né. Vingt sept ans que je n’arrive pas à en venir à bout ! Et ce n’est pas faute d’avoir essayé. Etant en vacances, je passe devant, je m’assois, j’essaye une dizaine de fois... et je me dis : “si je n’arrive pas à craquer ce problème, est-ce que je ne pourrais pas écrire un programme qui le fait pour moi ?”.

Les règles que je connais sont simples : tu enlèves la bille du milieu. Tu fais sauter une bille par-dessus une autre, en ligne. La bille par dessus laquelle tu sautes doit être retirée. Le but est d'exécuter cette opération jusqu’à n’avoir plus qu’une seule bille sur le plateau.

Je modélise donc mon plateau, un simple dictionnaire de coordonnées. Facilement visualisable avec une librairie Python.

![](https://github.com/haagor/Solitaire/blob/main/img/solitaireStep1.png)

Je code ma fonction qui trouve les mouvements possibles. Une autre qui exécute un mouvement... Je choisis aléatoirement un mouvement parmi ceux possibles, j'exécute et je fais tourner jusqu'à qu'il n'y ait plus de possibilité. S'il reste à la fin plus de 1 bille, je recommence.

La première fois que j'ai exécuté une partie il y avait de quoi être découragé :

![](https://github.com/haagor/Solitaire/blob/main/img/doupt.png)

Mais bon il faut laisser du temps pour que la magie de l'aléatoire opère...

![](https://github.com/haagor/Solitaire/blob/main/img/stupid.png)

Ici ```.``` correspond à 1000 essais. Les chiffres ```3``` et ```2``` s'affichent pour indiquer qu'une partie s'est terminée avec ce nombre de billes. C’était censé être encourageant.

En attendant que ma machine travaille, je continue de secouer ce casse tête de mes mains. Pour augmenter les chances d’obtenir un nombre de billes restant qui soit bas, j’opte pour l’optimisation suivante : regarder le nombre de mouvements possibles qu’on pourra faire au tour suivant si on exécute un mouvement donnée. Je fais ce travail pour tous les mouvements possibles et je sélectionne les mouvements qui me laisseront le plus de choix au prochain tour. Ainsi, j'obtiens plus de résultats inférieurs à 4. En revanche, le temps pour exécuter une partie est devenu plus long. 

Je fais tourner ça toute la nuit :

![](https://github.com/haagor/Solitaire/blob/main/img/better.png)

Toujours rien ! A ce stade, il faut savoir qu'une partie totalement aléatoire à une chance de résoudre le jeu. Cependant, mon optimisation produit des exécutions qui ne sont plus 100% aléatoire et rend peut être la victoire impossible car en dehors de la stratégie pour résoudre ce jeu.

J'essaye de trouver d'autres optimisations. A force, je me rends compte qu'il ne s'agit pas de réduire simplement les billes à 1, mais plutôt de construire un schéma de quelques billes qui peuvent se réduire à 1 bille. J’essaye d’autres optimisations. Je secoue mon plateau en essayant de trouver le bon chemin. Rien.

Après quelques jours à tourner en rond, je craque, je regarde sur internet. Je tombe là-dessus :

![](https://github.com/haagor/Solitaire/blob/main/img/oups.png)

En fait, ça fait juste 27 ans que je vis dans le mensonge, sur cette variante de solitaire à 37 billes, retirer la bille du milieu rend le problème insoluble. Comme quoi, c’est pas parce que ça fait des années qu’on vous dit quelque chose que c’est vrai. Pour ma part, **la prochaine fois je lirai les specs jusqu’au bout**.
Du coup j’ai relancé ma machine avec ma première optimisation ! J’ai pas eu le temps de manger que ma machine criait déjà “VICTORY!”

![](https://github.com/haagor/Solitaire/blob/main/img/victory.png)

---

Simon P



