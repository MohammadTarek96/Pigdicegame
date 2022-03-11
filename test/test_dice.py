import unittest
from pig.game import Dice


class TestDice(unittest.TestCase):
    def test_random_rolls(self):
        """
        Test that the dice does not produce results outside the range 1-6
        Might not work 100% of the time, due to randomness
        A more extensive test case might test the distribution of the numbers
        """
        dice = Dice()
        min_roll = None
        max_roll = None

        for i in range(1000):
            x = dice.roll()
            if min_roll is None:
                min_roll = x
                max_roll = x
            min_roll = min(x, min_roll)
            max_roll = max(x, max_roll)

        self.assertEqual(1, min_roll)
        self.assertEqual(6, max_roll)

    def test_configured_dice(self):
        test_configuration = [4, 5, 6, 2, 4, 1, 3, 3]

        dice = Dice(test_configuration)
        dice_rolls = []

        for i in range(2 * len(test_configuration)):
            dice_rolls.append(dice.roll())

        expected_list = []
        expected_list.extend(test_configuration)
        expected_list.extend(test_configuration)
        self.assertListEqual(expected_list, dice_rolls)
