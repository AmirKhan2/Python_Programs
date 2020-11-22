def zero(a, b):
    return a / b


try:
    print("Resource Open")
    zero(2, 0)
    z = int(input("Enter a number: "))
    print(z)
except ZeroDivisionError as e:
    print(e, "error")
except ValueError as e:
    print("Incorrect Input")
finally:
    print("Resource Closed")
