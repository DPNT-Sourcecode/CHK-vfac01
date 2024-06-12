import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../lib'))


from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('ABCDABA') == 210
        assert checkout_solution.checkout('AXYZ') == 95
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('AAAAA') == 200
        assert checkout_solution.checkout('AAAAAA') == 250
        assert checkout_solution.checkout('AAABBBB') == 220
        assert checkout_solution.checkout('AAABBBCCDD') == 275
        assert checkout_solution.checkout('EEEE') == 160
        assert checkout_solution.checkout('EEBB') == 110
        assert checkout_solution.checkout('EEEEBB') == 160
        assert checkout_solution.checkout('EEEEB') == 160
        assert checkout_solution.checkout('FFFFF') == 40
        assert checkout_solution.checkout('FFF') == 20
        assert checkout_solution.checkout('FF') == 20
        assert checkout_solution.checkout('FFFF') == 30
        assert checkout_solution.checkout('JIGHHLMOSTWHHH') == 345
        assert checkout_solution.checkout('JIGHHLMOSTWHHHHHHHH') == 380
        assert checkout_solution.checkout('KKKQQQQVV') == 430
        assert checkout_solution.checkout('NNNMM') == 135
        assert checkout_solution.checkout('UUUU') == 120
        assert checkout_solution.checkout('RRRQ') == 150
        assert checkout_solution.checkout('STX') == 45
        assert checkout_solution.checkout('SSS') == 45
        assert checkout_solution.checkout('STYXZ') == 75
     