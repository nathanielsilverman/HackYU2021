import speech_recognition as sr
from deep_translator import GoogleTranslator
# from emoji_translate.emoji_translate import Translator

# emo = Translator(exact_match_only=False, randomize=True)
dest_lang = input('What language do you want your lecture in?')
to_translate = 'I want to translate this text'


recognizer = sr.Recognizer()
# while True:
with sr.Microphone() as source:
    print("Talk")
    # audio_text = recognizer.record(source, duration=5)
    audio_text = recognizer.listen(source)
    st = recognizer.recognize_google(audio_text)
    print(type(st))
    print("Time over, thanks")

# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

    try:
        # using google speech recognition
        # text = recognizer.recognize_google(audio_text)
        print("Text: "+recognizer.recognize_google(audio_text))
        translated = GoogleTranslator(source='auto', target=dest_lang).translate(st)
        print(translated)
        # print(emo.emojify(text))
    except:
        print("Sorry, I did not get that")