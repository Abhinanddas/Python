from concurrent.futures import ThreadPoolExecutor
from time import sleep
from threading import current_thread

values = [i for i in range(100)]


def cube(x):
    r = f"{current_thread().getName()}||\n"
    print(f'Cube of {x}:{x*x*x}', r)


if __name__ == '__main__':
    result = []
    with ThreadPoolExecutor(max_workers=5) as exe:
        exe.submit(cube, 10)
        result = exe.map(cube, values)

        # for r in result:
            # print(r)


# from concurrent.futures import ThreadPoolExecutor, Future
# from threading import current_thread
# from time import sleep
# from random import randint

# # imagine these are urls
# URLS = [i for i in range(100)]


# def do_some_work(url, a, b):
#     """Simulates some work"""
#     sleep(2)
#     rand_num = randint(a, b)
#     if rand_num == 5:
#         raise ValueError("No! 5 found!")
#     r = f"{current_thread().getName()}||: {url}_{rand_num}\n"
#     return r


# def show_fut_results(fut: Future):
#     """Callback for future shows results or shows error"""
#     if not fut.exception():
#         print(fut.result())
#     else:
#         print(f"{current_thread().getName()}|  Error: {fut.exception()}\n")


# if __name__ == '__main__':
#     with ThreadPoolExecutor(max_workers=10) as pool:
#         for i in URLS:
#             _fut = pool.submit(do_some_work, i, 1, 10)
#             _fut.add_done_callback(show_fut_results)