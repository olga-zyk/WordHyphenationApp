from hyphenation_alg import Hyphenator
from strategy_interface import StrategyInterface
import time
import os.path


class BatchMode(StrategyInterface):

    def execute(self):
        user_input = input('Type in the path to the file: ').strip()
        file = open(user_input, 'r')
        data = [line.strip() for line in file.readlines()]
        file.close()

        batch = Hyphenator(self.config)

        hyphenated_words = []
        start_time = time.time()
        for word in data:
            word = batch.hyphenate(word)
            hyphenated_words.append(word)
        end_time = time.time()
        time_diff = end_time - start_time

        formatted_string = '\n'.join(hyphenated_words)

        path_to_file = input('Type in the full path to output folder: ').strip()
        doc_title = input('Type in the title for output file: ').strip()
        complete_name = os.path.join(path_to_file, doc_title + '.txt')

        file = open(complete_name, 'w+')
        file.write(formatted_string)
        file.close()

        print('The hyphenated words were successfully saved to the file. Please, check the output file.')
        print('The running time is: {0} seconds'.format(round(time_diff, 5)))

