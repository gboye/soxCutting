# coding: utf-8

from bs4 import BeautifulSoup as bs
import sys


class TranscriberExtracteur:
    """
        Cette classe permet potentiellement d'extraire n'importe quelle information d'un fichier trs

    """
    def __init__(self, xmlFile):
        if not xmlFile.endswith(".xml"):
            raise TypeError("Le fichier fourni doit être au format xml.")
        self.entree = bs(open(xmlFile))

    def extraireTemps(self, noeud="Turn", attributs=("startTime", "endTime")):
        """
            Fonction cherchant les bornes temporels d'un fichier TRS.
            Parmi toutes les balises 'noeud' je cherche les attributs 'attributs'
        :param noeud:
        :param attributs:
        :return: None
        """
        temps = self.entree.find_all(noeud)

        for debut, fin in map(lambda x: (x.get(attributs[0]), x.get(attributs[1])), temps):
            yield debut, fin

    def xml2db(self):
        """
            On transforme le fichier xml d'entrée en bases relationnelles
        :return:
        """


def extraire():
    import argparse

    parser = argparse.ArgumentParser(
        prog="extraire",
        description="""
            A partir d'un fichier xml, on sort telle ou telle information
            On sort l'information en format csv.
            du coup on peut multiplier la sortie.
        """
    )

    parser.add_argument(
        "xmlfile"
    )

    parser.add_argument(
        "input_encoding"
    )

    parser.add_argument(
        "-n",
        "-noeud",
        action="append"
    )

    parser.add_argument(
        "-a",
        "--attributes",
        nargs="+",
        action="append"
    )

    parser.add_argument(
        "-f",
        "--separator"
    )

    args = parser.parse_args()

    with open(args.xmlfile, mode='r', encoding=args.input_encoding) as filex:
        soup = bs(filex, "lxml")

    for element in zip(args.n, args.attributes):
        (node, (speaker, start, end)) = element
        for x in soup.find_all(dict([element])):
            sys.stdout.write(
                '\t'.join(
                    [
                        args.xmlfile, x.get(start),
                        x.get(end),
                        "|".join(filter(str, x.text.split('\n')))
                    ]
                ) + "\n"
            )


if __name__ == '__main__':
    extraire()
