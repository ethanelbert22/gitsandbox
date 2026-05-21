def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def temp_converter_celsius(celsius):
    return (celsius * 9/5) + 32

def temp_converter_fahrenheit(fahrenheit):
    return (fahrenheit - 32) * 5/9