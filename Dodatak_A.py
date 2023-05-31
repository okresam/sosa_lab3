import os
import getpass
import math
import ast

class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        if (type(self.a) != int and type(self.a) != float) or (type(self.b) != int and type(self.b) != float):
            raise ValueError()

        if self.b == 0:
            return None

        return self.a / self.b

def square_root(n):
    """Returns the square root of n. If n is negative, returns NaN."""
    if type(n) != int:
        raise ValueError()

    if n < 0:
        return None

    return math.sqrt(n)

def validate_string_length(s):
    """Cuts the string if it exceeds length of 5 characters and returns it. If the input is not a string, throws ValueError."""
    if type(s) != str:
        raise ValueError()
    
    if len(s) > 5:
        return s[:5]

    return s

def login_success():
    a = float(input("A = "))
    b = float(input("B = "))
    ops_manager = OperationsManager(a, b)
    print(ops_manager.perform_division())
 
    expression = input('Enter a mathematical formula to calculate: ')
    print ("Result: ", ast.literal_eval(expression))


if __name__ == "__main__":
    user = input("Username: ")
    #password = getpass.getpass("Password: ")
    if user != "root":
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        login_success()

