import random as rn
import time


def get_question(digit1: int = 2, digit2: int = 2):
    a = rn.randint(10 ** (digit1 - 1), 10**digit1 - 1)
    b = rn.randint(10 ** (digit2 - 1), 10**digit2 - 1)
    return a, b, a * b


if __name__ == "__main__":
    while True:
        tic = time.perf_counter()
        a, b, ans = get_question(2)
        print(f"{a} * {b} = ?")
        user_ans = int(input())
        toc = time.perf_counter()
        if user_ans == "exit":
            print(f"Bye!")
            break
        if user_ans == ans:
            print(f"Correct! ({toc - tic:0.4f}s)")
        else:
            print(f"Wrong! ({toc - tic:0.4f}s)")
