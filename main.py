n = int(input())

arr = list(map(int, input().split()))

l = arr[0]
start = None
for i in range(1, len(arr)):
    if l > arr[i]:
        start = i - 1
        break
    l = arr[i];

if start is None:
    print("yes")
    print(1, 1)
    raise SystemExit

end = n
for i in range(start + 1, len(arr)):
    if l < arr[i]:
        end = i
        break

arr[start:end] = reversed(arr[start:end])

l = arr[0]
for i in range(1, n):
    if l > arr[i]:
        print("no")
        break
    l = arr[i]
else:
    print("yes")
    print(start + 1, end)
