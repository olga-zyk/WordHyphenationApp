from hyphenation_alg import Hyphenator
from strategy_interface import StrategyInterface
from timer import Timer


class InteractiveMode(StrategyInterface):

    def execute(self):
        word = input('Type in the word for hyphenation: ').strip()

        timer = Timer()
        hyphenator = Hyphenator(self.config)

        start = timer.start()
        result = hyphenator.hyphenate(word)
        stop = timer.stop()
        time_diff = timer.measurement(start, stop)

        print('before: {0}\nafter: {1}'.format(word, result) + '\n')
        print('The running time is: {0} seconds'.format(round(time_diff, 5)))
