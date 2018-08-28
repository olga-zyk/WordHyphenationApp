import abc


class ApplicationMode(metaclass=abc.ABCMeta):
    def __init__(self):
        self.config = None

    def set_config(self, config):
        self.config = config

    @abc.abstractmethod
    def execute(self):
        pass
