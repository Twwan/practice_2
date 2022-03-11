# Лист 2 #9
def get_input(a) -> int:
    while True:
        print(f'Введите значение {a}: ')
        try:
            return int(input())
        except ValueError as hmm:
            print(f'Введеная строка не является целым числом.')


def summ(a: int):
    summ = 0
    for i in range(a, 101):
        summ += i
    return summ


def print_ans(ans: int):
    print(f'Ответ: {ans}')


def main():
    a = get_input('a')
    otv = summ(a)
    print_ans(otv)

if __name__ == '__main__':
    main()