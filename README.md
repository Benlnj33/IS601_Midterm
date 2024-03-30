### Ben's IS601_Midterm Project

LINK TO VIDEO: https://drive.google.com/file/d/120e4bEPcio7VxivGu4PlSPHXJdO9lLlT/view?usp=sharing

My name is Ben Lim and I am in Professir William's IS 601-852 class
Here is the Advanced Python Calculator for my Software Engineering Graduate Course Midterm (IS601)
This calculator app is a Python based command line calculator that allows users to perform basic arithmetic operations, manage calculation history, and customize functionalities using plugins.

To set up the Calculator App, pls follow these steps that i wrote out:

Clone the repository:
- git clone https://github.com/Benlnj33/IS601_Midterm

Navigate to the project directory: 
- cd calculator

Activate a virtual environment (optional but recommended):
- source venv/bin/activate  # On Unix/Linux
- .\venv\Scripts\activate   # On Windows

Install dependencies:
- pip install -r requirements.txt

Run the calculator:
- pip calculator.py

-------------------------------------------------------------------

### Dependencies

The Calculator App requires Python 3 and the following dependencies:

pandas: For managing calculation history.
pytest: For comprehensive testing.
pylint: For static code analysis

-------------------------------------------------------------------

### Calculator Operations

The Calculator App supports the following arithmetic operations:

- Addition (Example: 3+4)
- Subtraction (Example: 5-2)
- Multiplication (Example: 6*3)
- Division (Example: 2/1)

and via the trig plugin:

- sin (Example: sin 40)
- cos (Example: cos 50)
- tan (Example: tan 60)

Users can perform these operations by entering commands in the command-line interface. Like operand1 + operand 2.

-------------------------------------------------------------------

### History Management

The Calculator App utilizes the pandas library for managing calculation history. Calculation history is stored in a CSV file (history.csv) and can be loaded, saved, cleared, or modified using the provided commands.

Load history: load history
Save history: save history
Clear history: clear history
Delete specific history record: delete record <index>

-------------------------------------------------------------------

### Environmental Variables

The Calculator App uses the python-dotenv and os for loading environmental variables.

-------------------------------------------------------------------

### REPL Interface

The Calculator App provides a REPL command-line interface where users can interact with the calculator, perform operations, and manage calculation history. The interface is intuitive and user-friendly.

-------------------------------------------------------------------

### Command Design Patterns

The Calculator App implements the Command design pattern to encapsulate arithmetic operations as commands. This design pattern allows for easy extensibility and customization through plugins.

-------------------------------------------------------------------

### Comprehensive Testing with Pytest

The Calculator App is thoroughly tested using the pytest framework. Unit tests cover various functionalities, ensuring the reliability and robustness of the application.

-------------------------------------------------------------------

### Requirements.txt

The requirements.txt file contains a list of dependencies required to run the Calculator App. It includes all necessary libraries and versions for seamless installation.
