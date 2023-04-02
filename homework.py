import random
import itertools


class RandomGen(object):
    # Values that may be returned by next_num()
    _random_nums = []
    # Probability of the occurence of random_nums
    _probabilities = []

    def next_num(self) -> int | None:
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        try:
            cum_weights = list(itertools.accumulate(self._probabilities))
            return random.choices(population=self._random_nums, cum_weights=cum_weights, k=1)[0]
        except Exception as e:
            print(f'exception in next_num:', e)
            return None
