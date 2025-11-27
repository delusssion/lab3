import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.ui import sequences_menu, sorting_menu, stack_menu, benchmark_menu
from src.sequences import Sequences
from src.output import format_output


def print_line(message):
    print(format_output(message))


def main():
    sequences = Sequences()
    
    while True:
        try:
            print_line('\n' + '='*50)
            print_line('ГЛАВНОЕ МЕНЮ')
            print_line('='*50)
            print_line('1. Последовательности (Факториал и Фибоначчи)')
            print_line('2. Сортировки')
            print_line('3. Структуры данных (Стек)')
            print_line('4. Бенчмарки')
            print_line('5. Выход')
            print_line('='*50)
            
            choice = input('Выберите раздел (1-5): ').strip()
            
            if choice == '1':
                sequences_menu(sequences)
            elif choice == '2':
                sorting_menu()
            elif choice == '3':
                stack_menu()
            elif choice == '4':
                benchmark_menu()
            elif choice == '5':
                print_line('Выход из программы...')
                break
            else:
                print_line('Неверный выбор! Попробуйте снова.')
                
        except KeyboardInterrupt:
            print_line('\n\nПрограмма прервана пользователем')
            break
        except EOFError:
            print_line('\n\nНеожиданный конец ввода')
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print_line('\n\nПрограмма завершена')
    except Exception as e:
        print_line(f'\nНеожиданная ошибка: {e}')
