from hyphenation_alg import Hyphenator
from strategy_interface import StrategyInterface
import time


class InteractiveMode(StrategyInterface):

    def execute(self):
        word = input('Type in the word for hyphenation: ').strip()

        interactive = Hyphenator(self.config)

        start_time = time.time()
        result = interactive.hyphenate(word)
        end_time = time.time()
        time_diff = end_time - start_time

        print('before: {0}\nafter: {1}'.format(word, result) + '\n')
        print('The running time is: {0} seconds'.format(round(time_diff, 5)))
