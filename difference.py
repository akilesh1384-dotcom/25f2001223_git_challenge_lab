# difference.py
# This module provides a function to subtract two numbers

def subtract(a, b):
    """
    Returns the difference of two numbers.
    
    Parameters:
    a (int or float): First number
    b (int or float): Second number
    
    Returns:
    int or float: a - b
    """
    return a - b

# Example usage
if __name__ == "__main__":
    num1 = 10
    num2 = 4
    print(f"The difference of {num1} and {num2} is {subtract(num1, num2)}")
