#!/usr/bin/env python3

''' Module proposant la classe FileDePriorite '''
from typing import TypeVar

T = TypeVar('T')

class FileDePriorite:
    ''' File qui gère la priorité des éléments à partir d'une fonction cle

    arguments:
    elements -- tuple d'éléments à initialiser dans la file
    cle -- fonction de comparation des éléments dans la file
    '''
    def __init__(self, elements: tuple = (), cle = lambda e:e):
        ''' Initialise la file avec des éléments et une fonction cle '''
        self.cle = cle
        self.file = []
        for e in elements:
            self.enfiler(e)

    @property
    def est_vide(self):
        ''' Permet de savoir si la file est vide 
        
        resultat: un booleen qui renvoie True si la liste est vide, False sinon'''
        return len(self.file)==0

    def enfiler(self, element: T):
        ''' Permet d'enfiler un élément dans la file '''
        self._verifier_element_comparable(self, element)
        self.file.append(element)
        self.file = sorted(self.file, key=self.cle)

    def defiler(self) -> T:
        ''' Permet de défiler l'élément le plus prioritaire 
        
        resultat: l'élément qui est défilé'''
        self._verifier_file_de_priorite_vide(self)
        return self.file.pop(0)

    @property
    def element(self):
        ''' Permet d'obtenir l'élément le plus prioritaire sans le défiler
         
        resultat: l'élément le plus prioritaire '''
        self._verifier_file_de_priorite_vide(self)
        return self.file[0]

    def __repr__(self):
        return f"FileDePriorite({self.file})"

    def __str__(self):
        return f"{self.file}"

    def __iter__(self):
        return iter(self.file)

    def __eq__(self, autre):
        if not isinstance(autre, self.__class__):
            return False
        return self.file == autre.file and self.cle == autre.cle

    @staticmethod
    def _verifier_file_de_priorite_vide(file):
        if file.est_vide:
            raise FileDePrioriteVideErreur("La file de priorité est vide")

    @staticmethod
    def _verifier_element_comparable(file, element):
        try:
            _ = element < element #pylint: disable=comparison-with-itself
        except TypeError:
            raise ElementNonComparableErreur(f"La classe de {element} ne possède \
                                             pas les méthodes de comparaison") from None

        if not file.est_vide:
            try:
                _ = element < file.file[0]
            except TypeError:
                raise ElementNonComparableErreur(f"{element} ne peut être comparé aux \
                                                 éléments déjà présents dans la file") from None

class FileDePrioriteVideErreur(Exception):
    ''' Exception FileDePrioriteVideErreur qui est levée lorsqu'on essaye d'obtenir 
    ou défiler l'élément en tête d'une file vide
    '''

class ElementNonComparableErreur(Exception):
    ''' Exception ElementNonComparableErreur qui est levée lorsqu'on essaye d'ajouter un élément:
    - dont la classe ne possède pas les opérations de comparaison; 
    - qui ne peut pas être comparé avec les éléments déjà présents dans la file.
    '''
