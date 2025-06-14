import pyautogui as py
import os
import time

print('Esperando entrar no chat...')
time.sleep(5)
print('\nIniciando Bot...')

# Lista de imagens
waifu_dir = 'waifus'
lista_waifus = os.listdir(waifu_dir)

def encontrar_imagem(imagem_path):
    try:
        caminho = os.path.join(waifu_dir, imagem_path)
        posicao = py.locateCenterOnScreen(caminho, confidence=0.8)
        if posicao:
            print(f'✅ Waifu encontrada: {imagem_path}')
            py.click(posicao)
            return True
    except Exception:
        print(f'❌ Waifu não encontrada: {imagem_path}')
        return False

while True:
    for c in range(10):
        py.write('$wa')
        time.sleep(0.5)
        py.press('Enter')
        time.sleep(1)

        print('\nProcurando waifus...')
        encontrada = False
        for imagem in lista_waifus:
            if encontrar_imagem(imagem):
                encontrada = True
                break  

        if encontrada:
            time.sleep(1)
            print('\n🎊🎉👰 Se casando com personagem... 👰🎊🎉')
            click_in_react = py.locateCenterOnScreen('reactsemote/react_button.png')
            time.sleep(.5)
            py.click(click_in_react)
            time.sleep(.5)
            react_found = py.locateCenterOnScreen('reactsemote/react_emote.png')
            py.click(react_found)
            time.sleep(.5)
            print('\n⏰ Esperando para casar novamente... ⏰\n')
            for x in range(10800, 0, -1):
                print(f'{x//3600:02}:{(x//60)%60:02}:{x%60:02}', end='\r')
                time.sleep(1)
            print('\n😼 Voltando em busca das gatas... 😼\n')
        time.sleep(1)
        print('\nNão encontramos 😿, bora tentar de novo...\n')
        time.sleep(1)

    print("\nNenhuma gata a mais encontrada 😿. Esperando uma horinha ⏰...\n")
    
    for x in range(3600, 0, -1):
        print(f'{x//3600:02}:{(x//60)%60:02}:{x%60:02}', end='\r')
        time.sleep(1)

    print('\n😼 Que a sorte esteja conosco... 😼\n')
