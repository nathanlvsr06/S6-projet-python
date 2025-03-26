#!/usr/bin/env python3

''' Module proposant la classe FileDePriorite '''
from typing import TypeVar

T = TypeVar('T')

class FileDePriorite:
    ''' File qui gère la priorité des éléments à partir d'une fonction cle.

    arguments:
    - _file (list[T]): Liste des éléments triés selon leur priorité.
    - _cle (function): Fonction appliquée à chaque élément pour définir son ordre.
    '''
    def __init__(self, elements: tuple = (), cle = lambda e:e):
        ''' Initialise la file avec des éléments et une fonction cle.
        
        params:
        - elements (tuple[T], optionnel): Éléments initiaux à insérer dans la file.
        - cle (function, optionnel): Fonction utilisée pour comparer les éléments 
        (par défaut `lambda e: e`).
        '''
        self.cle = cle
        self.file = []
        for e in elements:
            self.enfiler(e)

    @property
    def est_vide(self):
        ''' Vérifie si la file est vide.

        returns:
        - bool: True si la file est vide, False sinon.
        '''
        return len(self.file)==0

    def enfiler(self, element: T):
        ''' Ajoute un élément dans la file en respectant l'ordre de priorité.

        params:
        - element (T): Élément à insérer.

        raises:
        - ElementNonComparableErreur : Levée si l'élément ne peut pas être comparé.
        '''
        self._verifier_element_comparable(self, element)
        self.file.append(element)
        self.file = sorted(self.file, key=self.cle)

    def defiler(self) -> T:
        ''' Retire et retourne l'élément le plus prioritaire de la file.

        returns:
        - T: Élément en tête de file.

        raises:
        - FileDePrioriteVideErreur : Levée si la file est vide.
        '''
        self._verifier_file_de_priorite_vide(self)
        return self.file.pop(0)

    @property
    def element(self):
        ''' Retourne l'élément le plus prioritaire sans le retirer de la file.

        returns:
        - T: Élément en tête de file.

        raises:
        - FileDePrioriteVideErreur : Levée si la file est vide.
        '''
        self._verifier_file_de_priorite_vide(self)
        return self.file[0]

    def __repr__(self):
        ''' Retourne une représentation formelle de la file de priorité.

        returns:
        - str: Représentation sous forme `FileDePriorite([...])`.
        '''
        return f"FileDePriorite({self.file})"

    def __str__(self):
        ''' Retourne une représentation informelle de la file de priorité.

        returns:
        - str: Chaîne contenant la liste des éléments triés.
        '''
        return f"{self.file}"

    def __iter__(self):
        ''' Permet d'itérer sur les éléments de la file de priorité.

        returns:
        - Iterator[T]: Itérateur sur les éléments triés.
        '''
        return iter(self.file)

    def __eq__(self, autre):
        ''' Vérifie si deux files de priorité sont équivalentes.

        params:
        - autre (FileDePriorite): L'autre file à comparer.

        returns:
        - bool: True si les files contiennent les mêmes éléments dans le même ordre, False sinon.
        '''
        if not isinstance(autre, self.__class__):
            return False
        return self.file == autre.file and self.cle == autre.cle

    @staticmethod
    def _verifier_file_de_priorite_vide(file):
        ''' Vérifie que la file de priorité n'est pas vide.

        raises:
        - FileDePrioriteVideErreur : Levée si la file est vide.
        '''
        if file.est_vide:
            raise FileDePrioriteVideErreur("La file de priorité est vide")

    @staticmethod
    def _verifier_element_comparable(file, element):
        ''' Vérifie que l'élément est comparable avec les autres éléments de la file.

        params:
        - element (T): Élément à vérifier.

        raises:
        - ElementNonComparableErreur : Levée si l'élément ne possède pas 
        les opérateurs de comparaison.
        '''
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
