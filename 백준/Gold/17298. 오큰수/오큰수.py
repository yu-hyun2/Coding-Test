N = int(input())
arr = list(map(int, input().split()))
result = [-1] * N  # Initialize the result array with -1
stack = []

for i in range(N):
    while stack and arr[i] > arr[stack[-1]]:
        top = stack.pop()
        result[top] = arr[i]
    stack.append(i)

output = ' '.join(map(str, result))
print(output)