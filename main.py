import pyautogui as py
import os
import time

# === Settings ===
WAIFU_DIR = 'waifus'
TEMPO_CASAMENTO = 10800  # 3 hours
TEMPO_ESPERA_SEM_WAIFU = 3600  # 1 hour
DELAY_COMANDO = 0.5
DELAY_ENTRE_TENTATIVAS = 1

def encontrar_imagem(imagem_path):
    """
    Searches for an image on the screen and clicks it if found.
    """
    try:
        caminho = os.path.join(WAIFU_DIR, imagem_path)
        posicao = py.locateCenterOnScreen(caminho, confidence=0.8)
        if posicao:
            print(f'✅ Waifu found: {imagem_path}')
            py.click(posicao)
            return True
    except Exception:
        print(f'❌ Waifu not found: {imagem_path}')
    return False

def esperar_timer(segundos):
    """
    Displays a countdown timer in the terminal.
    """
    for x in range(segundos, 0, -1):
        print(f'{x//3600:02}:{(x//60)%60:02}:{x%60:02}', end='\r')
        time.sleep(1)

def executar_loop_de_waifus(lista_waifus):
    """
    Main loop that searches for waifus and tries to marry them.
    """
    for _ in range(10):
        py.write('$wa')
        time.sleep(DELAY_COMANDO)
        py.press('Enter')
        time.sleep(1)

        print('\nSearching for waifus...')
        encontrada = False
        for imagem in lista_waifus:
            if encontrar_imagem(imagem):
                encontrada = True
                break  

        if encontrada:
            time.sleep(1)
            print('\n🎊🎉👰 Marrying the Waifu... 👰🎊🎉')
            click_in_react = py.locateCenterOnScreen('reactsemote/react_button.png')
            if click_in_react:
                py.click(click_in_react)
                time.sleep(0.5)
                react_found = py.locateCenterOnScreen('reactsemote/react_emote.png')
                if react_found:
                    py.click(react_found)
            time.sleep(0.5)
            print('\n⏰ Waiting to marry again... ⏰\n')
            esperar_timer(TEMPO_CASAMENTO)
            print('\n😼 Back on the hunt... 😼\n')
        else:
            time.sleep(1)
            print('\nNothing found 😿, trying again...\n')
            time.sleep(1)

def main():
    print('Waiting to enter the chat...')
    time.sleep(5)
    print('\nStarting Bot...')

    if not os.path.exists(WAIFU_DIR):
        print(f'❌ Folder "{WAIFU_DIR}" not found.')
        return

    lista_waifus = os.listdir(WAIFU_DIR)
    if not lista_waifus:
        print(f'⚠️ No images in the "{WAIFU_DIR}" folder.')
        return

    while True:
        executar_loop_de_waifus(lista_waifus)
        print("\nNo more waifus found 😿. Waiting one hour ⏰...\n")
        esperar_timer(TEMPO_ESPERA_SEM_WAIFU)
        print('\n😼 May luck be with us... 😼\n')

if __name__ == '__main__':
    main()
