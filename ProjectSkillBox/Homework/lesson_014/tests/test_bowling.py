import unittest
from bowling import BowlingScoreEngine

class BowlingScoreEngineTest(unittest.TestCase):


    def test_bowling(self):
        self.assertEqual(BowlingScoreEngine('XXXXXXXXXX').score, 200)
        self.assertEqual(BowlingScoreEngine('9-9-9-9-9-').score, 45)
        self.assertEqual(BowlingScoreEngine('5/5/5/5/5/').score, 75)
        self.assertEqual(BowlingScoreEngine('Х4/34').score, 42)
        self.assertEqual(BowlingScoreEngine('X7/9-X-88/').score, 88)
    def test_bowling_error(self):
        self.assertRaises(ValueError, BowlingScoreEngine, 'XXXXXXXXXXX')
        self.assertRaises(ValueError, BowlingScoreEngine, 'x')
        self.assertRaises(ValueError, BowlingScoreEngine, '!')
        self.assertRaises(ValueError, BowlingScoreEngine, '0')
        self.assertRaises(ValueError, BowlingScoreEngine, 'Х4|34')
        self.assertRaises(ValueError, BowlingScoreEngine, "'")
        self.assertRaises(ValueError, BowlingScoreEngine, '"')
        self.assertRaises(TypeError, BowlingScoreEngine, None)
        self.assertRaises(ValueError, BowlingScoreEngine, '')
        self.assertRaises(ValueError, BowlingScoreEngine, ' ')



if __name__ == '__main__':
    unittest.main()
