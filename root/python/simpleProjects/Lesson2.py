text = "ADMIN, BOGDAN, DAVID | eva, python, robocode"
word = input("Input your account: ")
plov = input("шукати у перщій чи друній ")
print(word)
middle = int(len(text)/2) + 1
if word in text :
    print("Аккаунт знайшли")
else:
    print("Аккаунт не знайдено")

True and False