import pyttsx3
import wikipedia
import webbrowser
import speech_recognition as sr
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

#Transformar o texto em áudio
def speak(text):
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

#Transformar o áudio em texto
def listen():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		print("Ouvindo...")
		audio = recognizer.listen(source)
		try:
			text = recognizer.recognize_google(audio, language='pt-BR')
			print(f"Você disse: {text}")
			return text.lower()
		except sr.UnknownValueError:
			return "Não entendi o que você disse."
		except sr.RequestError:
			return "Erro ao aessar o serviço de reconhecimento."
		
#Abrir o wikipedia
def search_wikipedia(query):
	wikipedia.set_lang("pt")
	try:
		result = wikipedia.summary(query, sentences=2)
		speak(result)
		print(result)
	except wikipedia.exceptions.DisambiguationError as e:
		speak("Página não encontrada.")

#Abrir o youtube
def open_youtube():
	url = "https://www.youtube.com/"
	webbrowser.open(url)
	speak("Abrindo o YouTube")

#Vai localizar a farmácia mais próxima conforme a sua localização usando o GEOPY

def find_nearest_pharmacy(location_name= "farmácia"):
	geolocator = Nominatim(user_agent="virtual_assistant")
	try:
		location = geolocator.geocode(location_name, exactly_one=True)
		if location:
			speak(f"Encontrei a farmácia mais próxima conforme a sua localização: {location.address}")
			print(location.address)
		else:
			speak("Não foi possível encontrar uma farmácia próxima.")
	except Exception as e:
		speak("Houve um erro ao tentar localizar uma farmácia.")
		print(f"Erro: {e}")

def main():
	speak("Assistente virtual iniciado.")
	while True:
		command = listen()
		print(f"Comando capturado: {command}")

		if "pesquisar" in command.lower().strip():
			speak("O que você quer pesquisar no Wikipedia? ")
			query = listen()
			search_wikipedia(query)

		elif "youtube" in command:
			open_youtube()
		elif "farmácia" in command:
			find_nearest_pharmacy()
		elif "sair" in command or "fechar" in command:
			speak("Encerrando o sistema. Até mais!")
			break
		else:
			speak("Comando não reconhecido.Tente novamente.")

if __name__ == "__main__":
    main()