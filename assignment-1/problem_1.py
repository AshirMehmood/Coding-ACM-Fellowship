# average of n numbers

num = input("How many numbers? ")
num = int(num)
numbers = []

for n in range(0,num):
    x = int(input("Enter number: "))
    numbers.append(x)

total = sum(numbers)
average = total/num
print(average)    