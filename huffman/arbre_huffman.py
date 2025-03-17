#!/usr/bin/env python3

''' Module proposant la classe ArbreHuffman '''
class ArbreHuffman:
    def __init__(self, element=None, nb_occurences: int = None, fils_gauche=None, fils_droit=None):
        if element and nb_occurences and not (fils_gauche and fils_droit):
            self._element = element
            self._nb_occurences = nb_occurences
            self._fils_gauche = fils_gauche
            self._fils_droit = fils_droit
        if not (element and nb_occurences and not (fils_gauche and fils_droit)):
            raise ArbreHuffmanIncoherentErreur("Incohérence, création noeud et feuille.")
        if fils_gauche and fils_droit and not (element and nb_occurences):
            if fils_gauche == fils_droit:
                raise ArbreHuffmanIncoherentErreur("Le fils gauche et le fils droit sont identiques.")
            self._fils_gauche = fils_gauche
            self._fils_droit = fils_droit
            self._element = element
            self._nb_occurences = fils_gauche.nb_occurences + fils_droit.nb_occurences
        if not (fils_gauche and fils_droit and not (element and nb_occurences)):
            raise ArbreHuffmanIncoherentErreur("Incohérence, création noeud et feuille.")


    @property
    def est_une_feuille(self):
        return bool(self._element)

    @property
    def nb_occurences(self):
        return self._nb_occurences

    @property
    def element(self):
        if self._element:
            return self._element
        raise DoitEtreUneFeuilleErreur("Doit être une feuille.")
    
    @property
    def fils_gauche(self):
        if self._fils_gauche:
            return self._fils_gauche
        raise NeDoitPasEtreUneFeuilleErreur("Ne doit pas être une feuille.")
    
    @property
    def fils_droit(self):
        if self._fils_droit:
            return self._fils_droit
        raise NeDoitPasEtreUneFeuilleErreur("Ne doit pas être une feuille.")
    
    def equivalent(self, autre):
        if not isinstance(autre, ArbreHuffman):
            return False
        
        if self.est_une_feuille and autre.est_une_feuille:
            return self.nb_occurences == autre.nb_occurences and self.element == autre.element
        
        if not self.est_une_feuille and not autre.est_une_feuille:
            return (self.nb_occurences == autre.nb_occurences and
                    self.fils_gauche.equivalent(autre.fils_gauche) and
                    self.fils_droit.equivalent(autre.fils_droit))
        
    def __gt__(self, autre):
        return self.nb_occurences > autre.nb_occurences

    def __ge__(self, autre):
        return self.nb_occurences >= autre.nb_occruences
    
    def __lt__(self, autre):
        return self.nb_occurences < autre.nb_occruences
    
    def __le__(self, autre):
        return self.nb_occurences <= autre.nb_occruences
    
    def __add__(self, autre):
        return ArbreHuffman(fils_gauche = self, fils_droit = autre)
    
    def __repr__(self):
        if self.est_une_feuille:
            return f"ArbreHuffman(element={self.element}, nb_occurences={self.nb_occurences})"
        return f"ArbreHuffman(fils_gauche={self.fils_gauche}, fils_droit={self.fils_droit})"

    def __str__(self):
        if self.est_une_feuille:
            return f"Feuille(element={self.element}, nb_occurences={self.nb_occurences})"
        return f"Noeud(nb_occurences={self.nb_occurences}, fils_gauche={self.fils_gauche},\
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