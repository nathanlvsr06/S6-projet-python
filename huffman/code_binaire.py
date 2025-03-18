#!/usr/bin/env python3

''' Module proposant la classe CodeBinaire '''
from enum import Enum, auto

class Bit(Enum):
    ''' Représente un bit en tant qu'énumération. '''
    BIT_0 = auto()
    BIT_1 = auto()

    def __repr__(self):
        ''' Retourne une représentation textuelle détaillée du bit. 
        
        returns:
        - str: Nom de l'énumération sous forme `Bit.BIT_0` ou `Bit.BIT_1`.
        '''
        cls_name = self.__class__.__name__
        return f"{cls_name}.{self.name}"

    def __str__(self):
        ''' Retourne la valeur du bit sous forme de chaîne de caractères. 
        
        returns:
        - str: `"BIT_0"` ou `"BIT_1"`.
        '''
        return f"{self.name}"

class CodeBinaire:
    '''Classe représentant un code binaire constitué de bits.
    
    arguments:
    - _bits (list[Bit]): Liste des bits constituant le code binaire.
    '''

    def __init__(self, *bits):
        ''' Initialise un CodeBinaire à partir de bits.

        params:
        - bits: Séquence de Bit à ajouter au code binaire.
        
        raises:
        TypeError: levée si un élément n'est pas un Bit.
        '''
        self._verifier_type_bits(bits)
        self._bits = list(bits)

    @property
    def bits(self):
        ''' Retourne les bits sous forme de tuple. 
        
        returns:
        - tuple[Bit]: Séquence des bits du CodeBinaire.
        '''
        return tuple(self._bits)

    def ajouter(self, bit):
        ''' Ajoute un bit au CodeBinaire. 
        
        params:
        - bit: Le bit à ajouter.
        
        raises:
        - TypeError: Levée si l'élément ajouté n'est pas un Bit.
        '''
        self._verifier_type_bits([bit])
        self._bits.extend([bit])

    def __len__(self):
        ''' Retourne la longueur du CodeBinaire (nombre de bits).
         
        returns:
        - int: Nombre de bits du CodeBinaire.
        '''
        return len(self._bits)

    def __add__(self, other):
        ''' Concatène deux `CodeBinaire` pour en former un nouveau.

        params:
        - other (CodeBinaire): CodeBinaire à concaténer.

        returns:
        - CodeBinaire: Nouveau CodeBinaire contenant les bits des deux codes.

        raises:
        - TypeError : Levée si `other` n'est pas un `CodeBinaire`.
        '''
        self._verifier_type_bits(other)
        return CodeBinaire(*self._bits, *other._bits)

    def __getitem__(self, index):
        ''' Accède à un ou plusieurs bits du CodeBinaire.

        params:
        - index: Index ou slice.
        
        returns:
        - Bit: Si `index` est un entier.
        - CodeBinaire: Si `index` est un `slice`.
        '''
        if isinstance(index, slice):
            return CodeBinaire(*self._bits[index])
        return self._bits[index]

    def __setitem__(self, index, value):
        ''' Modifie un ou plusieurs bits du CodeBinaire.

        params:
        - index (int | slice): Index ou slice à modifier.
        - value (Bit | list[Bit] | CodeBinaire): Nouveau(s) bit(s) ou CodeBinaire.
        '''
        if isinstance(index, slice):
            if isinstance(value, CodeBinaire):
                self._bits[index] = list(value._bits)
            else:
                self._bits[index] = list(value)
        else:
            self._bits[index] = value

    def __delitem__(self, index):
        ''' Supprime un ou plusieurs bits du CodeBinaire.

        params:
        - index (int | slice): Index ou slice des bits à supprimer.

        raises:
        - AuMoinsUnBitErreur: Levée si le code binaire est nul après suppression.
        '''
        self._verifier_au_moins_un_bit(self, index)
        del self._bits[index]

    def __repr__(self):
        ''' Retourne une représentation formelle du CodeBinaire.
        
        returns:
        - str: Représentation sous forme `CodeBinaire(Bit.BIT_0, Bit.BIT_1)`.
        '''
        return f"CodeBinaire{self.bits}"

    def __str__(self):
        ''' Retourne la représentation binaire sous forme de chaîne de caractères.

        returns:
        - str: Chaîne binaire correspondant aux bits du CodeBinaire.
        '''
        return "".join("0" if bit == Bit.BIT_0 else "1" for bit in self._bits)

    def __iter__(self):
        ''' Permet d'itérer sur les bits du CodeBinaire.
        
        returns:
        - Iterator[Bit]: Itérateur sur les bits.
        '''
        return iter(self._bits)

    def __eq__(self, other):
        ''' Vérifie l'égalité entre deux CodeBinaire.

        params:
        - other (CodeBinaire): L'autre CodeBinaire à comparer.

        returns:
        - bool: True si les codes sont identiques, False sinon.
        '''
        if not isinstance(other, CodeBinaire):
            return False
        return self.bits == other.bits

    @staticmethod
    def _verifier_type_bits(bits):
        ''' Vérifie que tous les éléments sont du type Bit.

        params:
        - bits (list[Bit] | tuple[Bit]): Séquence de bits à vérifier.
        
        raises:
        - TypeError : Levée si un élément n'est pas un `Bit`.
        '''
        if not all(isinstance(bit, Bit) for bit in bits):
            raise TypeError("Un CodeBinaire ne peut être construit qu'à partir de Bit")

    @staticmethod
    def _verifier_au_moins_un_bit(bits, index):
        ''' Vérifie que le CodeBinaire est composé d'au moins un bit.

        params:
        - index (int | slice): Index unique ou tranche (`slice`).

        raises:
        - AuMoinsUnBitErreur : Levée si la suppression rend le CodeBinaire vide.
        '''
        if isinstance(index, slice):
            length = index.stop - index.start if index.start else index.stop
            if len(bits.bits) - length <= 0:
                raise AuMoinsUnBitErreur("Un CodeBinaire doit contenir au moins un bit.")
        else:
            # Vérifier si la suppression laisse le code binaire vide
            if len(bits.bits) == 1:
                raise AuMoinsUnBitErreur("Un CodeBinaire doit contenir au moins un bit.")

class AuMoinsUnBitErreur(Exception):
    '''Exception levée lorsqu'un CodeBinaire devient vide.'''
