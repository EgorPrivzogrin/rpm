if __name__ == '__main__':
    a = float(input('коэффицент a:'))
    b = float(input('коэффицент b:'))
    c = float(input('коэффицент c:'))
    D = b ** 2 - (4 * a * c)
    if D < 0:
        print('Корней нет')
    elif D > 0:
        x1 = (-b + D ** (1 / 2)) / (2 * a)
        x2 = (-b - D ** (1 / 2)) / (2 * a)
        print(x1, x2)
    else:
        print(-b / (2 * a))
