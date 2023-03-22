import pyttsx3

def text_to_audio(text):
    # Cria um objeto engine
    engine = pyttsx3.init()

    # Define as propriedades da voz
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Converte o texto em áudio
    engine.save_to_file(text, 'audio.wav')
    engine.runAndWait()
    engine.stop()

    # Retorna o nome do arquivo gerado
    return 'audio.mp3'
