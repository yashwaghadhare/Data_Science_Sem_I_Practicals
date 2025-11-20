num = int(input("Enter a number: "))
rev = 0
temp = num

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print(rev)

num = int(input("Enter another number: "))
rev = 0

for _ in range(len(str(num))):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)
