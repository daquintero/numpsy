import unittest
import numpy as np
import numpsy as nsy

class TestHelpers(unittest.TestCase):

    def test_select_available_property_(self):
        self.assertEqual(nsy.helpers.__select_available_property__("first", "default", "default"), "first")
        self.assertEqual(nsy.helpers.__select_available_property__("default", "second", "default"), "second")
        self.assertEqual(nsy.helpers.__select_available_property__("default",
                                                                   "default",
                                                                   "default",
                                                                   "optional"),
                         "optional")
        self.assertEqual(nsy.helpers.__select_available_property__("default",
                                                                   "default",
                                                                   "default",
                                                                   "default",
                                                                   "optional"
                                                                   ),
                         "optional")
        self.assertEqual(nsy.helpers.__select_available_property__(nsy.configuration.undefined_unit_symbol,
                                                                   nsy.configuration.undefined_unit_symbol,
                                                                   nsy.configuration.undefined_unit_symbol),
                         nsy.configuration.undefined_unit_symbol)
        self.assertEqual(nsy.helpers.__select_available_property__(nsy.configuration.undefined_unit_symbol,
                                                                   nsy.configuration.undefined_unit_symbol,
                                                                   nsy.configuration.undefined_unit_symbol,
                                                                   nsy.configuration.undefined_unit_symbol),
                         nsy.configuration.undefined_unit_symbol)
        self.assertEqual(nsy.helpers.__select_available_property__("",
                                                                   "",
                                                                   "default"),
                         "default")


class TestConfiguration(unittest.TestCase):

    def test_defaults(self):
        self.assertEqual("Ø", nsy.configuration.undefined_value_symbol)
        # TODO

class TestCore(unittest.TestCase):

    def test_default_initialization(self):
        self.unit = nsy.Unit()
        self.assertEqual(self.unit.__name__, nsy.configuration.undefined_unit_name)
        self.assertEqual(self.unit.__name_expression__, nsy.configuration.undefined_unit_name)
        self.assertEqual(self.unit.__symbol__, nsy.configuration.undefined_unit_symbol)
        self.assertEqual(self.unit.__symbolic_expression__, nsy.configuration.undefined_unit_symbolic_expression)

    def test_shortcut_initialization(self):
        self.unit_shortcut = nsy.Unit(na="unit", s="u")
        self.unit_long = nsy.Unit(name="unit", symbol="u")
        self.assertEqual(self.unit_shortcut.name, self.unit_long.name)
        self.assertEqual(self.unit_shortcut.na, self.unit_long.na)
        self.assertEqual(self.unit_shortcut.symbol, self.unit_long.symbol)
        self.assertEqual(self.unit_shortcut.s, self.unit_long.s)

    def test_multiplication(self):
        self.variable_shorthand_1 = nsy.V(s="\mu_{nb}", n=1)
        self.variable_shorthand_2 = nsy.V(s="\mu_{pe}", n=1)
        self.assertIsNotNone(self.variable_shorthand_1 * self.variable_shorthand_2)

    def test_value_initialization_integrated_units(self):
        self.compounded_constant_1 = nsy.C(s="k", na="Boltzmann constant", n=1.380649e-23, unit=nsy.U(s="J") / nsy.U(s="K"))
        self.compounded_variable_1 = nsy.V(s="T_a", na="Ambient temperature", n=np.linspace(0.1, 300), unit=nsy.U(s="K"))
        self.compounded_variable_2 = nsy.V(s="q", na="single electron charge", n=1.602176634e-19, unit=nsy.U(s="J"))
        self.assertIsNotNone(self.compounded_constant_1)
        self.assertIsNotNone(self.compounded_variable_1)
        self.assertIsNotNone(self.compounded_variable_2)

class TestFunctions(unittest.TestCase):
    def test_exp(self):
        self.assertTrue(nsy.exp(1))
        self.assertTrue(nsy.log(1))
        self.assertTrue(nsy.log10(1))

if __name__ == '__main__':
    unittest.main()
