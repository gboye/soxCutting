# soxCutting ou extractor

Deux facettes:
    La première, c'est l'extraction d'information d'un fichier xml
    La seconde, c'est le découpage d'un son enplus petits segments

<code>sh soxCutting.sh</code>

Cette commande execute <code>TranscriberExtracteur.py</code>
sur un fichier exemple puis pipe la sortie sur sox.

Ce script ne modifie en rien le fichier son mais le son doit avoir
le même nom que le fichier xml passé en argument
à <code>TranscriberExtracteur.py</code>

Le coeur de la fonction reste l'extraction.


##### A suivre:
###### xml2db:
        transformer une structure XML en tables SQL.
    en ayant ce genre d'outils, on peut alors faire n'importe
    quelle table à partir de cette transformation