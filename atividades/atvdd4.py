#A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
def gerar_fibonacci():
    a, b = 0, 1
    fibonacci_sequence = []

    while a <= 500:
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

resultado = gerar_fibonacci()
print(resultado)