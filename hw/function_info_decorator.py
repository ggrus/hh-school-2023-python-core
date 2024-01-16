from datetime import datetime

def function_info_decorator(func):
    def wrapper(*args, **kwargs):
        print('\nСтарт функции', func.__qualname__)
        start = datetime.now()
        result = func(*args, **kwargs)
        print('Финиш. Затраченное время: ', datetime.now() - start)
        print('Результат выполнения:\n', result)
        return result
    return wrapper