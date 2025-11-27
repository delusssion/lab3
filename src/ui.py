from src.sequences import Sequences
from src.sorting import *
from src.stack import LinkedListStack, ListStack, QueueStack
from src.constants import *
from src.generator_tests import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array
from src.benchmarks import run_comprehensive_benchmark, benchmark_sorts, print_benchmark_results
from src.output import Fore, Style, format_output


def print_line(message, color=None):
    '''Единый вывод с поддержкой цвета.'''
    print(format_output(message, color))


def benchmark_menu():
    '''Меню для бенчмарков.'''
    while True:
        try:
            print_line('\n' + '-'*40)
            print_line('БЕНЧМАРКИ')
            print_line('-'*40)
            print_line('1. Комплексный бенчмарк сортировок')
            print_line('2. Сравнить алгоритмы на текущем массиве')
            print_line('3. Назад в главное меню')
            print_line('-'*40)
            
            choice = input('Выберите операцию (1-3): ').strip()
            
            if choice == '1':
                run_comprehensive_benchmark()
                
            elif choice == '2':
                compare_algorithms_on_current_array()
                
            elif choice == '3':
                break
            else:
                print_line('Неверный выбор! Попробуйте снова.', Fore.RED)
                    
        except KeyboardInterrupt:
            print_line('\nВозврат в главное меню...', Fore.RED)
            break
        except EOFError:
            print_line('\nВозврат в главное меню...', Fore.RED)
            break


def compare_algorithms_on_current_array():
    '''Сравнивает все алгоритмы сортировки на одном массиве.'''
    try:
        print_line('\nСОЗДАНИЕ ТЕСТОВОГО МАССИВА')
        print_line('1. Ввести массив вручную')
        print_line('2. Сгенерировать массив')
        input_choice = input('Выберите способ (1-2): ').strip()
        
        if input_choice not in ['1', '2']:
            print_line('Ошибка: выберите 1 или 2', Fore.RED)
            return
        
        if input_choice == '1':
            input_str = input('Введите список чисел через пробел: ')
            try:
                arr = list(map(int, input_str.split()))
                if len(arr) == 0:
                    print_line('Ошибка: массив не может быть пустым', Fore.RED)
                    return
            except ValueError:
                print_line('Ошибка: введите только целые числа через пробел', Fore.RED)
                return
            
        elif input_choice == '2':
            print_line('\nТИПЫ ГЕНЕРАЦИИ МАССИВА:')
            print_line('1. Случайный целочисленный массив')
            print_line('2. Почти отсортированный массив')
            print_line('3. Массив с большим количеством дубликатов')
            print_line('4. Обратно отсортированный массив')
            print_line('5. Случайный вещественный массив (для корзинной)')
            
            gen_choice = input('Выберите тип массива (1-5): ').strip()
            
            if gen_choice not in ['1', '2', '3', '4', '5']:
                print_line('Ошибка: выберите тип массива от 1 до 5', Fore.RED)
                return
            
            try:
                n = int(input('Введите количество элементов: '))
                if n <= 0:
                    print_line('Ошибка: количество элементов должно быть положительным', Fore.RED)
                    return
            except ValueError:
                print_line('Ошибка: введите целое число', Fore.RED)
                return
            
            if gen_choice == '1':
                try:
                    lo = int(input('Введите нижнюю границу: '))
                    hi = int(input('Введите верхнюю границу: '))
                    if hi < lo:
                        print_line('Ошибка: верхняя граница должна быть больше нижней', Fore.RED)
                        return
                except ValueError:
                    print_line('Ошибка: введите целые числа для границ', Fore.RED)
                    return
                    
                distinct_input = input('Уникальные элементы? (y/n): ').strip().lower()
                if distinct_input not in ['y', 'n']:
                    print_line('Ошибка: введите y или n', Fore.RED)
                    return
                distinct = distinct_input == 'y'
                
                try:
                    arr = rand_int_array(n, lo, hi, distinct=distinct)
                except ValueError as e:
                    print_line(f'Ошибка генерации: {e}', Fore.RED)
                    return
                
            elif gen_choice == '2':
                try:
                    swaps = int(input('Введите количество случайных обменов: '))
                    if swaps < 0:
                        print_line('Ошибка: количество обменов не может быть отрицательным', Fore.RED)
                        return
                except ValueError:
                    print_line('Ошибка: введите целое число для количества обменов', Fore.RED)
                    return
                    
                arr = nearly_sorted(n, swaps)
                
            elif gen_choice == '3':
                try:
                    k_unique = int(input('Введите количество уникальных элементов: '))
                    if k_unique <= 0:
                        print_line('Ошибка: количество уникальных элементов должно быть положительным', Fore.RED)
                        return
                except ValueError:
                    print_line('Ошибка: введите целое число для уникальных элементов', Fore.RED)
                    return
                    
                try:
                    arr = many_duplicates(n, k_unique)
                except ValueError as e:
                    print_line(f'Ошибка генерации: {e}', Fore.RED)
                    return
                
            elif gen_choice == '4':
                arr = reverse_sorted(n)
                
            elif gen_choice == '5':
                try:
                    lo = float(input('Введите нижнюю границу: '))
                    hi = float(input('Введите верхнюю границу: '))
                    if hi < lo:
                        print_line('Ошибка: верхняя граница должна быть больше нижней', Fore.RED)
                        return
                except ValueError:
                    print_line('Ошибка: введите числа для границ', Fore.RED)
                    return
                    
                arr = rand_float_array(n, lo, hi)
        
        print_line(f'\nТестовый массив ({len(arr)} элементов): {arr[:20]}{'...' if len(arr) > 20 else ''}', Fore.GREEN)
        
        algos = {
            'Пузырьковая': bubble_sort,
            'Быстрая': quick_sort,
            'Подсчетом': counting_sort,
            'Поразрядная': lambda a: radix_sort(a, 10),
            'Пирамидальная': heap_sort,
            'Корзинная': bucket_sort,
        }
        
        results = benchmark_sorts({'Текущий массив': arr}, algos)
        print_benchmark_results(results)
        
    except ValueError as e:
        print_line(f'Ошибка ввода: {e}', Fore.RED)
    except Exception as e:
        print_line(f'Ошибка: {e}', Fore.RED)

def sequences_menu(sequences):
    '''Меню для работы с последовательностями.'''
    while True:
        try:
            print_line('\n' + '-'*40)
            print_line('ПОСЛЕДОВАТЕЛЬНОСТИ')
            print_line('-'*40)
            for i, option in enumerate(SEQUENCES_OPTIONS, 1):
                print_line(f'{i}. {option}')
            print_line('-'*40)
            
            choice = input('Выберите операцию (1-5): ').strip()
            
            if choice == '5':
                break
            
            if choice in ['1', '2', '3', '4']:
                try:
                    n = int(input('Введите число n: '))
                    
                    if choice == '1':
                        result = sequences.factorial(n)
                        print_line(f'{n}! = {result}', Fore.GREEN)
                    elif choice == '2':
                        result = sequences.factorial_recursive(n)
                        print_line(f'{n}! = {result} (рекурсивный)', Fore.GREEN)
                    elif choice == '3':
                        result = sequences.fibo(n)
                        print_line(f'F({n}) = {result}', Fore.GREEN)
                    elif choice == '4':
                        result = sequences.fibo_recursive(n)
                        print_line(f'F({n}) = {result} (рекурсивный)', Fore.GREEN)
                        
                except ValueError as e:
                    print_line(f'Ошибка ввода: {e}', Fore.RED)
                except Exception as e:
                    print_line(f'Ошибка вычисления: {e}', Fore.RED)
                    
        except KeyboardInterrupt:
            print_line('\nВозврат в главное меню...', Fore.RED)
            break
        except EOFError:
            print_line('\nВозврат в главное меню...', Fore.RED)
            break


def sorting_menu():
    '''Меню для работы с сортировками.'''
    while True:
        try:
            print_line('\n' + '-'*40)
            print_line('СОРТИРОВКИ')
            print_line('-'*40)
            for i, option in enumerate(SORTING_OPTIONS, 1):
                print_line(f'{i}. {option}')
            print_line('-'*40)
            
            choice = input('Выберите сортировку (1-7): ').strip()
            
            if choice == '7':
                break
            
            if choice in ['1', '2', '3', '4', '5', '6']:
                try:
                    print_line('\nВВОД МАССИВА:')
                    print_line('1. Ввести массив вручную')
                    print_line('2. Сгенерировать массив автоматически')
                    input_choice = input('Выберите способ (1-2): ').strip()
                    
                    if input_choice == '1':
                        input_str = input('Введите список чисел через пробел: ')
                        
                    elif input_choice == '2':
                        print_line('\nТИПЫ ГЕНЕРАЦИИ МАССИВА:')
                        print_line('1. Случайный целочисленный массив')
                        print_line('2. Почти отсортированный массив')
                        print_line('3. Массив с большим количеством дубликатов')
                        print_line('4. Обратно отсортированный массив')
                        print_line('5. Случайный вещественный массив')
                        
                        gen_choice = input('Выберите тип массива (1-5): ').strip()
                        n = int(input('Введите количество элементов: '))
                        
                        if gen_choice == '1':
                            lo = int(input('Введите нижнюю границу: '))
                            hi = int(input('Введите верхнюю границу: '))
                            distinct = input('Уникальные элементы? (y/n): ').strip().lower() == 'y'
                            arr = rand_int_array(n, lo, hi, distinct=distinct)
                            
                        elif gen_choice == '2':
                            swaps = int(input('Введите количество случайных обменов: '))
                            arr = nearly_sorted(n, swaps)
                            
                        elif gen_choice == '3':
                            k_unique = int(input('Введите количество уникальных элементов: '))
                            arr = many_duplicates(n, k_unique)
                            
                        elif gen_choice == '4':
                            arr = reverse_sorted(n)
                            
                        elif gen_choice == '5':
                            lo = float(input('Введите нижнюю границу: '))
                            hi = float(input('Введите верхнюю границу: '))
                            arr = rand_float_array(n, lo, hi)
                            
                        else:
                            print_line('Неверный выбор типа массива!', Fore.RED)
                            continue
                        
                        print_line(f'Сгенерированный массив: {arr}', Fore.GREEN)
                        input_str = ' '.join(map(str, arr))
                        
                    else:
                        print_line('Неверный выбор способа ввода!', Fore.RED)
                        continue
                    
                    if choice == '5':
                        arr = list(map(float, input_str.split()))
                    else:
                        arr = list(map(int, input_str.split()))
                    
                    print_line(f'Исходный список: {arr}')
                    print_line(f'Количество элементов: {len(arr)}')
                    
                    if choice == '1':
                        result = bubble_sort(arr)
                        print_line(f'Отсортированный список (пузырьком): {result}', Fore.GREEN)
                    elif choice == '2':
                        result = quick_sort(arr)
                        print_line(f'Отсортированный список (быстрая): {result}', Fore.GREEN)
                    elif choice == '3':
                        result = counting_sort(arr)
                        print_line(f'Отсортированный список (подсчетом): {result}', Fore.GREEN)
                    elif choice == '4':
                        base_input = input('Введите основание системы счисления (по умолчанию 10): ')
                        base = int(base_input) if base_input.strip() else RADIX_DEFAULT_BASE
                        result = radix_sort(arr, base)
                        print_line(f'Отсортированный список (поразрядная): {result}', Fore.GREEN)
                    elif choice == '5':
                        buckets_input = input('Введите количество ведер (Enter для автоматического): ')
                        buckets = int(buckets_input) if buckets_input.strip() else None
                        result = bucket_sort(arr, buckets)
                        print_line(f'Отсортированный список (ведерная): {result}', Fore.GREEN)
                    elif choice == '6':
                        result = heap_sort(arr)
                        print_line(f'Отсортированный список (пирамидальная): {result}', Fore.GREEN)
                        
                except ValueError as e:
                    print_line(f'Ошибка ввода: {e}', Fore.RED)
                except Exception as e:
                    print_line(f'Ошибка сортировки: {e}', Fore.RED)
                    
        except KeyboardInterrupt:
            print_line('\nВозврат в главное меню...', Fore.RED)
            break
        except EOFError:
            print_line('\nВозврат в главное меню...', Fore.RED)
            break


def stack_menu():
    '''Меню для работы со стеком.'''
    while True:
        try:
            print_line('\n' + '-'*40)
            print_line('СТЕК')
            print_line('-'*40)
            for i, option in enumerate(STACK_IMPLEMENTATIONS, 1):
                print_line(f'{i}. {option}')
            print_line('-'*40)
            
            choice = input('Выберите реализацию стека (1-4): ').strip()
            
            if choice == '4':
                break
            
            if choice in ['1', '2', '3']:
                if choice == '1':
                    stack = LinkedListStack()
                    stack_name = 'связный список'
                elif choice == '2':
                    stack = ListStack()
                    stack_name = 'список'
                else:
                    stack = QueueStack()
                    stack_name = 'очереди'
                
                stack_operations_menu(stack, stack_name)
                
        except KeyboardInterrupt:
            print_line('\nВозврат в главное меню...', Fore.RED)
            break
        except EOFError:
            print_line('\nВозврат в главное меню...', Fore.RED)
            break


def stack_operations_menu(stack, stack_name):
    '''Меню операций со стеком.'''
    while True:
        try:
            print_line(f'\nОперации со стеком ({stack_name})')
            print_line('-'*30)
            for i, option in enumerate(STACK_OPERATIONS, 1):
                print_line(f'{i}. {option}')
            print_line('-'*30)
            
            choice = input('Выберите операцию (1-7): ').strip()
            
            if choice == '7':
                break
            
            try:
                if choice == '1':
                    x = int(input('Введите число для добавления: '))
                    stack.push(x)
                    print_line(f'Добавлен элемент: {x}', Fore.GREEN)
                elif choice == '2':
                    result = stack.pop()
                    print_line(f'Удален элемент: {result}', Fore.GREEN)
                elif choice == '3':
                    result = stack.peek()
                    print_line(f'Верхний элемент: {result}', Fore.GREEN)
                elif choice == '4':
                    result = stack.is_empty()
                    print_line(f'Стек пуст: {result}', Fore.GREEN)
                elif choice == '5':
                    result = len(stack)
                    print_line(f'Размер стека: {result}', Fore.GREEN)
                elif choice == '6':
                    result = stack.min()
                    print_line(f'Минимальный элемент: {result}', Fore.GREEN)
            except IndexError as e:
                print_line(f'Ошибка: {e}', Fore.RED)
            except Exception as e:
                print_line(f'Ошибка: {e}', Fore.RED)
                
        except KeyboardInterrupt:
            print_line('\nВозврат в меню стека...', Fore.RED)
            break
        except EOFError:
            print_line('\nВозврат в меню стека...', Fore.RED)
            break
