from abc import ABC, abstractmethod

class Plugin(ABC):
    """
    Interface for calculator plugins.
    """

    @abstractmethod
    def get_name(self):
        """
        Get the name of the plugin.
        """
        pass

    @abstractmethod
    def get_commands(self):
        """
        Get a dictionary of plugin commands.
        The dictionary keys are command names, and the values are corresponding functions.
        """
        pass