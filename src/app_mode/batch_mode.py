from src.hyphenator.hyphenation_alg import Hyphenator
from src.app_mode.mode_interface import ApplicationMode
from src.utils.timer import Timer
from src.utils.file_processing import FileProcessing


class BatchMode(ApplicationMode):

    def execute(self):
        user_input = input('Type in the path to the input file: ').strip()
        with FileProcessing(user_input, 'r') as file:
            words = [line.strip() for line in file.readlines()]

        timer = Timer()
        hyphenator = Hyphenator(self.config)

        hyphenated_words = []
        timer.start()
        for word in words:
            word = hyphenator.hyphenate(word)
            hyphenated_words.append(word)
        timer.stop()
        time_diff = timer.duration()

        formatted_string = '\n'.join(hyphenated_words)

        complete_name = input('Type in the path to output file: ').strip()

        with FileProcessing(complete_name, 'w') as file:
            file.write(formatted_string)

        print('The file was successfully saved to {0}'.format(complete_name))
        print('The running time is: {0} seconds'.format(round(time_diff, 5)))
