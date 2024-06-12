import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../lib'))


from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('ABCDABA') == 210
        assert checkout_solution.checkout('AXYZ') == -1
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('AAAAA') == 230
        assert checkout_solution.checkout('AAAAAA') == 260
        assert checkout_solution.checkout('AAABBBB') == 220