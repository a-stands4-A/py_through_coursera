A, B, N = int(input()), int(input()), int(input())

print(int(str(A * N) + '0')//10 + B * N // 100, B * N % 100)
