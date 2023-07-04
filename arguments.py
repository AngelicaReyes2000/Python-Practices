import sys

for argument in sys.argv:
    print(argument)


total = 1
del(sys.argv[0])
for argument in sys.argv:
    try:
        number = float(argument)
        total *= number
    except Exception as e:
        print(e)
        print("Only numbers can be provide")
        sys.exit(1)

print(total)
