import psutil
import platform
from function_Uteis import basicos
from time import sleep


def InforPC(): 
    print('==' * 20)
    print(f'\033[1;31m{"Informações do PC".center(40)}\033[m')
    print('==' * 20)

    basicos.reproduzir_voz('Aquir estão as informações do PC')

    info_SO = {'Sistema Operacional': platform.uname().system,
               'Versão': platform.uname().version,
               'Arquitetura do Sistema': platform.uname().machine,
               'Nome do PC': platform.uname().node}
    for key,value in info_SO.items():
        print(f'{key:.<35}', end="")
        print(f'\033[1;37m{value}\033[m')
    print('--' * 20)
    infor_cpu = {'Série do Processador': platform.uname().processor,
                 'Velocidade Atual': round(psutil.cpu_freq().current/1000,1),
                 'Velocidade máxima': round(psutil.cpu_freq().max/1000,1),
                 'Total de Nucleos': psutil.cpu_count(),
                 'Total de Nucleos Físicos': psutil.cpu_count(logical=False)}
    for key,value in infor_cpu.items():
        print(f'{key:.<35}', end="")
        if 'Velocidade' in key:
            print(f'\033[1;37m{value}GHZ\033[m')
        else:
            print(f'\033[1;37m{value}\033[m')
    sleep(2)
    basicos.reproduzir_voz('Informações dos discos rígidos')
    print('--' * 20)
    print(f'\033[1;31m{"Discos Rigidos".center(40)}\033[m')
    print('--' * 20)
    disklist = psutil.disk_partitions()
    i = 0
    print(f"Total de Discos: {len(disklist)}")
    while i < len(disklist):
        print(f'Disco {i}:')
        print(f'Ponto de montagem: \033[1;37m{disklist[i].mountpoint}\033[m')
        print(f'Sistema de Arquivos: \033[1;37m{disklist[i].fstype}\033[m')
        print()
        i += 1
    sleep(2)
    basicos.reproduzir_voz('informações de memória')
    print('--' * 20)
    print(f'\033[1;31m{"Memoria".center(40)}\033[m')
    print('--' * 20)
    infor_Memory = {'Tamanho da memoria': psutil.virtual_memory().total/(1024**3),
                   'Consumo Atual da Memoria': psutil.virtual_memory().percent,
                   'Memoria livre': psutil.virtual_memory().free/(1024**3),
                   'Memoria Usada': psutil.virtual_memory().used/(1024**3)}
    for key,value in infor_Memory.items():
        print(f'{key:.<35}', end="")
        if 'Consumo' in key:
            print(f'\033[1;37m{value}%\033[m')
        else:
            print(f'\033[1;37m{value:.2f}GBs\033[m')
    sleep(2)
    basicos.reproduzir_voz('Informações da rede')
    print('--' * 20)
    print(f'\033[1;31m{"Internet".center(40)}\033[m')
    print('--' * 20)
    bytesNetwork = psutil.net_io_counters(pernic=False)
    infor_net = {'Bytes Enviados': bytesNetwork.bytes_sent/(1024**3),
                 'Bytes Recebidos': bytesNetwork.bytes_recv/(1024**3),
                 'Pacotes Enviados': bytesNetwork.packets_sent,
                 'Pacotes Recebidos': bytesNetwork.packets_recv}
    for key,value in infor_net.items():
        print(f'{key:.<35}', end="")
        if 'Bytes' in key:
            print(f'\033[1;37m{value:.3f}GBs\033[m')
        else:
            print(f'\033[1;37m{value:.2f}Bytes\033[m')
    sleep(2)
    basicos.reproduzir_voz('você que analisar o consumo da sua C.P.U?')
    print('==' * 20)
    print(f'\033[1;31m{"Analise da CPU".center(40)}\033[m')
    print('==' * 20)
    print('--' * 20)
    print('[1] => Ver Média do consumo da CPU')
    print('[2] => Seguir adiante')
    print('--' * 20)

    resp = int(input('Escolha uma opção: '))

    if resp == 1:
        seg = int(input('Você que analisar em quantos segundos?'))
        media = 0
        for c in range(seg):
            print('__' * 10)
            consumo = psutil.cpu_times_percent(interval=1)
            print(f'Consumindo: {consumo.user + consumo.system:.2f}%')
            print(f'Livre: {consumo.idle:.2f}')
            media += consumo.user + consumo.system
        media = media/seg
        print(f'A Média de consumo da CPU durante, {seg} segundos é de: {media:.2f}%')
        print('-=' * 40)
    else:
        print('-=' * 40)