# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

for i in range(10000):
    number = i + 1

    if number % n == 2:
        print(number)
