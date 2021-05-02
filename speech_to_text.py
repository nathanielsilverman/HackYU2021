import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    audio_text = recognizer.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

    try:
        # using google speech recognition
        print("Text: "+recognizer.recognize_google(audio_text))
    except:
        print("Sorry, I did not get that")
