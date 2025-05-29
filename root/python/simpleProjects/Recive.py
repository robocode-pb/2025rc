from cc import peripheral,redstone
modem = peripheral.wrap('top')
modem.close(5)
for message in modem.receive(5):
    command = message.content.decode()
    print("Recived command: " + command)
    if command == "open":
        redstone.setOutput('front',False)
    if command == "close":
        redstone.setOutput('front',True)
