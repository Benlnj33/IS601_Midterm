import cmd
import operator

class CalculatorREPL(cmd.Cmd):
    prompt = 'calculator> '

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
        except Exception as e:
            print('Error:', e)

if __name__ == '__main__':
    CalculatorREPL().cmdloop()
