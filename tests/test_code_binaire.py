#!/usr/bin/python3
# @u:file test_code_binaire.py

import pytest
from huffman.code_binaire import Bit, CodeBinaire, AuMoinsUnBitErreur
import copy

@pytest.fixture(scope="function")
def code_vide():
    return CodeBinaire()

@pytest.fixture(scope="function")
def code_non_vide():
    return CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_1)

@pytest.fixture(scope="function")
def code_non_vide2():
    return CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_1)

@pytest.fixture(scope="function")
def code_non_vide3():
    return CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)

@pytest.mark.parametrize("code_b1, code_b2, resultat",
                         [("code_vide", "code_vide", True),
                          ("code_vide", "code_non_vide", False),
                          ("code_non_vide", "code_non_vide2", True)
                        ])    
def test_eq(code_b1, code_b2, resultat, request):
    code_b1 = request.getfixturevalue(code_b1)
    code_b2 = request.getfixturevalue(code_b2)
    assert (code_b1 == code_b2) == resultat

def test_ajout_bit_a_la_fin(code_non_vide):
    code_non_vide.ajouter(Bit.BIT_1)
    assert code_non_vide == CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_1, Bit.BIT_1)

@pytest.mark.parametrize("code_b, resultat",
                         [("code_non_vide", Bit.BIT_0),
                          ("code_non_vide3", Bit.BIT_1),
                        ])  
def test_lecture_int(code_b, resultat, request):
    code_b = request.getfixturevalue(code_b)
    assert code_b[0] == resultat

@pytest.mark.parametrize("code_b, resultat",
                         [("code_non_vide", CodeBinaire(Bit.BIT_0, Bit.BIT_1)),
                          ("code_non_vide3", CodeBinaire(Bit.BIT_1, Bit.BIT_0)),
                        ])  
def test_lecture_slice(code_b, resultat, request):
    code_b = request.getfixturevalue(code_b)
    assert code_b[:2] == resultat

@pytest.mark.parametrize("code_b, resultat",
                         [("code_non_vide", CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_1)),
                          ("code_non_vide3", CodeBinaire(Bit.BIT_1, Bit.BIT_1, Bit.BIT_1)),
                        ])  
def test_ecriture_int(code_b, resultat, request):
    code_b = request.getfixturevalue(code_b)
    code_b[1] = Bit.BIT_1
    assert code_b == resultat

@pytest.mark.parametrize("code_b, resultat",
                         [("code_non_vide", CodeBinaire(Bit.BIT_0, Bit.BIT_0, Bit.BIT_0)),
                          ("code_non_vide3", CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_0)),
                        ]) 
def test_ecriture_slice(code_b, resultat, request):
    code_b = request.getfixturevalue(code_b)
    code_b[1:] = CodeBinaire(Bit.BIT_0, Bit.BIT_0)
    assert code_b == resultat

def test_ecriture_supp_slice(code_non_vide):
    code_non_vide[3:5] = (Bit.BIT_0, Bit.BIT_1)
    assert code_non_vide == CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)

@pytest.mark.parametrize("code_b, int, resultat",
                         [("code_non_vide", 1, CodeBinaire(Bit.BIT_0, Bit.BIT_1)),
                          ("code_non_vide3", 2, CodeBinaire(Bit.BIT_1, Bit.BIT_0)),
                        ]) 
def test_del_int(code_b, int, resultat, request):
    code_b = request.getfixturevalue(code_b)
    del(code_b[int])
    assert code_b == resultat


@pytest.mark.parametrize("code_b, slice, resultat",
                         [("code_non_vide", slice(1,3), CodeBinaire(Bit.BIT_0)),
                          ("code_non_vide3", slice(2), CodeBinaire(Bit.BIT_1)),
                        ]) 
def test_del_slice(code_b, slice, resultat, request):
    code_b = request.getfixturevalue(code_b)
    del(code_b[slice])
    assert code_b == resultat

@pytest.mark.parametrize("code_b1, code_b2, resultat",
                         [("code_non_vide", "code_non_vide3", 
                           CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_1, Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)),
                          ("code_non_vide3", "code_non_vide", 
                           CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1, Bit.BIT_0, Bit.BIT_1, Bit.BIT_1)),
                        ]) 
def test_plus(code_b1, code_b2, resultat, request):
    code_b1 = request.getfixturevalue(code_b1)
    code_b2 = request.getfixturevalue(code_b2)
    assert code_b1 + code_b2 == resultat

def test_plus_erreur(code_non_vide):
    with pytest.raises(TypeError):
        code_non_vide + [1]

def test_len(code_non_vide, code_non_vide3):
    codes = [code_non_vide, code_non_vide3, code_non_vide + code_non_vide3]
    resultats = [3, 3, 6]
    for code, resultat in zip(codes, resultats):
        assert len(code) == resultat

def test_au_moins_un_bit_erreur(code_non_vide):
    with pytest.raises(AuMoinsUnBitErreur):
        del(code_non_vide[:3])

@pytest.mark.parametrize("code_b, resultat",
                         [("code_non_vide", "CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_1)"),
                          ("code_non_vide3", "CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)"),
                        ])
def test_repr(code_b, resultat, request):
    code_b = request.getfixturevalue(code_b)
    assert repr(code_b) == resultat

@pytest.mark.parametrize("code_b, resultat",
                         [("code_non_vide", CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_1)),
                          ("code_non_vide3", CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1))
                        ])
def test_eval(code_b, resultat, request):
    code_b = request.getfixturevalue(code_b)
    assert eval(repr(code_b)) == resultat

@pytest.mark.parametrize("code_b, resultat",
                         [("code_non_vide", "011"),
                          ("code_non_vide3", "101")
                        ])
def test_str(code_b, resultat, request):
    code_b = request.getfixturevalue(code_b)
    assert str(code_b) == resultat
