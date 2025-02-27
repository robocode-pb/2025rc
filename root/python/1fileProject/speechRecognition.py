try:
    import speech_recognition
    import pyttsx3
    import Joking
    from geopy.geocoders import Nominatim
    import webbrowser
except ModuleNotFoundError as e:
    print(e)
    print('pip install SpeechRecognition PyAudio pyttsx3 setuptools Joking geolocator geopy geocoder')
    exit()

engine = pyttsx3.init()
SR = speech_recognition.Recognizer()

def usertextCut(usertext, word):
    if word in usertext:
        return usertext[usertext.find(word) + 1 + len(word):]
    return None

def get_user_location(user_input):
    geolocator = Nominatim(user_agent="location_app")
    try:
        user_location = geolocator.geocode(user_input)
        if user_location:
            return f'{user_location.latitude}, {user_location.longitude}'
    except Exception as e:
        say("Error geo")
    return None

def say(text):
    print(f'say: {text}')
    engine.say(text)
    engine.runAndWait()

def commands(usertext):
    if 'порахуй' in usertext:
        calc = usertextCut(usertext, 'порахуй')
        if not calc:
            return say('No expression to calculate')
        try:
            result = eval(calc)
            say(f'Calculate {calc} = {result}')
        except Exception:
            say('Can`t calculate')
            
                
    if 'жарт' in usertext:
        say(Joking.random_joke())
        
    if 'де' in usertext:
        coordinates = get_user_location(usertextCut(usertext, 'де'))
        if not coordinates:
            return say('No location specified')
        if coordinates:
            webbrowser.open(f"https://www.google.com/maps/place/{coordinates}")
        else:
            say('Can`t find location')
            

def startRecognition():
    print('Ключові слова: порахуй жарт де')
    with speech_recognition.Microphone() as source:
        SR.adjust_for_ambient_noise(source, duration=2)
        say("say the request")
        audio = SR.listen(source)
        print('Decode audio')
        try:
            usertext = SR.recognize_google(audio, language='uk-UA').lower()
            say(f"You said: {usertext}")
            commands(usertext)    
        except speech_recognition.UnknownValueError:
            say("Can't understand audio")
        except Exception as e:
            print("Error:", e)
            say("An error occurred")


startRecognition()