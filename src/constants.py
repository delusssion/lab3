FACTORIAL_MAX_ITERATIVE = 1000
FACTORIAL_MAX_RECURSIVE = 500

FIBO_MAX_ITERATIVE = 10000
FIBO_MAX_RECURSIVE = 1000

RADIX_DEFAULT_BASE = 10

COUNTING_SORT_MAX_VALUE = 100000
COUNTING_SORT_MAX_RANGE_RATIO = 100

BUCKET_SORT_MIN_VALUE = 0.0
BUCKET_SORT_MAX_VALUE = 1.0

BENCHMARK_SMALL_TIME = 0.001
BENCHMARK_MEDIUM_TIME = 0.01
BENCHMARK_ARRAY_SIZES = [100, 1000]
BENCHMARK_NEARLY_SORTED_SWAPS = {100: 10, 1000: 50}
BENCHMARK_DUPLICATES_UNIQUE = 10

SEQUENCES_OPTIONS = [
    'Факториал (итеративный)',
    'Факториал (рекурсивный)', 
    'Число Фибоначчи (итеративный)',
    'Число Фибоначчи (рекурсивный)',
    'Назад в главное меню'
]

SORTING_OPTIONS = [
    'Сортировка пузырьком',
    'Быстрая сортировка',
    'Сортировка подсчетом',
    'Поразрядная сортировка',
    'Ведерная сортировка',
    'Пирамидальная сортировка',
    'Назад в главное меню'
]

STACK_IMPLEMENTATIONS = [
    'Стек на связном списке',
    'Стек на списке', 
    'Стек на очередях',
    'Назад в главное меню'
]

STACK_OPERATIONS = [
    'Push (добавить элемент)',
    'Pop (удалить и вернуть элемент)',
    'Peek (посмотреть верхний элемент)',
    'Проверить пустоту',
    'Размер стека',
    'Минимальный элемент',
    'Назад'
]

BENCHMARK_ARRAY_NAMES = {
    'Случайный 100': 'Случ_100',
    'Случайный 1000': 'Случ_1000', 
    'Почти отсорт. 100': 'Почти_100',
    'Почти отсорт. 1000': 'Почти_1000',
    'Много дубликатов': 'Дубликаты',
    'Обратный 100': 'Обрат_100',
    'Обратный 1000': 'Обрат_1000'
}
