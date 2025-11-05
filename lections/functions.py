# def countFish(a, b):
#     sum = a + b
#     return f"Всего {sum} шт."
#
# a = int(input())
# b = int(input())
# print(countFish(a, b))

def countFish(a, b):
    sum = a + b
    prod = a * b
    return sum, prod


a = int(input())
b = int(input())
sum1, prod1 = countFish(a, b)
print(f'Сумма {sum1}, Произведение {prod1}')

# s2 = 'global'
# def test():
#    s1 = 'Local1'
#    print(s2)

# test()
# print(s1)