import wikipedia
from function_Uteis import basicos


def wikipédia(entrada):
    wikipedia.set_lang('pt')
    termo = entrada.split("wikipédia")
    termo_da_pesquisa = termo[1]
    basicos.escreval(f'\033[1;36mpesquisando por {termo_da_pesquisa} no wikipédia\033[m')
    basicos.reproduzir_voz(f'pesquisando por {termo_da_pesquisa} no wikipédia')
    pesquisa = wikipedia.page(termo_da_pesquisa)
    basicos.escreval(f"\033[1;36mAchamos a pagina {pesquisa.title} no wikipédia\033[m")
    basicos.reproduzir_voz(f"Achamos a pagina {pesquisa.title} no wikipédia")
    basicos.escreval("\033[1;36mAgora estamos buscando o conteúdo dela\033[m")
    basicos.reproduzir_voz("Agora estamos buscando o conteúdo dela")
    print(f'\033[1;36mFonte: {pesquisa.url}\033[m')
    print(f'\033[1;36m{pesquisa.content}\033[m')
    basicos.criaArquivos("Pesquisas wikipédia/", f"{pesquisa.title}{basicos.nomeAleatorio()}", "txt", pesquisa.content, "a")
    basicos.reproduzir_voz("você deseja que eu leia?")
    while 1:
        reps = str(input('sim|não: ')).strip().lower()
        if reps == "sim":
            basicos.reproduzir_voz(pesquisa.content)
        elif reps == "não" or reps == "nao":
            basicos.reproduzir_voz("Modo ler desativado")
            break
        else:
            basicos.reproduzir_voz('por favor digite apenas as opção dispoinvies.')
