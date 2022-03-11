# Неборский Мирон 421-4. Лист 1 #7
def get_input(a) -> float:
    while True:
        print(f'Введите значение {a}: ')
        try:
            return float(input())
        except ValueError as hmm:
            print(f'Введеная строка не является числом.')


def ex1(n: float):
    summand = 1
    k = 2
    while summand <= n:
        number = 1 / k
        summand += number
        k += 1
    return summand


def print_ans(ans: float):
    print(f'Ответ: {ans}')


def main():
    n = get_input('n')
    ans = ex1(n)
    print_ans(ans)


if __name__ == '__main__':
    main()
