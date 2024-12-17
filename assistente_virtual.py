import speech_recognition as sr
import pyttsx3
import wikipedia
import pyjokes
import datetime

# Inicializa o motor de fala
engine = pyttsx3.init()

# Configurações de voz (opcional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 1 para voz feminina, 0 para masculina

# Função para falar (TTS)
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para ouvir (Reconhecimento de fala)
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Estou ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Você disse: ")
        command = recognizer.recognize_google(audio, language='pt-BR')
        print(command)
        return command
    except sr.UnknownValueError:
        speak("Desculpe, não entendi. Pode repetir?")
        return None
    except sr.RequestError:
        speak("Houve um erro na conexão. Tente novamente.")
        return None

# Função para fornecer a hora atual
def tell_time():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    speak(f"Agora são {time}")

# Função para contar uma piada
def tell_joke():
    joke = pyjokes.get_joke(language='pt', category='all')
    speak(joke)

# Função para buscar informações na Wikipedia
def search_wikipedia(query):
    speak("Pesquisando na Wikipedia...")
    result = wikipedia.summary(query, sentences=2, lang='pt')
    speak(result)

# Função principal do assistente virtual
def run_assistant():
    speak("Olá, sou seu assistente virtual. Como posso ajudá-lo?")
    while True:
        command = listen()
        if command is None:
            continue
        command = command.lower()

        if 'hora' in command:
            tell_time()
        elif 'piada' in command:
            tell_joke()
        elif 'wikipedia' in command:
            speak("O que você gostaria de saber?")
            query = listen()
            if query:
                search_wikipedia(query)
        elif 'sair' in command:
            speak("Até logo!")
            break
        else:
            speak("Desculpe, não entendi. Pode repetir?")

# Inicia o assistente
run_assistant()
