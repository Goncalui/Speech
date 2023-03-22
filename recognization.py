import speech_recognition as sr
import wave
import pyaudio



def recognize():

  correto = 0
  while correto == 0:
    
    # Cria uma instância do recognizer
    r = sr.Recognizer()

    # Define o microfone como a fonte de áudio
    with sr.Microphone() as source:
        # Ajusta o ruído de fundo do microfone
        r.adjust_for_ambient_noise(source)
        print("Fale alguma coisa:")
        # Captura o áudio da fala do usuário
        audio = r.listen(source)
    try:
      # Usa o Google Speech Recognition para transcrever a fala
      text = r.recognize_google(audio, language='en')
      print("Você disse: ", text)
      correto = int(input("Correto = 1, Errado = 0"))
    except:
      input("Não entendi o ue falou, tecle enter para continuar")

  return text
