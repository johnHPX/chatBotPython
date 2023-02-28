import pyttsx3
from random import randint
from datetime import datetime


#configuração de voz
engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty("voice", voice.id)


def escreval(frase):
    print('~' * (len(frase) + 4))
    print(f' {frase}')
    print('~' * (len(frase) + 4))


def reproduzir_voz(frase):
    engine.say(frase)
    engine.runAndWait()


def nomeAleatorio():
    ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
    cont = 0
    nome = ""
    while cont <= 5:
        nome += "" + ABC[randint(0,25)]
        cont += 1
    return nome


def criaArquivos(caminho,nome,extençao, conteudo, modo='a'):
    arquivo = open(f"{caminho}{nome}.{extençao}", f"{modo}", encoding="utf-8")
    arquivo.write(conteudo)


def lerArquivos(caminho,nome,extençao):
    arquivo = open(f"{caminho}{nome}.{extençao}", "r",encoding="utf-8" )
    conteudo = arquivo.readlines()
    return conteudo


def horario(data):
    if data == "hora":
        now = datetime.now()
        hora_de_agora = (f'{now.hour}:{now.minute}')
        return hora_de_agora
    elif data == "data":
        now = datetime.now()
        data_de_hoje = (f'{now.day}/{now.month}/{now.year}')
        return data_de_hoje
