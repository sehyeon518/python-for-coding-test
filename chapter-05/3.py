# 5-3.py
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

# RecursionError: maximum recursion depth exceeded while pickling an object
