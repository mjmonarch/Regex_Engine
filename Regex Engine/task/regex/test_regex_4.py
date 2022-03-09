import unittest
import regex


class Test(unittest.TestCase):

    def test_level_1(self):
        # tests for the match of 1 symbol
        self.assertTrue(regex.match('a', 'a'))
        self.assertTrue(regex.match('.', 'a'))
        self.assertTrue(regex.match(' ', ' '))
        self.assertFalse(regex.match('A', 'a'))
        self.assertFalse(regex.match('-', '_'))

    def test_level_2(self):
        # tests for the match of 1 symbol
        self.assertTrue(regex.compare_same_length('apple', 'apple'))
        self.assertTrue(regex.compare_same_length('.pple', 'apple'))
        self.assertTrue(regex.compare_same_length('appl.', 'apple'))
        self.assertTrue(regex.compare_same_length('.....', 'apple'))
        self.assertFalse(regex.compare_same_length('peach', 'apple'))

    def test_level_2(self):
        # tests for the strings of the same length
        self.assertTrue(regex.compare_same_length('apple', 'apple'))
        self.assertTrue(regex.compare_same_length('.pple', 'apple'))
        self.assertTrue(regex.compare_same_length('appl.', 'apple'))
        self.assertTrue(regex.compare_same_length('.....', 'apple'))
        self.assertFalse(regex.compare_same_length('peach', 'apple'))

    def test_level_3(self):
        # tests for the strings of the different length without special cases
        self.assertTrue(regex.compare_simple('apple', 'apple'))
        self.assertTrue(regex.compare_simple('ap', 'apple'))
        self.assertTrue(regex.compare_simple('le', 'apple'))
        self.assertTrue(regex.compare_simple('a', 'apple'))
        self.assertTrue(regex.compare_simple('.', 'apple'))
        self.assertFalse(regex.compare_simple('apwle', 'apple'))
        self.assertFalse(regex.compare_simple('peach', 'apple'))

    def test_level_4(self):
        # tests for the strings of the different length with special cases
        self.assertTrue(regex.compare_complex('^app', 'apple'))
        self.assertTrue(regex.compare_complex('le$', 'apple'))
        self.assertTrue(regex.compare_complex('^a', 'apple'))
        self.assertTrue(regex.compare_complex('.$', 'apple'))
        self.assertTrue(regex.compare_complex('apple$', 'tasty apple'))
        self.assertTrue(regex.compare_complex('^apple', 'apple pie'))
        self.assertTrue(regex.compare_complex('^apple$', 'apple'))
        self.assertFalse(regex.compare_complex('^apple$', 'tasty apple'))
        self.assertFalse(regex.compare_complex('^apple$', 'apple pie'))
        self.assertFalse(regex.compare_complex('app$', 'apple'))
        self.assertFalse(regex.compare_complex('^le', 'apple'))


if __name__ == '__main__':
    unittest.main()
