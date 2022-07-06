# import mathlib
# import pytest
# import sys
#
# @pytest.mark.skip(reason="i dont want to ru the code")
# def test_calc_total():
#     total=mathlib.calc_total(4,5)
#     assert total == 9
#
# def test_calc_multil():
#     result =mathlib.calc_mul(10,3)
#     assert result == 30

# output:unittest_skip.py::test_calc_total SKIPPED (i dont want to ru the code)   [ 50%]
# Skipped: i dont want to ru the code
#
# unittest_skip.py::test_calc_multil PASSED                                [100%]
#

#-----------------------------skipif-------------------------------------
# import mathlib
# import pytest
# import sys
#
# @pytest.mark.skipif(sys.version_info <(3,10),reason="i dont want to run the code")
# def test_calc_total():
#     total=mathlib.calc_total(4,5)
#     assert total == 9
#
#
# def test_calc_multil():
#     result =mathlib.calc_mul(10,3)
#     assert result == 30
#     print(result)

# outPut:unittest_skip.py::test_calc_total SKIPPED (i dont want to run the code)  [ 50%]
# Skipped: i dont want to run the code
#
# unittest_skip.py::test_calc_multil PASSED                                [100%]30


# import mathlib
# import pytest
# import sys
#
# @pytest.mark.skipif(sys.version_info >(3,10),reason="i dont want to run the code")
# def test_calc_total():
#     total=mathlib.calc_total(4,5)
#     assert total == 9
#
#
# def test_calc_multil():
#     result =mathlib.calc_mul(10,3)
#     assert result == 30
#     print(result)

# output:unittest_skip.py::test_calc_total PASSED                                 [ 50%]
# unittest_skip.py::test_calc_multil PASSED                                [100%]30
# passed becaues python -version was 3.9.3 so if condition has passerd version is less than (3,10)



#--------------test run with name---------------------------

import mathlib
import pytest

@pytest.mark.total
def test_calc_total():
    total=mathlib.calc_total(4,5)
    assert total == 9

@pytest.mark.multil
def test_calc_multil():
    result =mathlib.calc_mul(10,3)
    assert result == 30


#--------------------with out using modles as mathlib(import mathlib)----------------------------

