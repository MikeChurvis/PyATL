import unittest

import yahtzee


class TestYahtzee(unittest.TestCase):
    def test__score_for_chance__is_sum_of_all_dice(self):
        test_arguments = [
            ((1, 1, 3, 3, 6), 14),
            ((4, 5, 5, 6, 1), 21),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_chance(*input_dice)
            self.assertEqual(actual_score, expected_score)

    def test__score_for_yahtzee__is_50__if_all_dice_are_the_same(self):
        test_arguments = [
            ((1, 1, 1, 1, 1), 50),
            ((4, 4, 4, 4, 4), 50),
            ((1, 1, 1, 2, 1), 0),
            ((4, 4, 4, 4, 5), 0),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_yahtzee(*input_dice)
            self.assertEqual(actual_score, expected_score)

    def test__score_for_number__is_the_sum_of_dice__with_the_given_number(self):
        test_arguments = [
            ((1, 1, 2, 4, 4), 4, 8),
            ((2, 3, 2, 5, 1), 2, 4),
            ((3, 3, 3, 4, 5), 1, 0),
        ]

        for input_dice, number_to_score, expected_score in test_arguments:
            actual_score = yahtzee.score_for_number(
                *input_dice,
                number_to_score=number_to_score
            )
            self.assertEqual(actual_score, expected_score)

    def test__score_for_pair__is_the_sum_of_dice__with_the_highest_number_that_has_exactly_two_occurences(self):
        test_arguments = [
            ((3, 3, 3, 4, 4), 8),
            ((1, 1, 6, 2, 6), 12),
            ((3, 3, 3, 4, 1), 0),
            ((3, 3, 3, 3, 1), 0),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_pair(*input_dice)
            self.assertEqual(actual_score, expected_score)

    def test__score_for_two_pair__is_the_sum_of_dice__with_numbers_that_have_exactly_two_occurences__if_exactly_two_such_numbers_exist(self):
        test_arguments = [
            ((1, 1, 2, 3, 3), 8),
            ((1, 1, 2, 3, 4), 0),
            ((1, 1, 2, 2, 2), 0),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_two_pair(*input_dice)
            self.assertEqual(actual_score, expected_score)

    def test__score_for_three_of_a_kind__is_sum_of_dice__with_a_number_that_has_exactly_three_occurences(self):
        test_arguments = [
            ((3, 3, 3, 4, 5), 9),
            ((3, 3, 4, 5, 6), 0),
            ((3, 3, 3, 3, 1), 0),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_three_of_a_kind(*input_dice)
            self.assertEqual(actual_score, expected_score)

    def test__score_for_four_of_a_kind__is_sum_of_dice__with_a_number_that_has_exactly_four_occurences(self):
        test_arguments = [
            ((2, 2, 2, 2, 5), 8),
            ((2, 2, 2, 5, 5), 0),
            ((2, 2, 2, 2, 2), 0),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_four_of_a_kind(*input_dice)
            self.assertEqual(actual_score, expected_score)

    def test__score_for_small_straight__is_15__if_all_numbers_1_through_5_occur(self):
        input_dice = 1, 2, 3, 4, 5
        expected_score = 15
        actual_score = yahtzee.score_for_small_straight(*input_dice)
        self.assertEqual(actual_score, expected_score)

    def test__score_for_large_straight__is_20__if_all_numbers_2_through_6_occur(self):
        input_dice = 2, 3, 4, 5, 6
        expected_score = 20
        actual_score = yahtzee.score_for_large_straight(*input_dice)
        self.assertEqual(actual_score, expected_score)

    def test__score_for_full_house__is_sum_of_all_dice__if_one_number_occurs_exactly_twice__and__if_one_number_occurs_exactly_three_times(self):
        test_arguments = [
            ((1, 1, 2, 2, 2), 8),
            ((2, 2, 3, 3, 4), 0),
            ((4, 4, 4, 4, 4), 0),
        ]

        for input_dice, expected_score in test_arguments:
            actual_score = yahtzee.score_for_full_house(*input_dice)
            self.assertEqual(actual_score, expected_score)


if __name__ == '__main__':
    unittest.main()
