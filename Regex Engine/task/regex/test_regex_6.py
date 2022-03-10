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
        self.assertTrue(regex.compare('apple', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('.pple', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('appl.', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('.....', 'apple', 0, 0, True))
        self.assertFalse(regex.compare('peach', 'apple', 0, 0, True))

    def test_level_2(self):
        # tests for the strings of the same length
        self.assertTrue(regex.compare('apple', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('.pple', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('appl.', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('.....', 'apple', 0, 0, True))
        self.assertFalse(regex.compare('peach', 'apple', 0, 0, True))

    def test_level_3(self):
        # tests for the strings of the different length without special cases
        self.assertTrue(regex.compare('apple', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('ap', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('le', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('a', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('.', 'apple', 0, 0, True))
        self.assertFalse(regex.compare('apwle', 'apple', 0, 0, True))
        self.assertFalse(regex.compare('peach', 'apple', 0, 0, True))

    def test_level_4(self):
        # tests for the strings of the different length with special cases
        self.assertTrue(regex.compare('^app', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('le$', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('^a', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('.$', 'apple', 0, 0, True))
        self.assertTrue(regex.compare('apple$', 'tasty apple', 0, 0, True))
        self.assertTrue(regex.compare('^apple', 'apple pie', 0, 0, True))
        self.assertTrue(regex.compare('^apple$', 'apple', 0, 0, True))
        self.assertFalse(regex.compare('^apple$', 'tasty apple', 0, 0, True))
        self.assertFalse(regex.compare('^apple$', 'apple pie', 0, 0, True))
        self.assertFalse(regex.compare('app$', 'apple', 0, 0, True))
        self.assertFalse(regex.compare('^le', 'apple', 0, 0, True))

    def test_level_5(self):
        # tests for the strings of the different length with special cases
        self.assertTrue(regex.compare('colou?r', 'color', 0, 0, True))
        self.assertTrue(regex.compare('colou?r', 'colour', 0, 0, True))
        self.assertFalse(regex.compare('colou?r', 'colouur', 0, 0, True))
        self.assertTrue(regex.compare('colou*r', 'color', 0, 0, True))
        self.assertTrue(regex.compare('colou*r', 'colour', 0, 0, True))
        self.assertTrue(regex.compare('colou*r', 'colouur', 0, 0, True))
        self.assertTrue(regex.compare('col.*r', 'color', 0, 0, True))
        self.assertTrue(regex.compare('col.*r', 'colour', 0, 0, True))
        self.assertTrue(regex.compare('col.*r', 'colr', 0, 0, True))
        self.assertTrue(regex.compare('col.*r', 'collar', 0, 0, True))
        self.assertFalse(regex.compare('col.*r$', 'colors', 0, 0, True))


if __name__ == '__main__':
    unittest.main()
