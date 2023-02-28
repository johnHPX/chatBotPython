from os import system
from function_Uteis import basicos
from function_Uteis import wikipedia
from function_Uteis import pesquisa_web
from function_Uteis import play_musica
from function_Uteis import cpu_check
from function_Uteis import Adiministração


def convesar_annabeth():
    basicos.reproduzir_voz("olá, meu nome é Annabeth!")
    basicos.reproduzir_voz("Estarei lhe ajudando quando você precisar")
    print('-' * 40)
    print('[0] => "\033[35mmostra informações do computador\033[m" ')
    print('[1] => "\033[35mqual o horário atual?\033[m" ')
    print(f'[2] => "\033[35mwikipédia {"pesquisa"}\033[m" ')
    print(f'[3] => "\033[35mabrir página web\033[m" ')
    print(f'[4] => "\033[35mprocurar conteúdo na web\033[m" ')
    print(f'[5] => "\033[35mabrir playlist de músicas\033[m" ')
    print('[6] => "\033[35mmostrar menu novamente\033[m" ')
    print('[7] => "\033[35mlimpe a tela\033[m" ')
    print('[8] => "\033[35mModo administrativo\033[m" ')
    print('[9] => "\033[35mencerrar programa\033[m" ')
    print('-' * 40)
    while 1:
        entrada = str(input('Digite alguma coisa: ')).strip().lower()
        if "horas" in entrada or "hora" in entrada or "data" in entrada or "horário" in entrada:
            horaHorario = basicos.horario("hora") + "-" + basicos.horario("data")
            basicos.reproduzir_voz(horaHorario)
            basicos.escreval(horaHorario)
        elif "wikipédia" in entrada and len(entrada) >= 2:
            wiki = wikipedia.wikipédia(entrada)
        elif "abrir" in entrada and "página" in entrada:
            pwap = pesquisa_web.abir_paginas_web()
        elif 'conteúdo' in entrada and 'web' in entrada:
            pwbc = pesquisa_web.buscar_conteudo_web()
        elif "abrir" in entrada and "músicas" in entrada:
            pmrm = play_musica.reproduzir_musica()
        elif 'informações' in entrada and 'computador' in entrada:
            midc = cpu_check.InforPC()
        elif 'modo' in entrada and 'administrativo':
            adm = Adiministração.func_adm()
        elif 'encerrar' in entrada:
            basicos.reproduzir_voz("encerrando o script!")
            break
        elif 'limpe' in entrada and 'tela' in entrada:
            system('cls') or None
        elif 'menu' in entrada:
            print('-' * 40)
            print('[0] => "\033[35mmostra informações do computador\033[m" ')
            print('[1] => "\033[35mqual o horário atual?\033[m" ')
            print(f'[2] => "\033[35mwikipédia {"pesquisa"}\033[m" ')
            print(f'[3] => "\033[35mabrir página web\033[m" ')
            print(f'[4] => "\033[35mprocurar conteúdo na web\033[m" ')
            print(f'[5] => "\033[35mabrir playlist de músicas\033[m" ')
            print('[6] => "\033[35mmostrar menu novamente\033[m" ')
            print('[7] => "\033[35mlimpe a tela\033[m" ')
            print('[8] => "\033[35mModo administrativo\033[m" ')
            print('[9] => "\033[35mencerrar programa\033[m" ')
            print('-' * 40)
        else:
            print('\033[1;33mAinda não possuo esse comando!\033[m')
            basicos.reproduzir_voz("Ainda não possuo esse comando!")
