import unittest
from homework import RandomGen


class HomeworkTests(unittest.TestCase):

    def setUp(self):
        self.random_gen = RandomGen()
        self.random_gen._random_nums = [-1, 0, 1, 2, 3]
        self.random_gen._probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

    def test_random_nums_and_probabilities_same_len(self):
        assert len(self.random_gen._random_nums) == len(self.random_gen._probabilities), \
            "_random_nums and probabilities must be of the same length"

    def test_probabilities_sum_to_roughly_1(self):
        assert abs(sum(self.random_gen._probabilities) - 1) < 0.0001, "_probabilities must sum to 1"

    def test_all_probability_positive(self):
        assert all(probability > 0 for probability in self.random_gen._probabilities), \
            "all _probabilities must be positive"

    def test_random_nums_unique(self):
        assert len(set(self.random_gen._random_nums)) == len(self.random_gen._random_nums), \
            "_random_nums must be unique"

    def test_random_nums_not_empty(self):
        assert len(self.random_gen._random_nums) > 0, "_random_nums must not be empty"

    def test_probabilities_not_empty(self):
        assert len(self.random_gen._probabilities) > 0, "_probabilities must not be empty"

    def test_random_nums_type(self):
        assert all(isinstance(val, (int, float)) for val in self.random_gen._random_nums), \
            "_random_nums must be numbers"

    def test_probabilities_type(self):
        assert all(isinstance(val, (int, float)) for val in self.random_gen._probabilities), \
            "_probabilities must be numbers"

    def test_next_num_returns_from_random_nums(self, test_times=1000):
        random_nums = self.random_gen._random_nums
        for _ in range(test_times):
            assert self.random_gen.next_num() in random_nums, "next_num method must return one of the _random_nums"

    def test_next_num_returns_value_roughly_within_set_probability(self, test_times=1000, tolerance=0.1):
        random_nums = self.random_gen._random_nums
        probabilities = self.random_gen._probabilities
        number_appearances = {random_num: 0 for random_num in random_nums}

        for _ in range(test_times):
            number_appearances[self.random_gen.next_num()] += 1

        for random_num, n_appearances in number_appearances.items():
            pct_times_appeared = n_appearances / test_times
            appearance_probability = probabilities[random_nums.index(random_num)]
            assert abs(pct_times_appeared - appearance_probability) < tolerance, \
                f"next_num method must return values within set _probabilities given the tolerance of {tolerance}"


if __name__ == '__main__':
    unittest.main()
