import random

lizt = []

for index in range(random.randint(1,10)):

    number = random.randint(0,20)
    lizt.append(number)
    print(index," - індекс, число - ", number)
print(len(lizt), ' - довжина списку')