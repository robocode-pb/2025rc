# # input = отримати с клавіатури тип "str"
# # numbers = int(input())
# #
# #
# # if numbers == 0:
# #     print("введене число 0")
# # else:
# #     numbers = numbers * 2
# #     print(numbers)
# name = input ("введіть ім'я? ")
# age = input ("який вік? ")
# hobby = input ("яке в тебе хоббі? ")
#
# if name:
#     print("Привіт "+name)
# else:
#     print('Ти никто?')
#
#
# if int(age)  <= 18:
#     print ("Иди в школу!")
#
# elif int(age) >= 100:
#     print ("Zombie!")
# else:
#     print ("Иди в унивірсітит!")
#     if ' ':
#         print("Цікаве в тебе хоббі " + hobby)
#     else:
#         print('В тебе нема хоббі?')
apples = 10
eatenaookes = input ('Скільки пітон зїв яблук? ')
eatinbutters = input ('Скільки пітон зїв бутерів? ')
if  int(eatenaookes) == 10 or int(eatinbutters) == 5:
    print("Пітон наївся")
elif  int(eatenaookes) > 10 or int(eatinbutters) > 5:
    print("Пітон лопнув")
else:
    print("Пітон хоче їсти ще")