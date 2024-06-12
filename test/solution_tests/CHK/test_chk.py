import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../lib'))


from solutions.CHK import checkout


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3