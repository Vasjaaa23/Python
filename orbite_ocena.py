def preberi_orbite(ime_datoteke):
    datoteka = open(ime_datoteke)
    slovar = dict()
    for vrstica in datoteka:
        kljuc = vrstica.split(")")[1]
        vrednost = vrstica.split(")")[0]
        slovar.update({kljuc.replace("\n",""):vrednost})
    return slovar


def lune(orbite):
    slovar = {}
    for luna, planet in orbite.items():
        if planet in slovar:
            slovar[planet].add(luna)
        else:
            slovar[planet] = {luna}
    return slovar


def prestej_korake(odkod, kam, orbite):
    trenutni = odkod
    koraki = 0
    while trenutni != kam:
        trenutni = orbite[trenutni]
        koraki += 1
    return koraki


def prestej_korake_r(odkod, kam, orbite):
    if odkod == kam:
        return 0
    return 1 + prestej_korake_r(orbite[odkod], kam, orbite)


def n_odvisnikov(planet, orbite):
    stevec = 0
    for luna in orbite:
        if planet == orbite[luna]:
            stevec += 1 + n_odvisnikov(luna,orbite)
    return stevec


def pot_do(odkod, kam, orbite):
    trenutni = odkod
    koraki = [trenutni]
    while trenutni != kam:
        trenutni = orbite[trenutni]
        koraki.append(trenutni)
    return koraki




import unittest
import warnings
import random
import os
import sys


class Test(unittest.TestCase):
    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", ResourceWarning)

        self.orbite = {'B': 'COM',
                  'C': 'B',
                  'D': 'C',
                  'E': 'D',
                  'F': 'E',
                  'G': 'B',
                  'H': 'G',
                  'I': 'D',
                  'J': 'E',
                  'K': 'J',
                  'L': 'K',
                  'SAN': 'I',
                  'YOU': 'K'}

    dolga_pot = [
        'SAN', 'H64', 'DLX', 'JLC', 'BTD', 'SN6', '1PW', 'PTF', 'ZXK',
        'QXH', 'W63', 'DCW', 'NFB', 'CZC', 'P38', 'NRN', '28S', '8NT',
        'CMV', 'ZKH', 'MPV', '5W2', 'KXK', '6CQ', 'S4D', 'Z7S', 'YS5',
        '51S', '7KN', '61Z', 'JW6', 'BDM', 'JDY', 'NYN', 'CM7', '6FD',
        'BP2', '69K', 'RV3', 'PHH', '35T', 'DBL', 'VGY', '4X9', 'MFL',
        '6SQ', '1GY', '7WH', '14P', '9BR', 'QSN', 'NDH', 'RFM', 'JRF',
        'NGS', 'XYQ', '77T', '2TK', '6V6', 'C3Q', 'P99', '71R', '2XW',
        'BGB', 'J24', 'DT2', 'Y9Z', '5FS', 'G7L', 'Y8N', 'X24', 'BPJ',
        'P8Q', 'XJQ', '98B', 'JB4', 'HK9', 'NN3', 'VPC', 'QSX', '9TL',
        'X25', 'X8Q', 'HY5', 'X6R', 'P3R', 'MKY', 'FLS', 'KQT', '5WX',
        '3R1', 'W35', '2VY', '2DM', 'MXS', '7FB', 'TXD', 'C32', 'J45',
        'QBV', 'DG7', '2RS', 'GB3', 'WZ6', 'W7R', 'R4Y', 'F4W', '2V8',
        '19D', 'GZC', '3VP', 'KNV', 'MKF', '4JW', 'FT8', 'V3N', 'RN1',
        'ZM3', 'G9T', '2JF', 'P67', '9TG', '3NV', 'XCZ', 'VGH', 'WL1',
        '1HN', 'YZC', 'HDY', 'LZ3', 'Q7N', 'Z9G', 'JWW', '5QH', '33Q',
        '95Q', 'Q8Q', 'WW7', '3P8', 'MZ7', 'NJY', '7QF', 'K3N', '8KZ',
        'BDH', 'HNN', 'LHB', '73P', '7ZB', 'YDG', 'K3T', 'G8K', 'DDZ',
        '3W9', 'M87', '1T9', 'BHB', 'CKH', 'NC9', 'JN8', '19X', 'V1D',
        'CK5', '1Z9', '4YN', 'VT4', 'JY4', 'HMM', 'SKW', 'GY3', '9Z4',
        'NBL', '3SC', 'QS2', '385', 'GMS', '79F', 'NJ1', 'HMS', 'C9W',
        '2FV', 'P7S', '36D', '5BF', 'X8T', 'YWT', '842', '8N9', '238',
        'RCT', 'KW2', 'HKJ', '43B', 'V7K', 'CG2', 'XXP', 'MK9', 'YQP',
        '697', '2JH', '6H1', 'NX2', '7MR', 'HGG', 'ZWL', 'N7G', 'V9Q',
        '7XM', 'DSX', 'HF1', 'H2K', 'BWG', 'Z9W', 'N1R', '34F', '75P',
        'TRM', '211', '2VD', '49K', 'SXT', 'JTY', 'DL8', '9SN', 'C93',
        'T6Z', 'JHK', 'F6Y', 'PWP', '66Z', 'MWF', 'HXD', 'COM']

    try:
        vorbite = preberi_orbite("input.txt")
    except:
        vorbite = None


class Test06(Test):
    def test_01_preberi_orbite(self):
        self.assertEqual(self.orbite, preberi_orbite("example.txt"))
        try:
            ime = str(random.randint(1000000, 9999999))
            os.rename("example.txt", ime)
            self.assertEqual(self.orbite, preberi_orbite(ime),
                             "Funkcija prejme ime datoteke kot argument!")
        except:
            raise
        finally:
            os.rename(ime, "example.txt")

    def test_02_lune(self):
        self.assertEqual(
            {'B': {'C', 'G'},
             'C': {'D'},
             'COM': {'B'},
             'D': {'E', 'I'},
             'E': {'F', 'J'},
             'G': {'H'},
             'I': {'SAN'},
             'J': {'K'},
             'K': {'L', 'YOU'}}, lune(self.orbite))

    def test_03_prestej_skoke(self):
        self.assertEqual(4, prestej_korake("K", "C", self.orbite))
        self.assertEqual(1, prestej_korake("K", "J", self.orbite))
        self.assertEqual(0, prestej_korake("K", "K", self.orbite))
        self.assertEqual(3, prestej_korake("F", "C", self.orbite))
        self.assertEqual(7, prestej_korake("L", "COM", self.orbite))

        orbite = preberi_orbite("input.txt")
        self.assertEqual(101, prestej_korake("D1W", "COM", orbite))

        orbite = {str(i + 1): str(i) for i in range(100000)}
        self.assertEqual(100000, prestej_korake("100000", "0", orbite))

    def test_04_prestej_skoke_r(self):
        self.assertEqual(4, prestej_korake_r("K", "C", self.orbite))
        self.assertEqual(1, prestej_korake_r("K", "J", self.orbite))
        self.assertEqual(0, prestej_korake_r("K", "K", self.orbite))
        self.assertEqual(3, prestej_korake_r("F", "C", self.orbite))
        self.assertEqual(7, prestej_korake_r("L", "COM", self.orbite))

        orbite = preberi_orbite("input.txt")
        self.assertEqual(101, prestej_korake_r("D1W", "COM", orbite))

        orbite = {str(i + 1): str(i) for i in range(2000)}
        self.assertEqual(100, prestej_korake_r("100", "0", orbite))
        self.assertEqual(500, prestej_korake_r("2000", "1500", orbite))

        try:
            sys.setrecursionlimit(1000)
            with self.assertRaises(RecursionError,
                                   msg="Funkcija mora biti rekurzivna"):
                prestej_korake_r("2000", "0", orbite)

            sys.setrecursionlimit(2500)
            self.assertEqual(2000, prestej_korake_r("2000", "0", orbite))
        except:
            raise
        finally:
            sys.setrecursionlimit(1000)

    def test_05_n_odvisnikov(self):
        self.assertEqual(8, n_odvisnikov("D", self.orbite))
        self.assertEqual(0, n_odvisnikov("F", self.orbite))
        self.assertEqual(13, n_odvisnikov("COM", self.orbite))

        orbite = preberi_orbite("input.txt")
        self.assertEqual(len(orbite), n_odvisnikov("COM", orbite))
        self.assertEqual(806, n_odvisnikov("ZWL", orbite))


class Test07(Test):
    def test_01_pot_do(self):
        self.assertEqual(["SAN", "I", "D", "C"],
                         pot_do("SAN", "C", self.orbite))
        self.assertEqual(["K", "J", "E"],
                         pot_do("K", "E", self.orbite))
        self.assertEqual(["F", "E"],
                         pot_do("F", "E", self.orbite))
        self.assertEqual(["F"],
                         pot_do("F", "F", self.orbite))

        self.assertEqual(self.dolga_pot,
                         pot_do("SAN", "COM", self.vorbite))

        orbite = {str(i + 1): str(i) for i in range(100000)}
        self.assertEqual([str(i) for i in range(100000, -1, -1)],
                         pot_do("100000", "0", orbite))

    def test_02_pot_v_niz(self):
        self.assertEqual("F -> E -> D -> C",
                         pot_v_niz(["F", "E", "D", "C"]))
        self.assertEqual("F -> E",
                         pot_v_niz(["F", "E"]))
        self.assertEqual("F",
                         pot_v_niz(["F"]))

    def test_03_navodila(self):
        try:
            ime_dat = f"{random.randint(10000, 99999)}.txt"
            navodila("F -> E -> D -> C -> B", ime_dat)
            self.assertEqual("Iz F pojdite na E.\n"
                             "Potem zavijte na D.\n"
                             "Potem zavijte na C.\n"
                             "Potem zavijte na B.\n"
                             "Vaš cilj, B, bo pod vami.",
                             open(ime_dat).read().strip("\n"))
            navodila("F -> E", ime_dat)
            self.assertEqual("Iz F pojdite na E.\n"
                             "Vaš cilj, E, bo pod vami.",
                             open(ime_dat).read().strip("\n"))
            navodila("F", ime_dat)
            self.assertEqual("Vaš cilj, F, bo pod vami.",
                             open(ime_dat).read().strip("\n"))
        except:
            raise
        finally:
            os.remove(ime_dat)





if __name__ == "__main__":
    unittest.main()
