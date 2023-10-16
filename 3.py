def factorial():
    n = int(input('Write a  number:'))
    fc = 1
    while n > 1:
        fc = fc * n
        n = n - 1

    print(fc)
factorial()

