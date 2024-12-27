print("Select an option:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Arithmetic mean")
print("6. Median")
print("7. Exit")
 
def mean(numbers):
    return sum(numbers) / len(numbers)
 
def median(numbers):
    n = len(numbers)
    if n % 2 != 0:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
 
 
def addition(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
 
 
while True:
    choice = input("Enter choice: ")
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        if choice == '7':
            print("Exiting...")
            break
 
        quantity = int(input("Enter quantity of numbers to operate: "))
        print("Enter numbers to operate") 
        numbers = []
        for _ in range(quantity):
            numbers.append(int(input()))
 
        if choice == '1':
            print("Result: ", addition(numbers))
        elif choice == '2':
            print("Result: ", numbers[0] - addition((numbers[1:])))
        elif choice == '3':
            result = 1
            for num in numbers:
                result *= num
            print("Result: ", result)
        elif choice == '4':
            if 0 in numbers[1:]:
                print("Division by zero is not allowed")
            else:
                result = numbers[0]
                for num in numbers[1:]:
                    result /= num
                print("Result: ", result)
        elif choice == '5':
            print("Result:", mean(numbers))
        elif choice == '6':
            print("Result:", median(numbers))
    else:
        print("Invalid choice")