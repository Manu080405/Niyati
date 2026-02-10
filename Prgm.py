n=int(input("Enter the value : "))
print(n,"is the values")

n=0
a=0
r=n/a
print(r)

n=int(input("Enter value : "))
b=int(n)+5
print(b)

try:
    n = input("Enter the value ")
    if not n.isdigit():
        raise TypeError("Input must be an integer")
    n = int(n)
    if n == 0:
        raise ValueError("Value cannot be zero")
    res = 100 / n

except TypeError as te:
    print(te)

except ValueError as ve:
    print(ve)

else:
    print("Result is", res)

finally:
    print("Execution completed")



