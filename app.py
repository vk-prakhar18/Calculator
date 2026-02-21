import calculator

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
print("5. Floor Division")
print("6. Modulo")
print("7. Exponential")

choice = input("Choose Operation(1/2/3/4/5/6/7):  ")

a = float(input("Enter Your First Number:  "))
b = float(input("Enter Your Second Number:  "))

if choice == "1":
    print("Result: ", calculator.add(a, b))
elif choice == "2":
    print("Result: ", calculator.subtract(a,b))
elif choice == "3":
    print("Result: ", calculator.multiply(a, b))
elif choice == "4":
    print("Result: ", calculator.division(a, b))
elif choice == "5":
    print("Result: ", calculator.floor_division(a, b))
elif choice == "6":
    print("Result: ", calculator.modulo(a,b))
elif choice == "7":
    print("Result: ", calculator.exponential(a,b))
else:
    print("Bhaad Mei Jao")