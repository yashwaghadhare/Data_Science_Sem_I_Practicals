# Using while loop
num = int(input("Enter a number: "))
rev = 0
temp = num

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reversed (using while loop):", rev)

# Using for loop
num = int(input("\nEnter another number: "))
rev = 0

for _ in range(len(str(num))):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed (using for loop):", rev)
