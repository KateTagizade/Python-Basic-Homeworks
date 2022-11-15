#hello world!!

from unittest import TestCase

import pytest
from pytest import fixture
from solver import Solver

class SolverTestCase(TestCase):

    def setUp(self) -> None:
        self.solver = Solver (2,3)

    def test_add(self):
        solver = Solver(2,3)
        result = solver.add()
        self.assertEqual(5,result)

    def test_mul(self):
        solver = Solver(2, 3)
        result = solver.mul()
        self.assertEqual(6,result)

@fixture
def slvr():
    return Solver(2,3)

@fixture
def solver_mix(request):
    a,b = request.param
    solver = Solver(a,b)
    return solver


class TestSolver:
    @pytest.mark.parametrize(
        "a,b,expected_result",[
        [1,2,3],
        [2,3,5],
        [3,6,9],],
    )
    def test_add(self,a,b,expected_result):
        solver = Solver(a,b)
        #result = solver.add()
        assert solver.add() == expected_result

    @pytest.mark.parametrize("solver_mix, expected_result", [
        pytest.param([1,2],3),
        pytest.param([5, 6], 11)
    ], indirect=["solver_mix"])
    def test_add_extra(self, solver_mix: Solver, expected_result):
        assert solver_mix.add() == expected_result


    def test_mul(self):
        solver = Solver(2,3)
        result = solver.mul()
        assert result == 6

    def test_mul__raises(self):
        solver = Solver("a",3)
        with pytest.raises(TypeError) as exc_info:
            solver.mul()

        print(exc_info)
        assert str(exc_info.value) == solver.PARAMS_TYPE_EXC_TEXT