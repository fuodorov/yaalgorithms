n = int(input())
array = input().split(' ')

somethingWasChanged = False

while True:
    somethingChanged = False
    for i in range(n - 1):
        if int(array[i]) > int(array[i + 1]):
            array[i], array[i + 1] = array[i + 1], array[i]
            somethingChanged = True
            somethingWasChanged = True

    if somethingChanged:
        print(' '.join(array))
    else:
        break

if not somethingWasChanged:
    print(' '.join(array))
