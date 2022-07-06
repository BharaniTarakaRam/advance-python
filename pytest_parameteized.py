#simple way

import mathlib

def test_squr1():
    sqr1=mathlib.clac_squ(5)
    assert sqr1 == 25

def test_squr2():
    sqr2=mathlib.clac_squ(2)
    assert sqr2 == 4


def test_squr3():
    sqr3=mathlib.clac_squ(9)
    assert sqr3 == 81


def test_squr4():
    sqr4=mathlib.clac_squ(3)
    assert sqr4 == 9


def test_squr5():
    sqr5=mathlib.clac_squ(10)
    assert sqr5 == 10



#-------------using parameteized method-------------------------------------------------

# import mathlib
# import pytest
#
# @pytest.mark.parametrize("num,output",
#                          [
#                              (5,25),
#                              (9,81),
#                              (10,100)
#
#                          ])
# def test_suqr(num,output):
#     result=mathlib.clac_squ(num)
#     assert  result==output


#--------------------with out using modles as mathlib(import mathlib)----------------------------
# import pytest
#
# @pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,33),(4,44)])
# def test_multiplication_11(num, output):
#    assert 11*num == output



