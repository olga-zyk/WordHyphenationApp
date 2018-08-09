from context import Context


class App:
    MESSAGE_WELCOME: str = 'Welcome!\nPlease select the operating mode:'
    MESSAGE_EXIT: str = 'See you later! :)\n'
    MODES = {'interactive': '1', 'batch': '2'}

    def __init__(self, config: dict):
        self.config = config
        self.operating_mode = '\tInteractive:\t' + self.MODES['interactive'] \
                              + '\n\tBatch:\t\t\t' + self.MODES['batch'] + '\n'

    def run(self):
        print(App.MESSAGE_WELCOME)

        while True:
            print(self.operating_mode)
            strategy_input = input().strip()

            try:
                context = Context(self.get_mode_name(strategy_input), self.config)
                context.execute()
            except KeyError:
                print('Incorrect mode selected: ', strategy_input)
            except NotImplementedError:
                print('This feature has not been implemented yet, sorry :-(')

            self.ask_for_continue()

    def get_mode_name(self, mode):
        for mode_name, value in self.MODES.items():
            if value == mode:
                return mode_name

    def ask_for_continue(self):
        print('Do you want to continue?[Y/n]')
        user_input = input().strip().lower()
        if user_input == 'n':
            print(App.MESSAGE_EXIT)
            exit()
