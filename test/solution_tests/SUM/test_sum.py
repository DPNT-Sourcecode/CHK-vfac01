import sys
if "D:\runner\runner-for-python-windows\accelerate_runner\lib" not in sys.path:
    sys.path.append("D:\runner\runner-for-python-windows\accelerate_runner\lib")
from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
