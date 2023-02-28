from selenium import webdriver
from webdrivermanager import ChromeDriverManager
from googlesearch import search
from function_Uteis import basicos
import pywhatkit


def buscar_conteudo_web():
    basicos.reproduzir_voz('Qual opção de navegador voçê quer selecionar?')
    navegador = str(input('Pessoal || vitual ')).strip().lower()
    if 'pessoal' not in navegador or 'vitual' not in navegador:
        while 1:
            if navegador == 'pessoal' or navegador == 'vitual':
                break
            print(
                '\033[1;31mSelecione apenas as opções "pessoal" ou "vitual \033[m"')
            navegador = str(input('Pessoal? || vitual? ')).strip().lower()
    basicos.reproduzir_voz("Qual site você deseja que eu procure? ")
    site = str(
        input("\033[1;36mqual site voçê que buscar o conteudo? \033[m")).strip().lower()
    basicos.reproduzir_voz("que conteudo voçê deseja que eu busque?")
    conteudo = str(
        input('\033[1;36mo que voçê quer buscar? \033[m')).strip().lower()
    basicos.reproduzir_voz("Qual a quantidade maxima de links sugeridos? ")
    maxlinks = int(input("\033[1;36mquantidade maxima de links: \033[m"))

    listas_links = []
    print("-=" * 30)
    print(f"\033[1;35m{'Menu links':-^60}\033[m")
    print('=' * 60)
    for resultado in search(f'"{conteudo}" {site}', stop=maxlinks):
        listas_links.append(resultado)
    for id, link in enumerate(listas_links):
        print(f'[{id}] -> {link}')
    basicos.reproduzir_voz("qual link você deseja que eu abra? ")
    while 1:
        reps = int(input("\033[1;36mdigite 999 para sair: \033[m"))
        if reps == 999:
            break
        if reps >= len(listas_links) or reps < 0:
            basicos.reproduzir_voz("Digite apenas numeros validos")
        else:
            if navegador == 'vitual':
                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.get(listas_links[reps])
            else:
                pywhatkit.search(listas_links[reps])
    print("-=" * 30)


def paginas_webs_function():
    paginas_webs_salvas = {}
    lista_keys = []
    pags = basicos.lerArquivos(
        'paginas webs/lista_paginas/', 'keys_paginas_web', 'txt')
    cont = 0
    for c in pags:
        lista_keys.append(c.rstrip("\n"))
        paginas_webs_salvas[f'{lista_keys[cont]}'] = []
        cont += 1
    for key in paginas_webs_salvas.keys():
        paginas = basicos.lerArquivos(f'paginas webs/', f'pagina {key}', 'txt')
        lista = []
        for pagina in paginas:
            lista.append(pagina.rstrip("\n"))
        paginas_webs_salvas[f'{key}'] = lista
    return paginas_webs_salvas


def abir_paginas_web():
    print('=-' * 20)
    paginas_webs_salvas = paginas_webs_function()

    basicos.reproduzir_voz('Aquir estão todas as páginas já registradas')

    print('-' * 40)
    for key in paginas_webs_salvas.keys():
        print(f'  *{key}*')
    print('-' * 40)

    while 1:
        pag = str(input(
            '\033[1;36mQual voçê quer abrir? [digite "exit" para sair] \033[m')).strip().lower()
        if pag == 'exit':
            break
        elif pag in paginas_webs_salvas.keys():
            pywhatkit.search(paginas_webs_salvas[pag][0])
        else:
            print('\033[1;31mAinda não tem essa página cadastrada!')
    print('=-' * 20)


def abir_paginas_web_adm():
    print('==' * 20)
    print(f'\033[1;36m{"ADM Paginas Web".center(40)}\033[m')
    print('==' * 20)
    print('--' * 20)
    print('[1] => \033[1;37m"ver paginas cadastradas"\033[m ')
    print('[2] => \033[1;37m"adicionar uma nova pagina"\033[m ')
    print('[3] => \033[1;37m"excluir uma pagina"\033[m ')
    print('[4] => \033[1;37m"Sair"\033[m ')
    print('--' * 20)

    while 1:

        resp = int(input('\033[1;37mQual você que selecionar?\033[m '))

        if resp == 1:
            paginas_webs_salvas = paginas_webs_function()
            print('--' * 20)
            print(f'{"Paginas Cadastradas".center(40)}')
            print('--' * 20)
            cont = 0
            for key, value in paginas_webs_salvas.items():
                print(f'{cont} => {key:.<30}', end="")
                print(f'\033[1;37m{value}\033[m')
                cont += 1
        elif resp == 2:
            nomePag = str(input('Nome da pagina: ')).strip().lower()
            linkPag = str(input('Link da paginas: ')).strip().lower()
            pws = paginas_webs_function()
            Npag = []
            for c in pws:
                Npag.append(c.rstrip("\n"))
            Npag.append(nomePag)
            NE = ''
            for v in Npag:
                NE += v + "\n"
            basicos.criaArquivos('paginas webs/lista_paginas/',
                                 'keys_paginas_web', 'txt', f'{NE}', 'w')
            basicos.criaArquivos(
                'paginas webs/', f'pagina {nomePag}', 'txt', f'{linkPag}', 'w')
        elif resp == 3:
            pagExcluir = int(
                input('Qual página deseja excluir? ["-1" para cancelar] '))
            if pagExcluir == -1:
                pass
            else:
                listaV = []
                pws = paginas_webs_function()
                for value in pws.values():
                    listaV.append(value)
                newPaginas_webs = {key: pws[key]
                                   for key in pws if pws[key] != listaV[pagExcluir]}
                npw = ''
                for key in newPaginas_webs.keys():
                    npw += key + "\n"
                basicos.criaArquivos(
                    'paginas webs/lista_paginas/', 'keys_paginas_web', 'txt', f'{npw}', 'w')
        else:
            break
