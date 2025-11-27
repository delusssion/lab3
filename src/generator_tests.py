import random


def rand_int_array(n, lo, hi, distinct=False):
    '''
    Генерирует массив случайных целых чисел.
    '''
    if distinct:
        if hi - lo + 1 < n:
            raise ValueError(f'Невозможно сгенерировать {n} уникальных чисел в диапазоне [{lo}, {hi}]')
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n, swaps):
    '''
    Генерирует почти отсортированный массив.
    '''
    if n == 0:
        return []
    
    arr = list(range(n))
    
    if n == 1 or swaps == 0:
        return arr
    
    max_swaps = min(swaps, n * (n - 1) // 2)
    
    for _ in range(max_swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr

def many_duplicates(n, k_unique=5):
    '''
    Генерирует массив с большим количеством дубликатов.
    '''
    if k_unique <= 0:
        raise ValueError('k_unique должен быть положительным')
    
    unique_values = list(range(k_unique))
    return [random.choice(unique_values) for _ in range(n)]


def reverse_sorted(n):
    '''
    Генерирует обратно отсортированный массив.
    '''
    return list(range(n - 1, -1, -1))


def rand_float_array(n, lo=0.0, hi=1.0):
    '''
    Генерирует массив случайных вещественных чисел.
    '''
    return [random.uniform(lo, hi) for _ in range(n)]
