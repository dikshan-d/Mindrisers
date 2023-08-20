try:
    a = int(input("Enter the Number: "))
    # print(a)
# except ValueError:
except Exception as e:
    print(e)
#     print("Only Number is Allowed")
try:
    print(a)
finally:
    print("Hello")
# except NameError:
#     print("A not defined")
