def add_numbers(*args):
    print(args, type(args))
    return sum(args)

print(add_numbers(2, 3, 4))        # (2, 3, 4) → 9
print(add_numbers(1, 2, 3, 4, 5))  # (1, 2, 3, 4, 5) → 15
