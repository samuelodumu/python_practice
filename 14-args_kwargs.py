#!/usr/bin/python3


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


def say_hi_sum_numbers(*args, **kwargs):
    total = 0
    for num in args:
        total += num
    print(f"The sum of numbers is {total}")

    if kwargs is not None:
        for key, value in kwargs.items():
            print(f"Key:, {key}, Value: {value}")

if __name__ == "__main__":
    say_hi_sum_numbers(12, 8, 20, 5, name='Samuel', age=19)
    print("=========================")
    test_args_kwargs(1, 2, 3)
