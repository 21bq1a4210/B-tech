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
    'power': '**',
    'sin': 'math.sin',
    'cos': 'math.cos',
    'tan': 'math.tan',
    'pi': 'math.pi',
    'e': 'math.e',
    'factorial': 'math.factorial'
}

def calculate(expression):
    expression = expression.replace('calculate', '')
    split = expression.split()
    split = [(num.replace(num, f'({num})') if num.isdigit() else num) for num in split]
    expression = ''.join(x for x in split)
    try:
        for word, opp in math_operations.items():
            expression = expression.replace(word, opp)

        result = eval(expression)
        return round(result, 2)
    except Exception as e:
        return str(e)