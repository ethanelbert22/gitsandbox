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

def vowel_count(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count