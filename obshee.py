import time

def consider_time(method):
    def data(*args, **kwargs):
        print(f"Выполняется функция {method.__name__}")
        start = time.time()
        method(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения функции в секундах: {end - start}")
    return data

@consider_time
def pretend_that_we_are_working():
    for i in range(2000):
        n = 4
        for i in range(1, n + 1):
            print("* " * i)

@consider_time
def we_also_pretend_that_we_are_working(n):
    for i in range(n):
        a = 2 + 5 + 7 + 10 + 15 +22222220
        print(a)
if __name__ == '__main__':
    pretend_that_we_are_working()
    we_also_pretend_that_we_are_working(1700)
