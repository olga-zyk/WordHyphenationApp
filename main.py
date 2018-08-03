from hyphenation_alg import Hyphenation

config: dict = {'data_file': 'list_of_patterns.txt'}

app = Hyphenation(config)
app.run()
