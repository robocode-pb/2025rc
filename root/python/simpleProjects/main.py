import painter

while("True"):
    painter.set_speed(10000)
    print("Яку фігуру виберете?")
    # Повідомляємо користувачу про фігури
    print('1-Circle')
    print('2-Square')
    print("3-Star")
    print("4-Flag")
    # Отримати від користувача номер фігури а не букву
    userChoice = int(input())

   # Якщо - if
    if userChoice > 4:
      print("error 101")
      print("Переглянути правильні варианті")
    if userChoice < 4:
      print("successful")
    if userChoice == 1:
        painter.draw_circle()
    if userChoice == 2:
        painter.draw_square()
    if userChoice == 3:
        painter.draw_star()
    if userChoice == 4:
        painter.draw_flag()


    '''
    5 - ціле число integer - int
    3.14 - дробове (float) -
    '''