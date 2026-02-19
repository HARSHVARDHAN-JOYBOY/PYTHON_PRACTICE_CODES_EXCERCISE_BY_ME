numbers = [1, 2, 3, 4]
squares = [cube for n in numbers if (cube:=n*n*n)]
print(squares)