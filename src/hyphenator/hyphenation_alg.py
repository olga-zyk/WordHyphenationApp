import re
from src.utils.file_processing import FileProcessing
import collections

"""
By default looks for patterns.txt in the same directory
"""


class Hyphenator:
    SEARCH_LINEAR = 'linear'
    SEARCH_OPTIMIZED = 'optimized'
    DEFAULT_CONFIG: dict = {'patterns_file': './src/data/patterns.txt', 'debug': False, 'search': SEARCH_LINEAR}

    def __init__(self, config: dict):
        self.config = {**self.DEFAULT_CONFIG, **config}
        # self.patterns_file = config.get('patterns_file') or self.DEFAULT_CONFIG.get('patterns_file')

        with FileProcessing(self.config['patterns_file'], 'r') as file:
            self.data_list = [line.strip() for line in file.readlines()]

        if self.config['search'] == self.SEARCH_LINEAR:
            self.patterns_dict = self.load_patterns()
            self.find_patt = self.patt_search_linear
        elif self.config['search'] == self.SEARCH_OPTIMIZED:
            self.grouped_dict = self.load_patterns_group()
            self.find_patt = self.patt_search_optimized
        else:
            raise ValueError('Unknown search algorithm specified: {0}'.format(self.config['search']))

    def load_patterns_group(self):
        patterns_dict = self.load_patterns()

        alphabet = [chr(letter) for letter in range(97, 123)]
        # create nested dictionary; sort patterns_dict alphabetically
        grouped_dict = collections.defaultdict(dict)
        for i in range(0, len(alphabet) - 1):
            for pattern, value in patterns_dict.items():
                if value.startswith(alphabet[i]):
                    grouped_dict[alphabet[i]][pattern] = value
        return grouped_dict

    def load_patterns(self):
        # pattern without dots and numbers
        clean_patterns = []
        for pattern in self.data_list:
            pattern = re.sub(r'[\.\d+]|[\.\d+]', '', pattern)
            clean_patterns.append(pattern)
        # create a dictionary for 'patterns': 'clean_patterns'
        return dict(zip(self.data_list, clean_patterns))

    def is_verbose(self):
        return self.config.get('debug') is True

    def hyphenate(self, word):
        letters = list(word)
        hyphenated_word = word

        array_for_numbers = self.find_patt(word)

        offset = 0
        for i in range(1, len(array_for_numbers) - 1):
            if array_for_numbers[i] % 2 != 0:
                letters.insert(i + offset, '-')
                offset += 1
            hyphenated_word = ''.join(letters)
        return hyphenated_word

    def patt_search_linear(self, word):
        array_for_numbers = [0 for i in range(len(word) + 1)]

        for pattern, clean_pattern in self.patterns_dict.items():
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

        return array_for_numbers

    def patt_search_optimized(self, word):
        array_for_numbers = [0 for i in range(len(word) + 1)]

        for letter in list(word):
            for pattern, clean_pattern in self.grouped_dict[letter].items():
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
        return array_for_numbers
