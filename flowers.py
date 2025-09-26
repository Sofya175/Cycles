# Цветочки
n =int(input('введите количество '))

left = "G"
central = 'C'
right = 'V'

for i in range(n):
    # действия Миши
    right, central = central, right
    # действия Тани
    left, central = central, left

print(left + central + right)
