#!/usr/bin/env bash

var=0
python TranscriberExtracteur.py id2015_aug12.trs latin-1 -n turn -a speaker starttime endtime |
grep -v "\t$" |                             # exclusion des span sans texte
while read line
    do
        read name start end text <<< $line  # pour que cette ligne marche $line doit comporté quatre champs, soit trois "\t"
        duration=$(echo $end-$start|bc)     # sox prend un point de début et une durée donc end-start donne la durée
        ext="${name##*.}"                   # récupération de l'extention
        filename="${name%.*}"               # récupération du nom sans l'extention
        ((var++))                           # incrémentation de la variable var
        sox $filename.mp3 $filename\_$var.mp3 trim $start $duration   # exécution de sox
        echo "$name,$var,$text"
        echo "$text" >> "$filename.txt"     # on accumule dans un fichier txt la variable text (newline automatique)
    done
