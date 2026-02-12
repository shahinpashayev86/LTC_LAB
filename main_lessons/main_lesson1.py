### --Sadə Kalkulyator
a = float(input("1-ci reqemi daxil edin: "))
operations = input("elemeliyti secin: ( +, -, *, /): ")
b = float(input("2-ci reqemi daxil edin: "))



if operations == "+":
    result = a+b
    print(result)
elif operations == "-":
    result = a-b
    print(result)
elif operations == "*":
    result = a*b
    print(result)
elif operations == "/":
    if b == 0:
        print("0 -ra bolmek olmaz")
    else:
        result = a/b
        print(result)
else:
    print("elemeliyti duzgun secilmeyib")

