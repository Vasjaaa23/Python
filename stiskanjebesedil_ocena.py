def slovar_besed(besedilo):
    b = besedilo.split()
    slovar = dict.fromkeys(b)
    for i,j in enumerate(slovar):
        slovar[j] = i
    return slovar


def stisni_besedilo(besedilo,slovar):
    seznam = []
    b = besedilo.split()
    for i in b:
        seznam.append(slovar[i])
    return seznam


def obrni_slovar(slovar):
    seznam = []
    besede = sorted(slovar, key=slovar.get)
    for i,j in enumerate(besede):
        seznam.append(j)
    return seznam


def raztegni_besedilo(besedilo,slovar):
    seznam = []
    for i in besedilo:
        for j in slovar:
            if i == slovar[j]:
                seznam.append(j)
    return " " .join(seznam)






"""

#Enumerate se sprehod po celotni dolžini dane tabele, slovarja ipd., sam se ustav

"""







import unittest

class Test06(unittest.TestCase):
    def test_slovar_besed(self):
        self.assertEqual(
            {"stavek": 0, "ki": 1, "to": 2, "ni": 3, "ker": 4, "kar": 5},
            slovar_besed("stavek ki to ni ker stavek ni kar to ni")
        )
        self.assertEqual({"bla": 0}, slovar_besed("bla bla bla"))

    def test_stisni_besedilo(self):
        self.assertEqual(
            [0, 1, 2, 3, 4, 0, 3, 5, 2, 3],
            stisni_besedilo("stavek ki to ni ker stavek ni kar to ni",
                            {"ni": 3, "ker": 4, "kar": 5, "stavek": 0, "ki": 1, "to": 2})
        )
        self.assertEqual(
            [6, 1, 2, 3, 4, 6, 3, 5, 2, 3],
            stisni_besedilo("stavek ki to ni ker stavek ni kar to ni",
                            {"beseda": 0, "ki": 1, "to": 2, "ni": 3, "ker": 4, "kar": 5, "stavek": 6})
        )


class Test07(unittest.TestCase):
    def test_obrni_slovar(self):
        self.assertEqual(
            ["stavek", "ki", "to", "ni", "ker", "kar"],
            obrni_slovar({"ni": 3, "ker": 4, "kar": 5, "stavek": 0, "ki": 1, "to": 2})
        )
        self.assertEqual(["bla"], obrni_slovar({"bla": 0}))
        self.assertEqual(["ena", "dva", "tri"],
                         obrni_slovar({"dva": 1, "ena": 0, "tri": 2}))

    def test_raztegni_besedilo(self):
        self.assertEqual(
            "stavek ki to ni ker stavek ni kar to ni",
            raztegni_besedilo([0, 1, 2, 3, 4, 0, 3, 5, 2, 3],
                            {"ni": 3, "ker": 4, "kar": 5, "stavek": 0, "ki": 1, "to": 2})
        )
        self.assertEqual(
            "stavek ki to ni ker stavek ni kar to ni",
            raztegni_besedilo([6, 1, 2, 3, 4, 6, 3, 5, 2, 3],
                            {"beseda": 0, "ki": 1, "to": 2, "ni": 3, "ker": 4, "kar": 5, "stavek": 6})
        )



if __name__ == "__main__":
    unittest.main()

