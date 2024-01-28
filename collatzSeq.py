# collatzSequence.py

print('Go ahead and type an integer: ')
new_int = input()

def collatz(num):
    if num % 2 == 0:
        return num // 2
    elif num % 2 == 1:
        return 3 * num + 1
    else:
        print("Error")

while new_int != 1:
    new_int = collatz(int(new_int))
    print(new_int)

