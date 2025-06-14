import pyautogui as py
import os
import time

# === Configurações ===
WAIFU_DIR = 'waifus'
TEMPO_CASAMENTO = 10800  # 3 horas
TEMPO_ESPERA_SEM_WAIFU = 3600  # 1 hora
DELAY_COMANDO = 0.5
DELAY_ENTRE_TENTATIVAS = 1

def encontrar_imagem(imagem_path):
    """
    Procura uma imagem na tela e clica nela se for encontrada.
    """
    try:
        caminho = os.path.join(WAIFU_DIR, imagem_path)
        posicao = py.locateCenterOnScreen(caminho, confidence=0.8)
        if posicao:
            print(f'✅ Waifu encontrada: {imagem_path}')
            py.click(posicao)
            return True
    except Exception:
        print(f'❌ Waifu não encontrada: {imagem_path}')
    return False

def esperar_timer(segundos):
    """
    Mostra um contador regressivo no terminal.
    """
    for x in range(segundos, 0, -1):
        print(f'{x//3600:02}:{(x//60)%60:02}:{x%60:02}', end='\r')
        time.sleep(1)

def executar_loop_de_waifus(lista_waifus):
    """
    Loop principal que busca waifus e tenta casar.
    """
    for _ in range(10):
        py.write('$wa')
        time.sleep(DELAY_COMANDO)
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
            if click_in_react:
                py.click(click_in_react)
                time.sleep(0.5)
                react_found = py.locateCenterOnScreen('reactsemote/react_emote.png')
                if react_found:
                    py.click(react_found)
            time.sleep(0.5)
            print('\n⏰ Esperando para casar novamente... ⏰\n')
            esperar_timer(TEMPO_CASAMENTO)
            print('\n😼 Voltando em busca das gatas... 😼\n')
        else:
            time.sleep(1)
            print('\nNão encontramos 😿, bora tentar de novo...\n')
            time.sleep(1)

def main():
    print('Esperando entrar no chat...')
    time.sleep(5)
    print('\nIniciando Bot...')

    if not os.path.exists(WAIFU_DIR):
        print(f'❌ Pasta "{WAIFU_DIR}" não encontrada.')
        return

    lista_waifus = os.listdir(WAIFU_DIR)
    if not lista_waifus:
        print(f'⚠️ Nenhuma imagem na pasta "{WAIFU_DIR}".')
        return

    while True:
        executar_loop_de_waifus(lista_waifus)
        print("\nNenhuma gata a mais encontrada 😿. Esperando uma horinha ⏰...\n")
        esperar_timer(TEMPO_ESPERA_SEM_WAIFU)
        print('\n😼 Que a sorte esteja conosco... 😼\n')

if __name__ == '__main__':
    main()
