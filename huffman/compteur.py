#!/usr/bin/env python3

""" Module proposant la classe Compteur """
from typing import TypeVar

T = TypeVar('T')

class Compteur:
    """ Compteur permet d'avoir des statistiques (nombre d'occurences) sur
des éléments hashables

    arguments:
    val_init -- dictionnaire(element, nb_occurences) qui permet d'initialiser
le compteur à sa création
    """
    def __init__(self, val_init: dict[T, int] = None):
        self.compteur = {}
        if val_init:
            self.compteur = dict(val_init.items())

    def incrementer(self, element: T) -> None:
        """ ajoute un element dans le compteur """
        if self.compteur:
            if element in self.compteur:
                self.compteur[element] += 1
            else:
                self.compteur[element] = 1
        else:
            self.compteur = {element: 1}

    def fixer(self, element: T, nb_occurences: int) -> None:
        """ fixe le nombre d'occurences de l'element à nb_occurences """
        if self.compteur:
            self.compteur[element] = nb_occurences
        else:
            self.compteur = {element: nb_occurences}

    def nb_occurrences(self, element: T) -> int:
        """ retourne le nombre d'occurences de l'element
        
        retourne: le nombre d'occurences (int)
        """
        if element in self.compteur:
            return self.compteur[element]
        return 0

    @property
    def elements(self) -> set[T]:
        """ retourne tous les elements dans le compteur
        
        retourne: un ensemble contenant les éléments"""
        return set(self.compteur.keys())

    def elements_nb_occurences(self, nb_occurences: int) -> set[T]:
        """ retourne tous les elements correspondant au nombre d'occurences

        resultat: un ensemble contenant les éléments
        """
        return set(e[0] for e in self.compteur.items() if e[1] == nb_occurences)

    def elements_moins_frequents(self) -> set[T]:
        """ retourne tous les elements les moins frequents

        resultat: un ensemble contenant les éléments les moins fréquents
        """
        if self.compteur.values():
            return self.elements_nb_occurences(min(self.compteur.values()))
        return set()

    def elements_plus_frequents(self) -> set[T]:
        """ retourne tous les elements les plus frequents

        resultat: un ensemble contenant les éléments les plus fréquents
        """
        if self.compteur.values():
            return self.elements_nb_occurences(max(self.compteur.values()))
        return set()

    def obtenir_cle(self, element: T) -> int:
        """ retourne le clé de l'element
        
        retourne: la clé
        """
        return [key for key, value in self.compteur.items() if value == element]

    def elements_par_nb_occurrences(self) -> dict[int, set[T]]:
        """retourne pour chaque nombre d'occurences présents dans compteur
    les éléments qui ont ces nombres d'occurences

        resultat: un dictionnaire dont les clés sont les nombres d'occurences
    et les valeurs des ensembles d'éléments qui ont ce nombre d'occurences"""
        resultat = {}
        for element, nb_occurences in self.compteur.items():
            if nb_occurences not in resultat:
                resultat[nb_occurences] = set()
            resultat[nb_occurences].add(element)
        return resultat

    def __repr__(self):
        return f"Compteur({self.compteur})"

    def __str__(self):
        return f"{self.compteur}"

def main():
    """Tests unitaires du module"""
    def ok_ko_en_str(booleen):
        return "OK" if booleen else "KO"

    def ok_ko(fct, resultat_attendu, *param):
        """mini fonction de TU"""
        res = fct.__name__ + ' : '
        res = res + ok_ko_en_str(fct(*param) == resultat_attendu)
        print(res)

    cpt1 = Compteur()
    cpt1.incrementer('a')
    cpt1.incrementer('a')
    cpt1.incrementer('b')
    cpt1.incrementer('c')
    cpt1.incrementer('c')
    cpt1.incrementer('c')
    cpt1.incrementer('d')

    ok_ko(Compteur.nb_occurrences, 2, cpt1, 'a')
    ok_ko(Compteur.elements, {'a', 'b', 'c', 'd'}, cpt1)
    ok_ko(Compteur.elements_moins_frequents, {'b', 'd'}, cpt1)
    ok_ko(Compteur.elements_plus_frequents, {'c'}, cpt1)
    ok_ko(Compteur.elements_par_nb_occurrences, {1: {'b', 'd'}, 2: {'a'}, 3: {'c'}}, cpt1)

if __name__ == "__main__":
    main()
