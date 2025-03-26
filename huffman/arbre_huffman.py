#!/usr/bin/env python3

''' Module proposant la classe ArbreHuffman '''
class ArbreHuffman:
    ''' 
    Classe représentant un arbre de Huffman.

    arguments:
    - _element (optionnel): Élément stocké dans une feuille.
    - _nb_occurrences (int, optionnel): Nombre d'occurrences de l'élément 
                                        ou somme des occurrences des sous-arbres.
    - _fils_gauche (ArbreHuffman, optionnel): Sous-arbre gauche.
    - _fils_droit (ArbreHuffman, optionnel): Sous-arbre droit.
    '''
    def __init__(self, element=None, nb_occurrences: int = None, fils_gauche=None, fils_droit=None):
        ''' 
        Initialise un arbre de Huffman.

        params:
        - element: Élément stocké dans une feuille (obligatoire pour une feuille).
        - nb_occurrences (int): Nombre d'occurrences (obligatoire pour une feuille).
        - fils_gauche (ArbreHuffman): Fils gauche (obligatoire pour un nœud interne).
        - fils_droit (ArbreHuffman): Fils droit (obligatoire pour un nœud interne).

        raises:
        - ArbreHuffmanIncoherentErreur : Levée si les paramètres sont incohérents.
        '''
        if element and nb_occurrences and not (fils_gauche and fils_droit):
            self._element = element
            self._nb_occurrences = nb_occurrences
            self._fils_gauche = fils_gauche
            self._fils_droit = fils_droit
        elif fils_gauche and fils_droit and not (element and nb_occurrences):
            if fils_gauche == fils_droit:
                raise ArbreHuffmanIncoherentErreur(
                    "Le fils gauche et le fils droit sont identiques.")
            self._fils_gauche = fils_gauche
            self._fils_droit = fils_droit
            self._element = element
            self._nb_occurrences = fils_gauche.nb_occurrences + fils_droit.nb_occurrences
        else:
            raise ArbreHuffmanIncoherentErreur("Incohérence, création noeud et feuille.")

    @property
    def est_une_feuille(self):
        ''' 
        Vérifie si l'arbre Huffman est une feuille.

        returns:
        - True si l'arbre est une feuille, False sinon.
        '''
        return bool(self._element)

    @property
    def nb_occurrences(self):
        ''' 
        Retourne le nombre d'occurrences associées à cet arbre.

        returns:
        - int: Nombre d'occurrences.
        '''
        return self._nb_occurrences

    @property
    def element(self):
        ''' 
        Retourne l'élément stocké dans une feuille.

        returns:
        - : L'élement dans la feuille.

        raises:
        - DoitEtreUneFeuilleErreur : Levée si l'arbre n'est pas une feuille.
        '''
        if self._element:
            return self._element
        raise DoitEtreUneFeuilleErreur("Doit être une feuille.")

    @property
    def fils_gauche(self):
        ''' 
        Retourne le fils gauche d'un nœud interne.

        returns:
        - ArberHuffman: Le fils gauche.

        raises:
        - NeDoitPasEtreUneFeuilleErreur : Levée si l'arbre est une feuille.
        '''
        if self._fils_gauche:
            return self._fils_gauche
        raise NeDoitPasEtreUneFeuilleErreur("Ne doit pas être une feuille.")

    @property
    def fils_droit(self):
        ''' 
        Retourne le fils droit d'un nœud interne.

        returns:
        - ArberHuffman: Le fils droit.

        raises:
        - NeDoitPasEtreUneFeuilleErreur : Levée si l'arbre est une feuille.
        '''
        if self._fils_droit:
            return self._fils_droit
        raise NeDoitPasEtreUneFeuilleErreur("Ne doit pas être une feuille.")

    def equivalent(self, autre):
        ''' 
        Vérifie si deux arbres Huffman sont équivalents (structure et valeurs identiques).

        params:
        - autre (ArbreHuffman) : L'autre arbre Huffman à comparer.

        returns:
        - bool: True si les arbres sont équivalents, False sinon.
        '''
        if not isinstance(autre, ArbreHuffman):
            return False

        if self.est_une_feuille and autre.est_une_feuille:
            return self.nb_occurrences == autre.nb_occurrences and self.element == autre.element

        if not self.est_une_feuille and not autre.est_une_feuille:
            return (self.nb_occurrences == autre.nb_occurrences and
                    self.fils_gauche.equivalent(autre.fils_gauche) and
                    self.fils_droit.equivalent(autre.fils_droit))

        return False

    def __gt__(self, autre):
        ''' Vérifie si l'arbre a plus d'occurrences qu'un autre arbre Huffman. '''
        return self.nb_occurrences > autre.nb_occurrences

    def __ge__(self, autre):
        ''' Vérifie si l'arbre a un nombre d'occurrences 
        supérieur ou égal à un autre arbre Huffman. '''
        return self.nb_occurrences >= autre.nb_occurrences

    def __lt__(self, autre):
        ''' Vérifie si l'arbre a moins d'occurrences qu'un autre arbre Huffman. '''
        return self.nb_occurrences < autre.nb_occurrences

    def __le__(self, autre):
        ''' Vérifie si l'arbre a un nombre d'occurrences 
        inférieur ou égal à un autre arbre Huffman. '''
        return self.nb_occurrences <= autre.nb_occurrences

    def __add__(self, autre):
        ''' Fusionne deux arbres Huffman en un seul. '''
        return ArbreHuffman(fils_gauche = self, fils_droit = autre)

    def __repr__(self):
        ''' Retourne une représentation textuelle formelle de l'arbre Huffman. '''
        if self.est_une_feuille:
            return f"ArbreHuffman(element={self.element}, nb_occurrences={self.nb_occurrences})"
        return f"ArbreHuffman(fils_gauche={self.fils_gauche}, fils_droit={self.fils_droit})"

    def __str__(self):
        ''' Retourne une représentation informelle de l'arbre Huffman. '''
        if self.est_une_feuille:
            return f"Feuille(element={self.element}, nb_occurrences={self.nb_occurrences})"
        return f"Noeud(nb_occurrences={self.nb_occurrences}, fils_gauche={self.fils_gauche},\
        fils_droit={self.fils_droit})"

class ArbreHuffmanErreur(Exception):
    """ Exception levée lorsqu'il y a une erreur sur la gestion d'un arbre Huffman ."""

class DoitEtreUneFeuilleErreur(ArbreHuffmanErreur):
    """ Exception levée lorsqu'on appelle une méthode/propriété 
    uniquement possible pour une feuille. """

class NeDoitPasEtreUneFeuilleErreur(ArbreHuffmanErreur):
    """ Exception levée lorsqu'on appelle une méthode/propriété 
    uniquement possible pour un noeid non feuille."""

class ArbreHuffmanIncoherentErreur(ArbreHuffmanErreur):
    """ Exception levée lorsqu'il y a une incohérence sur la création d'un arbre Huffman. """
