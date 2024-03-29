import os
import importlib
import cmd
import math
import logging
from plugin_interface import Plugin

# Configure logging
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example logging statements
logging.info('Application started')
logging.debug('Debug message')
logging.error('Error message')

# Function to load plugins
def load_plugins():
    plugins = []
    plugin_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = 'plugins.' + filename[:-3]
            module = importlib.import_module(module_name)
            for obj_name in dir(module):
                obj = getattr(module, obj_name)
                if isinstance(obj, type) and issubclass(obj, Plugin) and obj != Plugin:
                    plugins.append(obj())
    return plugins

class CalculatorREPL(cmd.Cmd):
    prompt = 'Bens_calculator> '
    HISTORY_FILE = 'test.csv'

    def __init__(self):
        super().__init__()
        # Set up logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.FileHandler('calculator.log'))

    def do_add(self, arg):
        try:
            operands = [float(x) for x in arg.split()]
            result = sum(operands)
            print('Result:', result)
        except ValueError:
            print('Invalid input. Please enter numbers separated by spaces.')

    def do_subtract(self, arg):
        try:
            operands = [float(x) for x in arg.split()]
            result = operands[0] - sum(operands[1:])
            print('Result:', result)
        except ValueError:
            print('Invalid input. Please enter numbers separated by spaces.')

    def do_multiply(self, arg):
        try:
            operands = [float(x) for x in arg.split()]
            result = 1
            for operand in operands:
                result *= operand
            print('Result:', result)
        except ValueError:
            print('Invalid input. Please enter numbers separated by spaces.')

    def do_divide(self, arg):
        try:
            operands = [float(x) for x in arg.split()]
            if len(operands) < 2:
                print('Invalid input. Please enter at least two numbers.')
                return
            result = operands[0] / operands[1]
            print('Result:', result)
        except ValueError:
            print('Invalid input. Please enter numbers separated by spaces.')
        except ZeroDivisionError:
            print('Cannot divide by zero.')

    def default(self, arg):
        try:
            result = eval(arg)
            print('Result:', result)
            self.logger.info(f'Input: {arg}, Output: {result}')  # Log the input and output
        except Exception as e:
            print('Error:', e)
            self.logger.error(f'Error: {e}')  # Log errors

# Load plugins
plugins = load_plugins()

# Print loaded plugins
print("Loaded plugins:")
for plugin in plugins:
    print(f"- {plugin.get_name()}")

# Integrate plugin commands into calculator application
for plugin in plugins:
    for command, func in plugin.get_commands().items():
        setattr(CalculatorREPL, 'do_' + command, func)

if __name__ == '__main__':
    CalculatorREPL().cmdloop()