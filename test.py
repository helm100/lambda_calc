#!/usr/bin/env python3
from Class_Lambda import functie
from Class_Lambda import expr
from str_to_expr import str_to_expr
#from terminal.py import ...
import unittest

class Test_str_to_expr(unittest.TestCase):

    def test_simple_expr(self):
        self.assertEqual("(labc.aabbcc)", str(str_to_expr("(labc.aabbcc)")))

    def test_complex_expr(self):
        self.assertEqual("(z(lpq.q)((lxy.(labc.aabbcc)xy)(labc.aabbcc)s))", str(str_to_expr("(z(lpq.q)((lxy.(labc.aabbcc)xy)(labc.aabbcc)s))")))



class Test_equal(unittest.TestCase):

		
	def test_simple(self):
		functie1 = functie(["a", "b", "c"], ["a", "a", "b", "b", "c", "c"])
		functie2 = functie(["x", "y"], [functie1, "x", "y"])
		functie3 = functie(["p", "q"], ["q"])
		expr1 = expr([functie1])
		expr2 = expr(["z", functie3, expr([functie2, functie1, "s"])])
		self.assertTrue(expr1==expr1)
		self.assertFalse(expr1==expr2)

if __name__ == '__main__':
    unittest.main()




