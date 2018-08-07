from hyphenation_alg import Hyphenator
from strategy_interface import StrategyInterface


class BatchMode(StrategyInterface):

    def execute(self):
        user_input = input('Type in the path to the file: ').strip()
        file = open(user_input, 'r')
        data = [line.strip() for line in file.readlines()]
        file.close()

        batch = Hyphenator(self.config)
        for word in data:
            word = batch.hyphenate(word)

            with open('hyphenated.txt', 'a+') as file:
                file.write(word + '\n')

        print('The words were hyphenated and saved to the file. Please, check the output file.')
