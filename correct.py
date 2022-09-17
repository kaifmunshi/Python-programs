largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        num = int(num)
        if largest is None or num > largest:
            largest = num
        elif smallest is None or num < smallest:
            smallest = num

    except:
        print("Invalid input")
        continue
print("smallest number is",smallest)
print("largest number is ",largest)
