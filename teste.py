import os
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def usingWatson(txt):
    # Configuração da autenticação com o serviço
    authenticator = IAMAuthenticator('Gz4PmmlLUhesM6lzY2RQlV6HuTPam0UjhNMNOvfyPpoX')
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )
    text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/bd7910a4-f9e0-4685-84c5-721896022527')

    # Texto que será convertido em fala
    texto = txt
    # Obtém a lista de vozes disponíveis
    #voices = text_to_speech.list_voices().get_result()
    #print("Voices: \n{}".format(voices))

    # Configuração da saída de áudio
    with open('output.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                texto,
                voice='en-US_AllisonV3Voice',
                accept='audio/wav'
            ).get_result().content)
