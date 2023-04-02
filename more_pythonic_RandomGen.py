import random
import itertools


class RandomGen:  # no need to inherit from object in Python 3 unless we want compatability with Python 2
    def __init__(self, params):  # pass params as a dict to make RandomGen more flexible
        self._random_nums = params.get('random_nums')
        self._probabilities = params.get('probabilities')
        self.assert_correct_input()
        # so we don't need to compute them every time in next_num, and we've already done assert_correct_input
        self._cum_weights = list(itertools.accumulate(self._probabilities))

    def assert_correct_input(self):
        assert len(self._random_nums) == len(self._probabilities), "random_nums and probabilities should be same length"
        assert abs(sum(self._probabilities) - 1) < 0.0001, "probabilities should add up to 1"
        assert all(probability > 0 for probability in self._probabilities), "all probabilities should be positive"
        assert len(set(self._random_nums)) == len(self._random_nums), "random_nums should be unique"
        assert len(self._random_nums) > 0, "random_nums should not be empty"
        assert len(self._probabilities) > 0, "probabilities should not be empty"
        assert all(isinstance(num, (int, float)) for num in self._random_nums), "random_nums should be integers"
        assert all(isinstance(val, (int, float)) for val in self._probabilities), "probabilities should be integers"

    def next_num(self) -> int:
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        :return: one of the random_nums or None
        """
        # no need for try/except here, because we already checked the input in assert_correct_input
        return random.choices(population=self._random_nums, cum_weights=self._cum_weights, k=1)[0]


if __name__ == '__main__':
    nums_dict = {
        'random_nums': [-1, 0, 1, 2, 3],
        'probabilities': [0.01, 0.3, 0.58, 0.1, 0.01]
    }
    random_gen = RandomGen(nums_dict)
    number_appearances = {random_num: 0 for random_num in random_gen._random_nums}
    for _ in range(10000):
        number_appearances[random_gen.next_num()] += 1
    print(number_appearances)
