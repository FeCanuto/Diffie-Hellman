# Troca de Chave usando Diffie-Hellman

import random


def primo(n):  # Verifica se o número é primo
    '''
Verifica se um numero gerado é primo
>>> primo(11) == True
'''
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i+2) == 0):
            return False
        i += 6
    return True


def gerar_primo():  # gerar o número primo - p e q
    '''
    Gera um numero primo aleatório
    >>> gerar_primo()
    7
    '''

    while True:  # 2**2048 são as chaves padrão RSA
        x = random.randrange(1, 100)  # definindo o alcançe dos números primos
        if (primo(x) == True):
            return x