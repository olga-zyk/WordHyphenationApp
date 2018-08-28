from src.app_mode.batch_mode import BatchMode
from src.app_mode.interactive_mode import InteractiveMode


class Context:
    STRATEGY_MAPPING = {'interactive': InteractiveMode, 'batch': BatchMode}

    def __init__(self, strategy_input, config: dict):
        self.strategy = self.get_strategy(strategy_input)
        self.config = config

    def get_strategy(self, strategy_input):
        if self.STRATEGY_MAPPING[strategy_input] is not None:
            return self.STRATEGY_MAPPING[strategy_input]()

    def execute(self):
        if self.strategy is not None:
            self.strategy.set_config(self.config)
            self.strategy.execute()
