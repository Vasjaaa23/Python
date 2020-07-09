# Tu napiši svoje funkcije

def lahko_sledi(prej,potem):
    if prej != potem and prej[-1] == potem[0]:
        return True


def izberi_besedo(beseda,slovar):
    najdaljsa_beseda = ""

    for element in slovar:
        if beseda[-1] == element[0] and beseda != element:
            if len(element) > len(najdaljsa_beseda):
                najdaljsa_beseda = element
            elif len(element) == len(najdaljsa_beseda):
                besede = []
                besede.append(element)
                besede.append(najdaljsa_beseda)
                besede.sort()
                najdaljsa_beseda = besede[0]
    return najdaljsa_beseda



def ni_ponavljanj(besede):
    if len(besede) == len(set(besede)):
        return True




def preveri_zaporedje(besede):
    if not ni_ponavljanj(besede):
        return False
    for i in range(len(besede) - 1):
        if not lahko_sledi(besede[i], besede[i+1]):
            return False
    return True




import unittest


class Obvezna(unittest.TestCase):
    def test_lahko_sledi(self):
        self.assertTrue(lahko_sledi("OMARA", "ASPARAGUS"))
        self.assertTrue(lahko_sledi("PETER", "REBEKA"))
        self.assertFalse(lahko_sledi("PETER", "ASPARAGUS"))
        self.assertFalse(lahko_sledi("PRETEP", "PRETEP"))

    def test_izberi_besedo(self):
        self.assertEqual(
            "RAZBOJNIK", izberi_besedo("PETER",
                                       ["RAZBOJNIK", "ROPAR", "RAVBAR", "TAT",
                                        "ŽEPAR", "OTORINOLARINGOLOGIJA"]))
        self.assertEqual(
            "RAZBOJNIK", izberi_besedo("PETER",
                                       ["ROPAR", "RAVBAR", "RAZBOJNIK", "TAT",
                                        "ŽEPAR", "OTORINOLARINGOLOGIJA"]))
        self.assertEqual(
            "RAVBAR", izberi_besedo("PETER",
                                    ["ROPAR", "RAVBAR", "TAT", "ROLAND",
                                     "ŽEPAR", "OTORINOLARINGOLOGIJA"]))
        self.assertEqual(
            "RAVBAR", izberi_besedo("PETER", ["ROPAR", "ROLAND", "TAT",
                                              "OTORINOLARINGOLOGIJA", "RAVBAR",
                                              "ŽEPAR"]))
        self.assertEqual(
            "PETER", izberi_besedo("PRETEP",
                                   ["PETER", "OTORINOLARINGOLOGIJA", "PRETEP",
                                    "PERO", "MAFIJA"]))

    def test_ni_ponavljanj(self):
        self.assertTrue(ni_ponavljanj(["PETER", "ŽOGA", "METLA", "JOŽE"]))
        self.assertTrue(ni_ponavljanj(["PETER"]))
        self.assertTrue(ni_ponavljanj([]))

        self.assertFalse(ni_ponavljanj(["PETER", "PETER"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "JOŽE"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "ŽOGA"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "PETER"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "PETER", "JOŽE"]))

    def test_preveri_zaporedje(self):
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



if __name__ == "__main__":
    unittest.main()
