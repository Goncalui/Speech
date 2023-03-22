import openai
import time
from recognization import recognize

from textoToAudio import text_to_audio
from teste import usingWatson

from playsound import playsound

# Configurar a chave de API da OpenAI
openai.api_key = "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"

# Inicializar o histórico de conversa como uma lista vazia
historico = []

# Gerar uma resposta para uma pergunta do usuário
a = 1
def gerar_resposta(pergunta):
    global a
    # Adicionar a pergunta atual ao histórico de conversa
    historico.append(f"Usuário: {pergunta}")
    
    # Concatenar todas as perguntas e respostas anteriores
    prompt = "/n".join(historico)
    
    # Gerar a resposta usando a API do OpenAI

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=124,
      n=1,
      stop=[" Human:", " AI:"],
      temperature=0.9,
    )
    
    # Adicionar a resposta atual ao histórico de conversa
    resposta = response.choices[0].text.strip()
    historico.append(f"OpenAI: {resposta}")
    
    # Retornar a resposta gerada pela API
    return resposta

# Exemplo de uso da função gerar_resposta
import pygame
pygame.init()

while True:
    pergunta = recognize()
    resposta = gerar_resposta(pergunta)

    print(f"OpenAI: {resposta}")
    print(usingWatson(resposta))
    time.sleep(2)

    # Load the music file
    pygame.mixer.music.load("output.wav")

    # Play the music file
    pygame.mixer.music.play()

    # Keep the program running while the music plays
    while pygame.mixer.music.get_busy():
        pass
    # Load the audio  file


