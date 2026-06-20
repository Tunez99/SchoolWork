#!/usr/bin/env python3

import unittest

import genealogy
from genealogy import *

import inspect
import warnings


class TestGenealogy(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(genealogy)
        redflags = [
            ('import', 'It looks like you are using imports, which is not allowed!'),
        ]
        for redflag, warning in redflags:
            if redflag in source:
                warnings.warn(warning)

    @staticmethod
    def __construct_example():
        genealogy = Genealogy('A')
        genealogy.add_child('A', 'B')
        genealogy.add_child('A', 'C')
        genealogy.add_child('B', 'D')
        genealogy.add_child('B', 'E')
        genealogy.add_child('C', 'F')
        genealogy.add_child('C', 'G')
        genealogy.add_child('D', 'H')
        genealogy.add_child('D', 'I')
        genealogy.add_child('D', 'J')
        genealogy.add_child('F', 'K')
        return genealogy

    def test_get_primogeniture_order_example(self):
        genealogy = self.__construct_example()
        expected = [c for c in 'ABDHIJECFKG']
        result = genealogy.get_primogeniture_order()
        print("\nPrimogeniture order:", result)
        self.assertEqual(result, expected)

    def test_get_seniority_order_example(self):
        genealogy = self.__construct_example()
        expected = [c for c in 'ABCDEFGHIJK']
        result = genealogy.get_seniority_order()
        print("\nSeniority order:", result)
        self.assertEqual(result, expected)

    def test_get_cousin_dist_example(self):
        genealogy = self.__construct_example()
        print("\nCousin distances:")
        print("B and C:", genealogy.get_cousin_dist('B', 'C'))
        print("D and E:", genealogy.get_cousin_dist('D', 'E'))
        print("B and F:", genealogy.get_cousin_dist('B', 'F'))
        print("D and F:", genealogy.get_cousin_dist('D', 'F'))
        print("B and D:", genealogy.get_cousin_dist('B', 'D'))
        print("B and J:", genealogy.get_cousin_dist('B', 'J'))
        print("J and K:", genealogy.get_cousin_dist('J', 'K'))
        print("J and F:", genealogy.get_cousin_dist('J', 'F'))
        print("D and K:", genealogy.get_cousin_dist('D', 'K'))
        print("B and K:", genealogy.get_cousin_dist('B', 'K'))

        self.assertEqual(genealogy.get_cousin_dist('B', 'C'), (0, 0))
        self.assertEqual(genealogy.get_cousin_dist('D', 'E'), (0, 0))
        self.assertEqual(genealogy.get_cousin_dist('B', 'F'), (0, 1))
        self.assertEqual(genealogy.get_cousin_dist('D', 'F'), (1, 0))
        self.assertEqual(genealogy.get_cousin_dist('B', 'D'), (-1, 1))
        self.assertEqual(genealogy.get_cousin_dist('B', 'J'), (-1, 2))
        self.assertEqual(genealogy.get_cousin_dist('J', 'K'), (2, 0))
        self.assertEqual(genealogy.get_cousin_dist('J', 'F'), (1, 1))
        self.assertEqual(genealogy.get_cousin_dist('D', 'K'), (1, 1))
        self.assertEqual(genealogy.get_cousin_dist('B', 'K'), (0, 2))

    def test_get_primogeniture_order_addition(self):
        genealogy = self.__construct_example()
        genealogy.add_child('I', 'X')
        result = genealogy.get_primogeniture_order()
        print("\nPrimogeniture after adding X:", result)
        self.assertEqual(result, [c for c in 'ABDHIXJECFKG'])

        genealogy.add_child('B', 'Y')
        result = genealogy.get_primogeniture_order()
        print("Primogeniture after adding Y:", result)
        self.assertEqual(result, [c for c in 'ABDHIXJEYCFKG'])

        genealogy.add_child('A', 'Z')
        result = genealogy.get_primogeniture_order()
        print("Primogeniture after adding Z:", result)
        self.assertEqual(result, [c for c in 'ABDHIXJEYCFKGZ'])

    def test_get_seniority_order_addition(self):
        genealogy = self.__construct_example()
        genealogy.add_child('I', 'X')
        result = genealogy.get_seniority_order()
        print("\nSeniority after adding X:", result)
        self.assertEqual(result, [c for c in 'ABCDEFGHIJKX'])

        genealogy.add_child('B', 'Y')
        result = genealogy.get_seniority_order()
        print("Seniority after adding Y:", result)
        self.assertEqual(result, [c for c in 'ABCDEYFGHIJKX'])

        genealogy.add_child('A', 'Z')
        result = genealogy.get_seniority_order()
        print("Seniority after adding Z:", result)
        self.assertEqual(result, [c for c in 'ABCZDEYFGHIJKX'])


if __name__ == '__main__':
    unittest.main(verbosity=2, buffer=False)
