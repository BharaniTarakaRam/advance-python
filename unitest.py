import mathlib
def test_calc_total():
   total=mathlib.calc_total(4,5)
   assert total == 9

def test_calc_multip():
   result=mathlib.calc_mul(10,3)
   assert result == 30
#
# output:unitest.py::test_calc_total PASSED                                       [ 50%]
# unitest.py::test_calc_multip PASSED                                      [100%]

# import mathlib
# import os
# import sys
# def test_calc_total():
#     total=mathlib.calc_total(4,5)
#     assert total == 9
# def test_calc_multip():
#     result=mathlib.calc_mul(10,3)
#     assert result == 30
# def test_calc_subs():
#     sub=mathlib.calc_sub(3,2)
#     assert sub == 1
#
# def test_calc_divde():
#     divs=mathlib.calc_div(3,2)
#     assert  divs == 1.5




#import mathlib
#def test_calc_total():
#    total=mathlib.calc_total(4,15)                           #error testcase is failed
#    assert total == 9
#def test_calc_multip():
#    result=mathlib.calc_mul(10,3)
#    assert result == 30

#output:unitest.py::test_calc_total FAILED                                       [ 50%]
#unitest.py:10 (test_calc_total)
#19 != 9

#Expected :9
#Actual   :19
#<Click to see difference>

#def test_calc_total():
#        total=mathlib.calc_total(4,15)
#>       assert total == 9
#E       assert 19 == 9

#unitest.py:13: AssertionError

#unitest.py::test_calc_multip PASSED                                      [100%]




#--------------------with out using modles as mathlib(import mathlib)----------------------------
# import pytest
# def test_add():
#     assert 2+2 == 4
#
# def test_sub():
#     assert 2-2 == 0
#
#
# def test_mul():
#     assert 2*2 == 4
#
# def test_squ():
#     assert 2**2 == 4


