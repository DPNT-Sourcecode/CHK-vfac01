import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../lib'))


from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('AAA') == 130