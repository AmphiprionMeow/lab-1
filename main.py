from math import sqrt


def main():

    prompt = "введите переменные a b c, через пробел: "
    while True:
        try:
            print("ax^2 + bx + c = 0:")
            a, b, c = map(int, input(prompt).split())
            break
        except ValueError:
            prompt = 'Введите 3 переменных через пробел: '

    dis = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % dis)

    if dis > 0:
        x1 = (-b + sqrt(dis)) / (2 * a)
        x2 = (-b - sqrt(dis)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif dis == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)

    else:
        print("Корней нет")


if __name__ == "__main__":
  main()