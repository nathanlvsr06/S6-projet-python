#!/usr/bin/env python3

''' Module proposant la classe Compteur '''
from typing import TypeVar

T = TypeVar('T')

class Compteur:
    ''' Compteur permet d'avoir des statistiques (nombre d'occurrences)
    sur des éléments hashables.

    arguments:
    - _compteur (dict[T, int]): Dictionnaire stockant les éléments
    et leurs occurrences.
    '''
    def __init__(self, val_init: dict[T, int] = None):
        ''' Initialise un compteur avec des éléments et leurs occurrences.

        params:
        - val_init (dict[T, int], optionnel): Dictionnaire contenant des éléments 
        et leurs occurrences initiales.
        '''
        self.compteur = {}
        if val_init:
            self.compteur = dict(val_init.items())

    def incrementer(self, element: T) -> None:
        ''' Ajoute un élément dans le compteur ou incrémente son occurrence.

        params:
        - element (T): Élément à ajouter ou incrémenter.
        '''
        if self.compteur:
            if element in self.compteur:
                self.compteur[element] += 1
            else:
                self.compteur[element] = 1
        else:
            self.compteur = {element: 1}

    def fixer(self, element: T, nb_occurrences: int) -> None:
        ''' Fixe le nombre d'occurrences d'un élément.

        params:
        - element (T): Élément dont on veut fixer l'occurrence.
        - nb_occurrences (int): Nombre d'occurrences à attribuer.
        '''
        if self.compteur:
            self.compteur[element] = nb_occurrences
        else:
            self.compteur = {element: nb_occurrences}

    def nb_occurrences(self, element: T) -> int:
        ''' Retourne le nombre d'occurrences d'un élément.

        params:
        - element (T): Élément à rechercher.

        returns:
        - int: Nombre d'occurrences de l'élément (0 s'il est absent).
        '''
        if element in self.compteur:
            return self.compteur[element]
        return 0

    @property
    def elements(self) -> set[T]:
        ''' Retourne tous les éléments présents dans le compteur.

        returns:
        - set[T]: Ensemble des éléments enregistrés.
        '''
        return set(self.compteur.keys())

    def elements_nb_occurrences(self, nb_occurrences: int) -> set[T]:
        ''' Retourne tous les éléments correspondant à un nombre d'occurrences donné.

        params:
        - nb_occurrences (int): Nombre d'occurrences recherché.

        returns:
        - set[T]: Ensemble des éléments ayant ce nombre d'occurrences.
        '''
        return set(e[0] for e in self.compteur.items() if e[1] == nb_occurrences)

    def elements_moins_frequents(self) -> set[T]:
        ''' Retourne les éléments les moins fréquents dans le compteur.

        returns:
        - set[T]: Ensemble des éléments ayant le plus faible nombre d'occurrences.
        '''
        if self.compteur.values():
            return self.elements_nb_occurrences(min(self.compteur.values()))
        return set()

    def elements_plus_frequents(self) -> set[T]:
        ''' Retourne les éléments les plus fréquents dans le compteur.

        returns:
        - set[T]: Ensemble des éléments ayant le plus grand nombre d'occurrences.
        '''
        if self.compteur.values():
            return self.elements_nb_occurrences(max(self.compteur.values()))
        return set()

    def obtenir_cle(self, element: T) -> int:
        ''' Retourne la liste des clés correspondant à un nombre d'occurrences donné.

        params:
        - element (T): Nombre d'occurrences recherché.

        returns:
        - list[int]: Liste des clés associées à ce nombre d'occurrences.
        '''
        return [key for key, value in self.compteur.items() if value == element]

    def elements_par_nb_occurrences(self) -> dict[int, set[T]]:
        ''' 
        Retourne un dictionnaire regroupant les éléments par nombre d'occurrences.

        returns:
        - dict[int, set[T]]: Dictionnaire dont les clés sont les nombres d'occurrences 
        et les valeurs sont des ensembles d'éléments ayant ces occurrences.
        '''
        resultat = {}
        for element, nb_occurrences in self.compteur.items():
            if nb_occurrences not in resultat:
                resultat[nb_occurrences] = set()
            resultat[nb_occurrences].add(element)
        return resultat
    
    def __eq__(self, autre):
        if isinstance(autre, Compteur):
            return self.compteur == autre.compteur
        return False

    def __repr__(self):
        ''' Retourne une représentation formelle du compteur.

        returns:
        - str: Représentation sous forme `Compteur({...})`.
        '''
        return f"Compteur({self.compteur})"

    def __str__(self):
        ''' Retourne une représentation informelle du compteur.

        returns:
        - str: Chaîne contenant le dictionnaire des occurrences.
        '''
        return f"{self.compteur}"
