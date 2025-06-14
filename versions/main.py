import pyautogui as py
import concurrent.futures
import os
import time

print('Esperando entrar no chat...')
time.sleep(5)
print('\nIniciando Bot...')

def encontrar_imagem(imagem_path):
    posicao = py.locateCenterOnScreen(f'waifus\{imagem_path}')
    py.click(posicao)
    return posicao is not None

# Lista de caminhos das imagens
directorywaifus = os.listdir('waifus')
lista_waifus = directorywaifus

def analisar_imagem(imagem_path):
    if encontrar_imagem(imagem_path):
        print(f'A imagem {imagem_path} FOI encontrada.\n')
        return True
    else:
        print(f'\nA imagem {imagem_path} NÃO FOI encontrada.')
        return False

while True:
    for c in range(0, 10):
        py.write('$wa')
        time.sleep(0.5)
        py.press('Enter')
        time.sleep(1)
        print('\nEncontramos alguma waifu?')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            resultados = executor.map(analisar_imagem, lista_waifus)
        if any(resultados):
            time.sleep(1)
            print('Se casando com personagem...')
            click_in_react = py.locateCenterOnScreen('reactsemote/react_button.png')
            time.sleep(.5)
            py.click(click_in_react)
            time.sleep(.5)
            react_found = py.locateCenterOnScreen('reactsemote/react_emote.png')
            py.click(react_found)
            time.sleep(.5)
            print('\nEsperando 3 horinhas para se casar novamente...\n')
            for x in range(10800, 0, -1):
                seconds = x % 60
                minutes = int(x / 60) % 60
                hours = int(x / 3600)
                print(f'{hours:02}:{minutes:02}:{seconds:02}')
                time.sleep(1)
            print('\nVoltando em busca das gatas...\n')
        time.sleep(1)
        print('\nnão encontramos, bora tentar de novo...\n')
        time.sleep(1)

    print("\nNenhuma gata a mais encontrada. Esperando uma horinha...\n")

    for x in range(3600, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f'{hours:02}:{minutes:02}:{seconds:02}')
        time.sleep(1)

    print('\nQue a sorte esteja conosco...\n')
