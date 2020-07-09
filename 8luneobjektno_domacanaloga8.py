class Luna:
    def __init__(self):
        self.lunice = []

    def pripni(self,ime):
        self.lunice.append(ime)

    def lune(self):
        return set(self.lunice)

    def ima_luno(self,ime):
        if ime in self.lunice:
            return True
        else:
            return False

    def stevilo_lun(self):
        return len(self.lunice)


class EkskluzivnaLuna(Luna):
    def pripni(self, ime):
        if len(self.lunice) >= 3:
            self.lunice.pop(0)
        super().pripni(ime)


import unittest
from unittest.mock import patch
import random


class Test01Obvezna(unittest.TestCase):
    def test01_luna(self):
        a = Luna()
        self.assertIsNone(a.pripni("b"), "Metoda `pripni` ne sme vračati ničesar")
        a.pripni("c")
        a.pripni("d")

        b = Luna()
        b.pripni("xyz")

        c = Luna()

        self.assertEqual({"b", "c", "d"}, a.lune())
        self.assertEqual({"xyz"}, b.lune())
        self.assertEqual(set(), c.lune())

        self.assertTrue(a.ima_luno("b"))
        self.assertFalse(a.ima_luno("xyz"))

        self.assertFalse(b.ima_luno("b"))
        self.assertTrue(b.ima_luno("xyz"))

        self.assertFalse(c.ima_luno("b"))
        self.assertFalse(c.ima_luno("xyz"))

        self.assertEqual(3, a.stevilo_lun())
        self.assertEqual(1, b.stevilo_lun())
        self.assertEqual(0, c.stevilo_lun())

    def test02_ekskluzivna_luna_pripni(self):
        imena = ["asd", "asdf", "aoij", "ivuiv", "asdjnf", "oija"]
        for _ in range(10):
            random.shuffle(imena)
            a = EkskluzivnaLuna()
            a.pripni(imena[0])
            self.assertEqual(1, a.stevilo_lun())
            a.pripni(imena[1])
            self.assertEqual(2, a.stevilo_lun())
            for i in range(2, len(imena)):
                a.pripni(imena[i])
                self.assertEqual(3, a.stevilo_lun())
                self.assertEqual(a.lune(), set(imena[i - 2:i + 1]),
                                 f"ko dodajam v tem vrstnem redu: {imena},\n"
                                 f"pride do napake, ko dodam {imena[i]}")

    def test02_ekskluzivna_luna_struktura(self):
        self.assertEqual((Luna,), EkskluzivnaLuna.__bases__,
                         "Razred EkskluzivnaLuna mora biti izpeljan iz razreda Luna")
        self.assertEqual(["pripni"],
                         [name for name in EkskluzivnaLuna.__dict__ if name[:2] != "__"],
                         "Razred EkskluzivnaLuna naj doda/spremeni samo metodo `pripni`")
        with patch.object(Luna, "pripni") as mock_pripni:
            a = EkskluzivnaLuna()
            a.pripni("b")
            self.assertTrue(mock_pripni.called, "Metoda pripni mora klicati podedovano metodo")





if __name__ == "__main__":
    unittest.main()
