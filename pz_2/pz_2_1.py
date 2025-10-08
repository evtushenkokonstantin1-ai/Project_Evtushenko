try:
    L = (float(input("Введите длину в сантиметрах: ")))
    A = L // 100
    print(A)
except ValueError:
    print("Ошибка! Использован неверный тип данных.")