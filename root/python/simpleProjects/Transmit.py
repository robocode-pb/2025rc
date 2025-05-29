from cc import peripheral
modem = peripheral.wrap('back')
userMessage = input("Enter message: ")
for _ in range(2)
    modem.transmit(5, 1, userMessage)
    