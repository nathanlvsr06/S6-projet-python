#!/usr/bin/env python3

''' Module proposant la classe CodeBinaire '''
from enum import Enum, auto

class Bit(Enum):
    """ Représente un bit en tant qu'énumération. """
    BIT_0 = auto()
    BIT_1 = auto()

    def __repr__(self):
        """ Retourne une représentation textuelle détaillée du bit. """
        cls_name = self.__class__.__name__
        return f"{cls_name}.{self.name}"

    def __str__(self):
        """ Retourne la valeur du bit sous forme de chaîne de caractères. """
        return f"{self.name}"

class CodeBinaire:
    """Classe représentant un code binaire constitué de bits."""

    def __init__(self, *bits):
        """ Initialise un CodeBinaire à partir de bits.

        params:
        - bits: Séquence de Bit à ajouter au code binaire.
        
        raises:
        TypeError: Si un élément n'est pas un Bit.
        """
        self._verifier_type_bits(bits)
        self._bits = list(bits)

    @property
    def bits(self):
        """ Retourne les bits sous forme de tuple. """
        return tuple(self._bits)

    def ajouter(self, bit):
        """ Ajoute un bit au CodeBinaire. 
        
        param:
        - bit: Le bit à ajouter.
        
        raises:
        - TypeError: Si l'élément ajouté n'est pas un Bit.
        """
        self._verifier_type_bits([bit])
        self._bits.extend([bit])

    def __len__(self):
        """ Retourne la longueur du CodeBinaire (nombre de bits). """
        return len(self._bits)

    def __add__(self, other):
        """ Concaténation de deux CodeBinaire. """
        self._verifier_type_bits(other)
        return CodeBinaire(*self._bits, *other._bits)

    def __getitem__(self, index):
        """ Accède à un ou plusieurs bits du CodeBinaire.

        param:
        - index: Index ou slice.
        
        return:
        - Un bit ou un CodeBinaire.
        """
        if isinstance(index, slice):
            return CodeBinaire(*self._bits[index])
        return self._bits[index]

    def __setitem__(self, index, value):
        """ Modifie un ou plusieurs bits du CodeBinaire.

        params:
        - index: Index ou slice à modifier.
        - value: Nouveau(s) bit(s) ou CodeBinaire.
        """
        if isinstance(index, slice):
            if isinstance(value, CodeBinaire):
                self._bits[index] = list(value._bits)
            else:
                self._bits[index] = list(value)
        else:
            self._bits[index] = value

    def __delitem__(self, index):
        """ Supprime un ou plusieurs bits du CodeBinaire.

        param:
        - index: Index ou slice des bits à supprimer.

        raises:
        - AuMoinsUnBitErreur: si le code binaire est nul après suppression.
        """
        self._verifier_au_moins_un_bit(self, index)
        del self._bits[index]
        

    def __repr__(self):
        """ Retourne une représentation détaillée du CodeBinaire. """
        return f"CodeBinaire{self.bits}"

    def __str__(self):
        """ Retourne la représentation binaire sous forme de chaîne de caractères. """
        return "".join("0" if bit == Bit.BIT_0 else "1" for bit in self._bits)

    def __iter__(self):
        """ Permet d'itérer sur les bits du CodeBinaire. """
        return iter(self._bits)

    def __eq__(self, other):
        """ Vérifie l'égalité entre deux CodeBinaire.

        param:
        - other: L'autre CodeBinaire à comparer.

        return:
        - True si les codes sont identiques, False sinon.
        """
        if not isinstance(other, CodeBinaire):
            return False
        return self.bits == other.bits

    @staticmethod
    def _verifier_type_bits(bits):
        """ Vérifie que tous les éléments sont du type Bit.

        param:
        - bits: Une liste ou un tuple de bits à vérifier.
        
        raises:
        - TypeError: Si un élément n'est pas un Bit.
        """
        if not all(isinstance(bit, Bit) for bit in bits):
            raise TypeError("Un CodeBinaire ne peut être construit qu'à partir de Bit")

    @staticmethod
    def _verifier_au_moins_un_bit(bits, index):
        """ Vérifie que le CodeBinaire est composé d'au moins un bit.

        param:
        - bits: Une liste ou un tuple de bits à vérifier.
        
        raises:
        - AuMoinsUnBitErreur: Si il y a aucun bit dans le code binaire.
        """
        if isinstance(index, slice):
            length = index.stop - index.start if index.start else index.stop
            if len(bits._bits) - length <= 0:
                raise AuMoinsUnBitErreur("Un CodeBinaire doit contenir au moins un bit.")
        else:
            # Vérifier si la suppression laisse le code binaire vide
            if len(bits._bits) == 1:
                raise AuMoinsUnBitErreur("Un CodeBinaire doit contenir au moins un bit.")

class AuMoinsUnBitErreur(Exception):
    """Exception levée lorsqu'un CodeBinaire devient vide."""
