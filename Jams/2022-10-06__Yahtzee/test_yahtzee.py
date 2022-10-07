import yahtzee
import unittest


class TestYahtzee(unittest.TestCase):
    def test__score_for_chance__is_sum_of_all_dice(self):
        test_arguments = [
            ((1, 1, 3, 3, 6), 14),
            ((4, 5, 5, 6, 1), 21),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_chance(*input_dice)
            self.assertEqual(actual_score, expected_score)

    def test__score_for_yahtzee__is_50__if_all_dice_are_the_same__is_0__otherwise(self):
        test_arguments = [
            ((1, 1, 1, 1, 1), 50),
            ((4, 4, 4, 4, 4), 50),
            ((1, 1, 1, 2, 1), 0),
            ((4, 4, 4, 4, 5), 0),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_yahtzee(*input_dice)
            self.assertEqual(actual_score, expected_score)

    def test__score_for_n__is_sum_of_all_occurences_of_n(self):
        test_arguments = [
            ((1, 1, 2, 4, 4), 4, 8),
            ((2, 3, 2, 5, 1), 2, 4),
            ((3, 3, 3, 4, 5), 1, 0),
        ]

        for input_dice, number_to_score, expected_score in test_arguments:
            actual_score = yahtzee.score_for_given_number(
                *input_dice,
                number_to_score=number_to_score
            )
            self.assertEqual(actual_score, expected_score)

    def test__score_for_pair__is_sum_of_the_highest_dice__where_its_number_has_exactly_two_occurences(self):
        test_arguments = [
            ((3, 3, 3, 4, 4), 8),
            ((1, 1, 6, 2, 6), 12),
            ((3, 3, 3, 4, 1), 0),
            ((3, 3, 3, 3, 1), 0),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_pair(*input_dice)
            self.assertEqual(actual_score, expected_score)

    def test__score_for_two_pair__is_sum_of_all_dice__where_its_number_has_exactly_two_occurences(self):
        test_arguments = [
            ((1, 1, 2, 3, 3), 8),
            ((1, 1, 2, 3, 4), 0),
            ((1, 1, 2, 2, 2), 0),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_two_pair(*input_dice)
            self.assertEqual(actual_score, expected_score)


if __name__ == '__main__':
    unittest.main()
