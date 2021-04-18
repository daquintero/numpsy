import unittest
import numpsy as nsy

class TestHelpers(unittest.TestCase):

    def test_select_available_property_(self):
        self.assertEqual(nsy.helpers.__select_available_property__("first", "default", "default"), "first")
        self.assertEqual(nsy.helpers.__select_available_property__("default", "second", "default"), "second")
        self.assertEqual(nsy.helpers.__select_available_property__("default", "default", "default", "optional"), "optional")
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
        self.assertEqual(self.unit.__symbolic_expression__, nsy.configuration.undefined_unit_symbol)

    def test_shortcut_initialization(self):
        self.unit_shortcut = nsy.Unit(n="unit", s="u")
        self.unit_long = nsy.Unit(name="unit", symbol="u")
        self.assertEqual(self.unit_shortcut.name, self.unit_long.name)
        self.assertEqual(self.unit_shortcut.na, self.unit_long.na)
        self.assertEqual(self.unit_shortcut.symbol, self.unit_long.symbol)
        self.assertEqual(self.unit_shortcut.s, self.unit_long.s)


if __name__ == '__main__':
    unittest.main()
