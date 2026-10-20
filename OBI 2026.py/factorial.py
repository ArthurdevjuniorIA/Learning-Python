def factorial(number):
    number = number
    for i in range(1,number):
        number = number * i
    if number == 0:
        print(1)
        return
    print(number)
factorial(int(input(" ")))