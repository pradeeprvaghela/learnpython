n=int(input("enter number: "))
table=[n*i for i in range(1,11)]
print(table)
with open("Tables.txt","a") as f:
    f.write(str(table)+ "\n")