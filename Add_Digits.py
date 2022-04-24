num= int(input())
def add_digits(num):
        return (num - 1) % 9 + 1 if num > 0 else 0
print(add_digits(num))