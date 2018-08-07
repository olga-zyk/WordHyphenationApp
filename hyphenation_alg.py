import re

"""
By default looks for patterns.txt in the same directory
"""


class Hyphenator:
    DEFAULT_CONFIG: dict = {'patterns_file': 'patterns.txt', 'debug': False}

    def __init__(self, config: dict):
        self.config = {**self.DEFAULT_CONFIG, **config}
        # self.patterns_file = config.get('patterns_file') or self.DEFAULT_CONFIG.get('patterns_file')

        with open(self.config['patterns_file'], 'rt') as file:
            self.data_list = [line.strip() for line in file.readlines()]

    def is_verbose(self):
        return self.config.get('debug') is True

    def hyphenate(self, word):
        letters = list(word)

        array_for_numbers = [0 for i in range(len(word) + 1)]

        # pattern without dots and numbers
        clean_patterns = []
        for pattern in self.data_list:
            pattern = re.sub(r'[\.\d+]|[\.\d+]', '', pattern)
            clean_patterns.append(pattern)

        # create a dictionary for 'patterns': 'clean_patterns'
        patterns_dict = dict(zip(self.data_list, clean_patterns))

        for pattern, clean_pattern in patterns_dict.items():
            pattern_position = word.find(clean_pattern)
            while pattern_position > -1:
                word_offset = pattern_position + len(clean_pattern)
                if (pattern[0] == '.' and pattern_position == 0) or (
                        pattern[-1] == '.' and pattern_position == len(word) - len(clean_pattern)) or (
                        pattern[0] != '.' and pattern[-1] != '.'):
                    # print(pattern)
                    for char in pattern:
                        if char.isalpha():
                            pattern_position += 1
                        if char.isdigit() and int(char) > array_for_numbers[pattern_position]:
                            array_for_numbers[pattern_position] = int(char)
                pattern_position = word.find(clean_pattern, word_offset)

        hyphenated_word = letters
        offset = 0
        for i in range(1, len(array_for_numbers) - 1):
            if array_for_numbers[i] % 2 != 0:
                letters.insert(i + offset, '-')
                offset += 1
            hyphenated_word = ''.join(letters)
        return hyphenated_word
