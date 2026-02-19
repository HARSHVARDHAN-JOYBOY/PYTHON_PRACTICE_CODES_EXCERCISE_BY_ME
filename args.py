def sum(*args):
    total=0
    for i in args:
        total+=i
    return total

print(sum(23,66,46,34,5))