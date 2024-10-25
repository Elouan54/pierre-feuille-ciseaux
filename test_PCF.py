from PFC import play
import unittest

class test(unittest.TestCase):
    def test_play(self):
        self.assertEqual(play('pierre', 'ciseaux'), 'player 1 win')
        self.assertEqual(play('feuille', 'pierre'), 'player 1 win')
        self.assertEqual(play('ciseaux', 'feuille'), 'player 1 win')
        self.assertEqual(play('pierre', 'pierre'), 'draw')
        self.assertEqual(play('feuille', 'feuille'), 'draw')
        self.assertEqual(play('ciseaux', 'ciseaux'), 'draw')
        self.assertEqual(play('feuille', 'ciseaux'), 'player 2 win')
        self.assertEqual(play('ciseaux', 'pierre'), 'player 2 win')
        self.assertEqual(play('pierre', 'feuille'), 'player 2 win')

if __name__ == "__main__":
    unittest.main()