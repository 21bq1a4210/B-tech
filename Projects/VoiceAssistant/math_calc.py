import math
math_operations = {
    'add': '+',
    'plus': '+',
    'subtract': '-',
    'minus': '-',
    'multiply': '*',
    'times': '*',
    'divide': '/',
    'divide by': '/',
    'square': '**2',
    'cube': '**3',
    'power': '**'
}

def calculate(expression):
    expression = expression.replace('calculate', '')
    try:
        for word, opp in math_operations.items():
            expression = expression.replace(word, opp)

        result = eval(expression)
        return result
    except Exception as e:
        return str(e)