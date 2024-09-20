import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import urllib.parse  # Used for URL encoding when performing searches

# Setting up recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to have the assistant speak aloud
def speak(message):
    engine.say(message)
    engine.runAndWait()

# Function to capture voice input
def capture_voice():
    with sr.Microphone() as source:
        print("I'm listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for any background sounds
        audio_data = recognizer.listen(source)

        try:
            print("Interpreting speech...")
            command = recognizer.recognize_google(audio_data, language='en-US')
            print(f"You said: {command}")
            return command.lower()  # Return as lowercase for easier processing
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            speak("I couldn't understand. Please say that again.")
            return "None"
        except sr.RequestError:
            print("Connection issue detected.")
            speak("Unable to reach the network.")
            return "None"

# Function to process and respond to user commands
def handle_command(command):
    # Basic greeting
    if "hello" in command:
        speak("Hello! How may I assist you today?")

    # Provide current time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time right now is {current_time}")

    # Provide current date
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")

    # Perform a web search
    elif "search" in command:
        speak("What would you like to search for?")
        search_term = capture_voice()  # Listen for what user wants to search
        if search_term and search_term != "None":
            encoded_term = urllib.parse.quote(search_term)
            # Open the browser with the search query
            webbrowser.open(f"https://www.google.com/search?q={encoded_term}")
            speak(f"Here are your search results for {search_term}")
        else:
            speak("I didn't catch your search request.")

    # Stop the assistant
    elif "stop" in command:
        speak("Goodbye.")
        exit()  # Exit the program

    # Default response for unrecognized commands
    else:
        speak("I'm sorry, I didn't understand that.")

# Main loop to keep listening and responding
def run_assistant():
    speak("Voice Assistant is now online.")
    while True:
        user_command = capture_voice()  # Get the voice input
        if user_command and user_command != "None":
            handle_command(user_command)  # Process the input
        if "stop" in user_command:  # Break the loop if "stop" command is given
            break

if __name__ == "__main__":
    run_assistant()
