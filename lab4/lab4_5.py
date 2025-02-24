def generate_squares(N):
    for i in range(1, N + 1):
        yield i * i

N = 10
squares = generate_squares(N)

for square in squares:
    print(square)