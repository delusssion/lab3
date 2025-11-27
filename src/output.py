try:
    from colorama import Fore, Style, init
    init()
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

    class Fore:
        GREEN = ''
        YELLOW = ''
        RED = ''

    class Style:
        RESET_ALL = ''


def format_output(message, color=None):
    '''Форматирует строку для вывода в консоль с учетом цвета.'''
    if COLORAMA_AVAILABLE and color:
        return f'{color}{message}{Style.RESET_ALL}'
    return message
