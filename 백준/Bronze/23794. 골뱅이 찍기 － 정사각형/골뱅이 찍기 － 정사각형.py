N = int(input())

# for i in range(N+2):
#     print('@'+' '*(N)+'@')

print('@'*(N+2))
for i in range(N):
    print(('@'+' '*(N)+'@'), sep='/n')
print('@'*(N+2))