import random

def generateRandomInteger(min_value, max_value):
    """
    Generate a random number between min_value and max_value.

    Args:
        min_value (int): The minimum value for the random number.
        max_value (int): The maximum value for the random number.

    Returns:
        int: A random number between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def selectRandomArithmetic():
    """
    Select randomly one of the arithmetic operators: '+', '-', or '*'.

    Args:
        None

    Returns:
        str: A random arithmetic operator that could be '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])

def calculateMathematicalExpression(first_number, second_number, operator):
    """
    Calculates the mathematical expression based on the first_number, second_number and operator.

    Args:
       first_number (int): The first number in the expression.
       second_number (int): The second number in the expression.
       operator (str): Arithmetic operator ('+', '-', or '*').

    Returns:
       tuple: A tuple containing the arithmetic expression and its result.
    """
    mathematical_expression = f"{first_number} {operator} {second_number}"
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    else:
        result = first_number * second_number
    return mathematical_expression, result

def math_quiz():
    # Initialize score and total number of questions
    s = 0
    t_q = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    for _ in range(t_q):
        # Generate 2 random numbers and select a random arithmetic operator
        first_number = generateRandomInteger(1, 10)
        second_number = generateRandomInteger(1, 5)
        operator = selectRandomArithmetic()
        # Calculate the Mathematical expression
        problem, answer = calculateMathematicalExpression(first_number, second_number, operator)
        print(f"\nQuestion: {problem}")
        # Error Handling by checking whether the user input is valid
        while True:
            try:
                user_answer = input("Your answer: ")
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        # Check user's answer and update the score
        if user_answer == answer:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()