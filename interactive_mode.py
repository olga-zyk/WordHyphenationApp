from hyphenation_alg import Hyphenator
from strategy_interface import StrategyInterface


class InteractiveMode(StrategyInterface):

    def execute(self):
        word = input('Type in the word for hyphenation: ').strip()
        interactive = Hyphenator(self.config)
        result = interactive.hyphenate(word)
        print('before: {0}\nafter: {1}'.format(word, result))
