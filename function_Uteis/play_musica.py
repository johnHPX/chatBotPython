from function_Uteis import basicos
from random import randint
import pygame


def estilo_musicas_function():
    estilo_musicas = {}
    lista_keys = []
    estilo = basicos.lerArquivos('../musicas/','estilos m','txt')
    cont = 0
    for c in estilo:
        lista_keys.append(c.rstrip("\n"))
        estilo_musicas[f'{lista_keys[cont]}'] = []
        cont += 1
    for key in estilo_musicas.keys():
        try:
            songs = basicos.lerArquivos(f'../musicas/{key}/', f'{key} songs', 'txt')
            lista = []
            for song in songs:
                lista.append(song.rstrip("\n"))
            estilo_musicas[f'{key}'] = lista
        except FileNotFoundError:
            estilo_musicas[key] = []
    return estilo_musicas


def reproduzir_musica():
    try:
        estilo_musicas = estilo_musicas_function()

        print('-=' * 30)
        print(f'\033[1;36m{"menu estilos musicais".center(60)}\033[m')
        print('-=' * 30)

        print('-' * 30)
        for key in estilo_musicas.keys():
            print(f'   * {key}')
        print('-' * 30)

        basicos.reproduzir_voz('Aquir estão todas as playlist já criadas')
        basicos.reproduzir_voz('selecione a playlist que voçê deseja')
        nomePlay = str(input('\033[1;37mQual playlist voçê que selecionar? \033[m')).strip().lower()

        if nomePlay in estilo_musicas.keys():
            NOTMusic = ''
            basicos.reproduzir_voz(f'voçê escolheu a playlist {nomePlay}')
            lista_musicas = []
            for key, musica in estilo_musicas.items():
                if key == nomePlay:
                    if len(musica) > 0:
                        for i, valor in enumerate(musica):
                            lista_musicas.append(valor)
                            print(f'{i} -> \033[1;37m{valor}\033[m')
                    else:
                        NOTMusic = 'não á musicas'
            if NOTMusic == "não á musicas":
                basicos.reproduzir_voz('Não á musicas nessa playlist')
                pass
            else:
                basicos.reproduzir_voz('Escolha entre o modo aleatório ou o modo manual')
                reps = str(input('\033[1;37mmodo aleátorio | modo manual: \033[m')).strip().lower()

                if 'aleátorio' in reps:
                    pygame.mixer.init()
                    repitido = []
                    total_musicas = 0
                    while 1:
                        aleatorio = randint(0, (len(lista_musicas) - 1))
                        if total_musicas == len(lista_musicas):
                            break
                        if aleatorio not in repitido:
                            musica = lista_musicas[aleatorio]
                            pygame.mixer.music.load(f"../musicas/{nomePlay}/{musica}")
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy() == 1:
                                continue
                            repitido.append(aleatorio)
                            total_musicas += 1
                else:
                    pygame.mixer.init()
                    lista_musicas_selecionadas = []
                    max = int(input('\033[1;37mQuantas musicas voçê quer selecionar? \033[m'))
                    for c in range(0, max):
                        music = int(input(f'\033[1;37mqual musica deseja colocar na posição {c}° ? \033[m'))
                        lista_musicas_selecionadas.append(music)
                    for c in range(0, max):
                        musica = lista_musicas[lista_musicas_selecionadas[c]]
                        pygame.mixer.music.load(f"../musicas/{nomePlay}/{musica}")
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy() == 1:
                            continue
        else:
            basicos.reproduzir_voz('Essa playlist não existe')
        print('\033[7mPLAYLIST ENCERRADA!\033[m')
        print('-=' * 30)
    except Exception:
        basicos.reproduzir_voz('um erro aconteceu!, voçê não pode iniciar essa função')
        print('-=' * 20)


def estilosADM():
    print('==' * 20)
    print(f'\033[1;36m{"ADM Estilos musicais".center(40)}\033[m')
    print('==' * 20)
    print('--' * 20)
    print('[1] => \033[1;37m"ver estilos cadastrados"\033[m ')
    print('[2] => \033[1;37m"adicionar um novo estilo"\033[m ')
    print('[3] => \033[1;37m"excluir um estilo"\033[m ')
    print('[4] => \033[1;37m"Sair"\033[m ')
    print('--' * 20)

    while 1:

        resp = int(input('\033[1;37mQual você que selecionar?\033[m '))

        if resp == 1:
            Em = estilo_musicas_function()
            print('--' * 20)
            print(f'{"Estilos Cadastrados".center(40)}')
            print('--' * 20)
            for pos, key in enumerate(Em.keys()):
                print(f'{pos:.<30}', end="")
                print(f'\033[1;37m{key}\033[m')
        elif resp == 2:
            nomePag = str(input('Nome do Estilo: ')).strip().lower()
            estilo = basicos.lerArquivos('../musicas/', 'estilos m', 'txt')
            Nestilo = []
            for c in estilo:
                Nestilo.append(c.rstrip("\n"))
            Nestilo.append(nomePag)
            NE = ''
            for v in Nestilo:
                NE += v + "\n"
            basicos.criaArquivos('../musicas/','estilos m','txt', f'{NE}','w')
        elif resp == 3:
            EstExcluir = int(input('Qual Estilo deseja excluir? ["-1" para cancelar] '))
            if EstExcluir == -1:
                pass
            else:
                estilo = basicos.lerArquivos('../musicas/', 'estilos m', 'txt')
                Nestilo = []
                for c in estilo:
                    Nestilo.append(c.rstrip("\n"))
                Nestilo.pop(EstExcluir)
                NE = ''
                for v in Nestilo:
                    NE += v + "\n"
                basicos.criaArquivos('../musicas/', 'estilos m', 'txt', f'{NE}', 'w')
        else:
            break
