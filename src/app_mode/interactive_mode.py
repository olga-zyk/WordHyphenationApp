from src.hyphenator.hyphenation_alg import Hyphenator
from src.app_mode.mode_interface import ApplicationMode
from src.utils.timer import Timer


class InteractiveMode(ApplicationMode):

    def execute(self):
        word = input('Type in the word for hyphenation: ').strip()

        timer = Timer()
        hyphenator = Hyphenator(self.config)

        timer.start()
        result = hyphenator.hyphenate(word)
        timer.stop()
        time_diff = timer.duration()

        print('before: {0}\nafter: {1}'.format(word, result) + '\n')
        print('The running time is: {0} seconds'.format(round(time_diff, 5)))
