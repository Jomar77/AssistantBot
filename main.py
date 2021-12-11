import pyttsx3
from random import choice
from functions.online_ops import  get_random_advice, get_random_joke, play_on_youtube, search_on_google
from functions.os_ops import open_calculator, open_notepad, open_photos
from txtToSpeech import speak, greet_user, take_user_input
from utils import apology_text
from pprint import pprint


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()
            speak(choice(apology_text))

        elif 'open calculator' in query:
            open_calculator()
            speak(choice(apology_text))

        elif 'open photos' in query:
            open_photos()
            speak(choice(apology_text))

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, you dumb bitch?')
            video = take_user_input().lower()
            play_on_youtube(video)
            speak(choice(apology_text))

        elif 'google' in query:
            speak('What do you want to search on Google, fucker?')
            query = take_user_input().lower()
            search_on_google(query)
            speak(choice(apology_text))

        elif 'joke' in query:
            speak(f"No friends to tell you one?")
            joke = get_random_joke()
            speak(joke)
            speak("In case you didn't get that I printed it in you low quality screen.")
            pprint(joke)
            speak(choice(apology_text))

        elif "advice" in query:
            speak(f"Here's an advice for you sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)
            speak(choice(apology_text))
        
