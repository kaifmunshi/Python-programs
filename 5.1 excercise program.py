largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        err = float(num)
    except:
        print("Invalid input")
        continue
    for val in [num]:
        if largest is None:
            largest = val
        elif val > largest:
            largest = val
    for value in [num]:
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value

print("Maximum", largest)
print("Minimum", smallest)