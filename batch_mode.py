from hyphenation_alg import Hyphenator
from strategy_interface import StrategyInterface
from timer import Timer


class BatchMode(StrategyInterface):

    def execute(self):
        user_input = input('Type in the path to the input file: ').strip()
        file = open(user_input, 'r')
        words = [line.strip() for line in file.readlines()]
        file.close()

        timer = Timer()
        hyphenator = Hyphenator(self.config)

        hyphenated_words = []
        start = timer.start()
        for word in words:
            word = hyphenator.hyphenate(word)
            hyphenated_words.append(word)
        stop = timer.stop()
        time_diff = timer.measurement(start, stop)

        formatted_string = '\n'.join(hyphenated_words)

        complete_name = input('Type in the path to output file: ').strip()

        file = open(complete_name, 'w')
        file.write(formatted_string)
        file.close()

        print('The file was successfully saved to {0}'.format(complete_name))
        print('The running time is: {0} seconds'.format(round(time_diff, 5)))
