def lahko_sledi(prej,potem):
    return (prej != potem and prej[-1] == potem[0])


def ni_ponavljanj(besede):
    return len(besede) == len(set(besede))


def preveri_zaporedje(besede):
    return ni_ponavljanj(besede) and all(lahko_sledi(prej, potem) for prej, potem in zip(besede, besede[1:]))


def mozne_naslednje(beseda, slovar):
    return [potem for potem in slovar if lahko_sledi(beseda,potem)]


def kvaliteta_besede(beseda):
    return (-len(beseda), beseda)


import unittest
import ast


class TestBase(unittest.TestCase):
    functions = {elm.name: elm
                 for elm in ast.parse(open(__file__).read()).body
                 if isinstance(elm, ast.FunctionDef)}

    def assert_is_one_line(self, func):
        func
        body = self.functions[func.__code__.co_name].body
        self.assertEqual(len(body), 1, "\nFunkcija ni dolga le eno vrstico")
        self.assertIsInstance(body[0], ast.Return, "\nFunkcija naj bi vsebovala le return")

    def test_nedovoljene_funkcije(self):
        dovoljene_funkcije = {
            "lahko_sledi", "ni_ponavljanj", "preveri_zaporedje",
            "mozne_naslednje",
            "kvaliteta_besede", "izberi_besedo", "pogostosti_zacetnic"}
        for func in self.functions:
            self.assertIn(func, dovoljene_funkcije, f"\nFunkcija {func} ni dovoljena.")

class Obvezna(TestBase):
    def test_lahko_sledi(self):
        self.assert_is_one_line(lahko_sledi)
        self.assertTrue(lahko_sledi("OMARA", "ASPARAGUS"))
        self.assertTrue(lahko_sledi("PETER", "REBEKA"))
        self.assertFalse(lahko_sledi("PETER", "ASPARAGUS"))
        self.assertFalse(lahko_sledi("PRETEP", "PRETEP"))

    def test_ni_ponavljanj(self):
        self.assert_is_one_line(ni_ponavljanj)
        self.assertTrue(ni_ponavljanj(["PETER", "ŽOGA", "METLA", "JOŽE"]))
        self.assertTrue(ni_ponavljanj(["PETER"]))
        self.assertTrue(ni_ponavljanj([]))

        self.assertFalse(ni_ponavljanj(["PETER", "PETER"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "JOŽE"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "ŽOGA"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "PETER"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "PETER", "JOŽE"]))

    def test_preveri_zaporedje(self):
        self.assert_is_one_line(preveri_zaporedje)
        self.assertTrue(preveri_zaporedje(
            ["PETER", "RAZBOJNIK", "KLEMEN", "NEPRIDIPRAV", "VINKO",
             "OROŽNIK"]))
        self.assertTrue(preveri_zaporedje(["PETER", "RAZBOJNIK"]))
        self.assertTrue(preveri_zaporedje(["VINKO"]))

        self.assertFalse(
            preveri_zaporedje(["PETER", "ZABOJNIK", "KLEMEN", "NEPRIDIPRAV"]))
        self.assertFalse(
            preveri_zaporedje(["PETER", "RAZBOJNIK", "ALEŠ", "NEPRIDIPRAV"]))
        self.assertFalse(
            preveri_zaporedje(["PETER", "RAZBOJNIK", "KLEMEN", "TAT"]))
        self.assertFalse(
            preveri_zaporedje(["PETER", "RAZBOJNIK", "KLEP", "PETER", "RIBA"]))

    def test_mozne_naslednje(self):
        self.assert_is_one_line(mozne_naslednje)
        mali_slovar = ["ABRAHAM", "ANGLIJA", "BOTER", "ČEŠNJA"]
        self.assertEqual(["ABRAHAM", "ANGLIJA"],
                         mozne_naslednje("ROŽA", mali_slovar))
        self.assertEqual(["BOTER"], mozne_naslednje("ROB", mali_slovar))
        self.assertEqual([], mozne_naslednje("ROBNIK", mali_slovar))






if __name__ == "__main__":
    unittest.main()

