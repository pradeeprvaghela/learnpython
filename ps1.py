try:
    with open("1.txt") as a:
        print(a.read())
    with open("2.txt") as b:
        print(b.read())
    with open("3.txt") as c:
        print(c.read())
except Exception as e:
    print(e)