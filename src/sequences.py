import functools
from src.constants import *


class Sequences:
    '''
    Класс для работы с математическими последовательностями.
    Реализует вычисление факториала и чисел Фибоначчи.
    '''
    
    def __init__(self):
        self.factorial_recursive.cache_clear()
        self.fibo_recursive.cache_clear()
    
    def factorial(self, n: int) -> int:
        '''Вычисляет факториал числа n итеративным методом.'''
        if not isinstance(n, int):
            raise TypeError('Аргумент должен быть целым числом')
        
        if n < 0:
            raise ValueError('Факториал определен только для неотрицательных чисел')
        
        if n > FACTORIAL_MAX_ITERATIVE:
            raise ValueError('Слишком большое число для вычисления факториала')
        
        result = 1
        for i in range(1, n + 1):
            result *= i
        
        return result

    @functools.lru_cache(maxsize=1000)
    def factorial_recursive(self, n: int) -> int:
        '''Вычисляет факториал числа n рекурсивным методом.'''
        if not isinstance(n, int):
            raise TypeError('Аргумент должен быть целым числом')
        
        if n < 0:
            raise ValueError('Факториал определен только для неотрицательных чисел')
        
        if n > FACTORIAL_MAX_RECURSIVE:
            raise RecursionError('Слишком большая глубина рекурсии для факториала')
        
        if n == 0 or n == 1:
            return 1
        
        result = n * self.factorial_recursive(n - 1)
        
        return result

    def fibo(self, n: int) -> int:
        '''Вычисляет n-ное число Фибоначчи итеративным методом.'''
        if not isinstance(n, int):
            raise TypeError('Аргумент должен быть целым числом')
        
        if n < 0:
            raise ValueError('Число Фибоначчи определено только для неотрицательных индексов')
        
        if n > FIBO_MAX_ITERATIVE:
            raise ValueError('Слишком большое число для вычисления числа Фибоначчи')
        
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b

    @functools.lru_cache(maxsize=1000)
    def fibo_recursive(self, n: int) -> int:
        '''Вычисляет n-ное число Фибоначчи рекурсивным методом.'''
        if not isinstance(n, int):
            raise TypeError('Аргумент должен быть целым числом')
        
        if n < 0:
            raise ValueError('Число Фибоначчи определено только для неотрицательных индексов')
        
        if n > FIBO_MAX_RECURSIVE:
            raise RecursionError('Слишком большая глубина рекурсии для чисел Фибоначчи')
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        result = self.fibo_recursive(n - 1) + self.fibo_recursive(n - 2)
        
        return result
