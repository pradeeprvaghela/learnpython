try:
    a=int(input("enter number: "))
    b=int(input("enter number: "))
    print(f"{a} / {b} = {a/b}")
except ZeroDivisionError as v:
    print("zero cant be divided")