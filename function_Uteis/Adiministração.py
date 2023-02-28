from function_Uteis import basicos
from function_Uteis import pesquisa_web
from function_Uteis import play_musica


def func_adm():
    print('-=' * 20)
    senha = str(input('Digite sua Senha: ')).strip().lower()

    if senha == '****':
        basicos.reproduzir_voz('funções administrativas')

        print('==' * 20)
        print(f'\033[1;31m{"MENU ADM".center(40)}\033[m')
        print('==' * 20)
        print('--' * 20)
        print('[1] => \033[1;37m"Configurações de páginas"\033[m ')
        print('[2] => \033[1;37m"Configurações de Estilo Musicais"\033[m ')
        print('[3] => \033[1;37m"Sair"\033[m ')
        print('--' * 20)

        while 1:
            resp = int(input('Sua escolha: '))
            if resp == 1:
                pesquisa_web.abir_paginas_web_adm()
            elif resp == 2:
                play_musica.estilosADM()
            else:
                break
    else:
        basicos.reproduzir_voz('Senha incorreta!')
    print('-=' * 20)
