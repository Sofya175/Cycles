"""x_wall = 120
x_person = 10

while x_person < x_wall:
    x_wall = x_person + 5
    print('хлоп')
"""

# поросить пользователя вводить числа
# суммировать эти числа до достижения 100
# в конце сказать "спасибо" и вывести получившуюся сумму

summa = 0
while summa < 100:
    number = int(input('введите число ')) # ввести число и прибавить его к сумме
    summa += number # summa = summa + number
print('спасибо ')   # вывести "Спасибо"
print( summa )      # вывести summa
