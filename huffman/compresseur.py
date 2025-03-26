#!/usr/bin/env python3
""" script principal du module """
from typing import Dict
import io
import logging
from huffman.compteur import Compteur
from huffman.arbre_huffman import ArbreHuffman
from huffman.file_de_priorite import FileDePriorite
from huffman.code_binaire import CodeBinaire, Bit

LOGGER = logging.getLogger()

NB_OCTETS_CODAGE_INT = 4

def statistiques(source: io.BufferedReader) -> (Compteur, int):
    """ fonction qui retourne le nombre d'occurences (Compteur)
d'un flux d'octets et ainsi que le nombre d'octets"""
# @u:start statistiques

    taille = 0
    compteur = Compteur()
    BUFFER_SIZE = 4096
    while (chunk := source.read(BUFFER_SIZE)):  # Lecture par blocs
        taille += len(chunk)  # Comptabilisation du nombre total d'octets
        for octet in chunk:  # Parcours des octets du chunk
            compteur.incrementer(octet)

    return compteur, taille

# @u:end statistiques

def arbre_de_huffman(stat: Compteur) -> ArbreHuffman:
    """ fonction qui retourne un arbre d'huffman à partir d'un compteur """
# @u:start arbre_de_huffman

    pass

# @u:end arbre_de_huffman

def codes_binaire(abr: ArbreHuffman) -> Dict[int, CodeBinaire]:
    """ fonction qui retourne le code binaire de tous les éléments
d'un arbre d'Huffman """
# @u:start code_binaire

    pass

# @u:end code_binaire

if __name__ == "__main__":
    pass
