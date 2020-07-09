def samoopisno(n):
    m = str(n)
    for i, j in enumerate(m):
        if m.count(str(i)) != int(j):
            return False
    return True




def vsa_samoopisna(d):
    seznam = []
    for i in range(10**(d-1), 10**d - 1):
        a = samoopisno(i)
        if a == True:
            seznam.append(i)
    return seznam






#print(vsa_samoopisna(4))                # printa vsa 4-mestna samoopisna števila

import unittest

class TestObvezna(unittest.TestCase):
    def test_samoopisno(self):
        self.assertTrue(samoopisno(1210))
        self.assertTrue(samoopisno(2020))
        self.assertTrue(samoopisno(3211000))
        self.assertTrue(samoopisno(6210001000))

        self.assertFalse(samoopisno(121))
        self.assertFalse(samoopisno(1211))
        self.assertFalse(samoopisno(202))
        self.assertFalse(samoopisno(20))
        self.assertFalse(samoopisno(123))
        self.assertFalse(samoopisno(1234))
        self.assertFalse(samoopisno(100))
        self.assertFalse(samoopisno(136))

    def test_vsa_samoopisna(self):
        self.assertEqual(vsa_samoopisna(4), [1210, 2020])
        self.assertEqual(vsa_samoopisna(5), [21200])





if __name__ == "__main__":
    unittest.main()

