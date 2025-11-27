import time
from src.output import COLORAMA_AVAILABLE, Fore, format_output


def _color(color):
    return color if COLORAMA_AVAILABLE else None


def timeit_once(func, *args, **kwargs):
    '''
    Измеряет время выполнения функции один раз.
    '''
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time


def benchmark_sorts(arrays, algos):
    '''
    Запускает бенчмарк сортировок на различных массивах.
    '''
    results = {}
    
    for algo_name, algo_func in algos.items():
        results[algo_name] = {}
        print(format_output(f'Тестируем {algo_name}...'))
        
        for array_name, array in arrays.items():
            test_array = array.copy()
            
            try:
                time_taken = timeit_once(algo_func, test_array)
                results[algo_name][array_name] = time_taken
                if time_taken < 0.001:
                    color = Fore.GREEN
                elif time_taken < 0.01:
                    color = Fore.YELLOW
                else:
                    color = Fore.RED
                print(format_output(f'  {array_name}: {time_taken:.6f} сек', _color(color)))
                
            except RecursionError:
                print(format_output(f'  {array_name}: ПРОПУЩЕНО - превышена глубина рекурсии', _color(Fore.RED)))
                results[algo_name][array_name] = None
            except MemoryError:
                print(format_output(f'  {array_name}: ПРОПУЩЕНО - недостаточно памяти', _color(Fore.RED)))
                results[algo_name][array_name] = None
            except ValueError as e:
                print(format_output(f'  {array_name}: ПРОПУЩЕНО - {e}', _color(Fore.YELLOW)))
                results[algo_name][array_name] = None
            except Exception as e:
                print(format_output(f'  {array_name}: ПРОПУЩЕНО - ошибка: {e}', _color(Fore.RED)))
                results[algo_name][array_name] = None
    
    return results


def print_benchmark_results(results):
    '''
    Выводит результаты бенчмарка.
    '''
    print(format_output('\n' + '='*80))
    print(format_output('РЕЗУЛЬТАТЫ БЕНЧМАРКА'))
    print(format_output('='*80))
    
    array_names = set()
    for algo_results in results.values():
        array_names.update(algo_results.keys())
    array_names = sorted(array_names)
    
    short_names = {}
    for name in array_names:
        if name == 'Случайный 100': short_names[name] = 'Случ_100'
        elif name == 'Случайный 1000': short_names[name] = 'Случ_1000'
        elif name == 'Почти отсорт. 100': short_names[name] = 'Почти_100'
        elif name == 'Почти отсорт. 1000': short_names[name] = 'Почти_1000'
        elif name == 'Много дубликатов': short_names[name] = 'Дубликаты'
        elif name == 'Обратный 100': short_names[name] = 'Обрат_100'
        elif name == 'Обратный 1000': short_names[name] = 'Обрат_1000'
        elif name == 'Float случайный 100': short_names[name] = 'F_Случ100'
        elif name == 'Float случайный 1000': short_names[name] = 'F_Случ1000'
        elif name == 'Float почти отсорт. 100': short_names[name] = 'F_Почти100'
        elif name == 'Float почти отсорт. 1000': short_names[name] = 'F_Почти1000'
        else: short_names[name] = name[:10]
    
    header = 'Алгоритм'.ljust(16)
    for name in array_names:
        header += f' {short_names[name]:>10}'
    print(header)
    print('-' * (16 + 11 * len(array_names)))
    
    for algo_name, algo_results in results.items():
        row = algo_name.ljust(16)
        for array_name in array_names:
            time_val = algo_results.get(array_name)
            if time_val is None:
                row += format_output(' {0:>10}'.format('N/A'), _color(Fore.RED))
            else:
                if time_val < 0.001:
                    color = Fore.GREEN
                elif time_val < 0.01:
                    color = Fore.YELLOW
                else:
                    color = Fore.RED
                row += format_output(f' {time_val:>10.6f}', _color(color))
        print(row)

def run_comprehensive_benchmark():
    '''
    Запускает комплексный бенчмарк с различными типами массивов.
    '''
    from src.generator_tests import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array
    from src.sorting import bubble_sort, quick_sort, counting_sort, radix_sort, heap_sort, bucket_sort
    
    int_arrays = {
        'Случайный 100': rand_int_array(100, 1, 1000),
        'Случайный 1000': rand_int_array(1000, 1, 10000),
        'Почти отсорт. 100': nearly_sorted(100, 10),
        'Почти отсорт. 1000': nearly_sorted(1000, 50),
        'Много дубликатов': many_duplicates(1000, 10),
        'Обратный 100': reverse_sorted(100),
        'Обратный 1000': reverse_sorted(1000),
    }
    
    float_arrays = {
        'Float случайный 100': rand_float_array(100, 0.0, 1.0),
        'Float случайный 1000': rand_float_array(1000, 0.0, 1.0),
        'Float почти отсорт. 100': [x/100 for x in nearly_sorted(100, 10)],
        'Float почти отсорт. 1000': [x/1000 for x in nearly_sorted(1000, 50)],
    }
    
    algos = {
        'Пузырьковая': bubble_sort,
        'Быстрая': quick_sort,
        'Подсчетом': counting_sort,
        'Поразрядная': radix_sort,
        'Пирамидальная': heap_sort,
        'Корзинная': bucket_sort,
    }
    
    all_arrays = {**int_arrays, **float_arrays}
    
    print(format_output('ЗАПУСК КОМПЛЕКСНОГО БЕНЧМАРКА'))
    print(format_output('='*50))
    
    results = benchmark_sorts(all_arrays, algos)
    print_benchmark_results(results)
    
    return results
